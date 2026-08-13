from __future__ import annotations

import hashlib
import re
import shutil
import zipfile
from dataclasses import dataclass
from pathlib import Path

RELEASE_VERSION = "0.1.1"
BUNDLE_NAME = "freeflow-claude-web-skills.zip"
EXPECTED_SKILLS = {
    "bypass",
    "commit-work",
    "decision-gate",
    "design-for-depth",
    "diagnose-failure",
    "discuss",
    "execute-work",
    "finish-branch",
    "handoff",
    "launch-work",
    "migration-work",
    "mode-contract",
    "release-work",
    "review-artifact",
    "review-work",
    "simplify-code",
    "tdd",
    "track-work",
    "verify-work",
    "workflow",
    "write-plan",
    "write-spec",
}

_NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
_FRONTMATTER_PATTERN = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
_INSTRUCTIONS_PATTERN = re.compile(
    r"<!-- CLAUDE-INSTRUCTIONS:START -->\s*"
    r"```markdown\n(.*?)\n```\s*"
    r"<!-- CLAUDE-INSTRUCTIONS:END -->",
    re.DOTALL,
)
_FORBIDDEN_PATH_PARTS = {".DS_Store", "__MACOSX", "__pycache__", "node_modules"}
_BUNDLE_README = """Freeflow Skills for Claude Web

This is a download bundle, not a Claude skill upload.

1. Extract this archive.
2. Open https://claude.ai/customize/skills.
3. Upload each ZIP from the skills directory separately.
4. Enable the uploaded skills.
5. Add the Freeflow instructions (Interaction Contract + Skills Bootstrap) to
   Claude's account-wide instructions as documented in the repository README.

Repository:
https://github.com/hassan-mohiddin/freeflow-claude-web-skills
"""


@dataclass(frozen=True)
class ReleaseResult:
    archives: tuple[Path, ...]
    checksums: Path


def discover_skills(root: Path) -> list[str]:
    skills_root = root / "skills"
    if not skills_root.is_dir():
        return []
    return sorted(
        path.name
        for path in skills_root.iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    )


def claude_instructions_from_readme(readme: Path) -> str:
    text = readme.read_text(encoding="utf-8")
    match = _INSTRUCTIONS_PATTERN.search(text)
    if match is None:
        raise ValueError("README Claude instructions block is missing")
    return match.group(1)


def _frontmatter(skill_file: Path) -> dict[str, str]:
    text = skill_file.read_text(encoding="utf-8")
    match = _FRONTMATTER_PATTERN.match(text)
    if match is None:
        return {}

    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line or line.startswith((" ", "\t", "#")) or ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"\'')
    return fields


def _skill_files(skill_root: Path) -> list[Path]:
    return sorted(
        path
        for path in skill_root.rglob("*")
        if path.is_file()
        and not any(part in _FORBIDDEN_PATH_PARTS for part in path.parts)
    )


def _validate_skill(root: Path, name: str) -> list[str]:
    findings: list[str] = []
    skill_root = root / "skills" / name
    skill_file = skill_root / "SKILL.md"

    if not skill_file.is_file():
        return [f"skills/{name}/SKILL.md: required file is missing"]

    manifests = [
        path
        for path in skill_root.rglob("*")
        if path.is_file() and path.name.lower() == "skill.md"
    ]
    if manifests != [skill_file]:
        findings.append(f"skills/{name}: must contain exactly one SKILL.md")

    fields = _frontmatter(skill_file)
    manifest_name = fields.get("name", "")
    description = fields.get("description", "")
    if manifest_name != name:
        findings.append(f"skills/{name}/SKILL.md: name must match its directory")
    if not _NAME_PATTERN.fullmatch(manifest_name) or len(manifest_name) > 64:
        findings.append(f"skills/{name}/SKILL.md: invalid Agent Skills name")
    if not description or len(description) > 1024:
        findings.append(f"skills/{name}/SKILL.md: invalid description")

    skill_root_resolved = skill_root.resolve()
    for markdown_file in skill_root.rglob("*.md"):
        text = markdown_file.read_text(encoding="utf-8")
        for target in _LINK_PATTERN.findall(text):
            target_path = target.split("#", 1)[0]
            is_external = "://" in target_path or target_path.startswith("mailto:")
            if not target_path or is_external:
                continue
            resolved = (markdown_file.parent / target_path).resolve()
            try:
                resolved.relative_to(skill_root_resolved)
            except ValueError:
                relative_file = markdown_file.relative_to(root)
                findings.append(
                    f"{relative_file}: link escapes skill root: {target}"
                )
                continue
            if not resolved.exists():
                findings.append(
                    f"{markdown_file.relative_to(root)}: missing link target: {target}"
                )

    for forbidden in (
        skill_root / "agents" / "openai.yaml",
        skill_root / ".claude-plugin",
    ):
        if forbidden.exists():
            findings.append(
                f"{forbidden.relative_to(root)}: host-specific metadata is not allowed"
            )

    files = _skill_files(skill_root)
    if len(files) > 500:
        findings.append(f"skills/{name}: exceeds 500 files")
    for path in files:
        if path.stat().st_size > 25 * 1024 * 1024:
            findings.append(f"{path.relative_to(root)}: exceeds 25 MB uncompressed")
        if path.is_symlink():
            findings.append(f"{path.relative_to(root)}: symlinks are not allowed")

    return findings


def validate_repository(root: Path) -> list[str]:
    root = root.resolve()
    findings: list[str] = []
    actual = set(discover_skills(root))
    if actual != EXPECTED_SKILLS:
        missing = sorted(EXPECTED_SKILLS - actual)
        extra = sorted(actual - EXPECTED_SKILLS)
        if missing:
            findings.append(f"skills/: missing expected skills: {', '.join(missing)}")
        if extra:
            findings.append(f"skills/: unexpected skills: {', '.join(extra)}")

    for required in (
        "README.md",
        "LICENSE",
        "INTERACTION_CONTRACT.md",
        "CLAUDE_INSTRUCTIONS.md",
        "MANIFEST.md",
        "CHANGELOG.md",
        "SECURITY.md",
    ):
        if not (root / required).is_file():
            findings.append(f"{required}: required public file is missing")

    readme = root / "README.md"
    instructions = root / "CLAUDE_INSTRUCTIONS.md"
    if readme.is_file() and instructions.is_file():
        try:
            embedded = claude_instructions_from_readme(readme)
        except ValueError as error:
            findings.append(f"README.md: {error}")
        else:
            canonical = instructions.read_text(encoding="utf-8").rstrip()
            if embedded.rstrip() != canonical:
                findings.append("README.md: embedded Claude instructions have drifted")

    for name in sorted(actual):
        findings.extend(_validate_skill(root, name))

    return findings


def _write_zip(archive_path: Path, entries: list[tuple[str, bytes]]) -> None:
    archive_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(
        archive_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as archive:
        for archive_name, content in sorted(entries):
            info = zipfile.ZipInfo(archive_name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, content, compresslevel=9)


def _entries_for_skill(skill_root: Path) -> list[tuple[str, bytes]]:
    return [
        (
            f"{skill_root.name}/{path.relative_to(skill_root).as_posix()}",
            path.read_bytes(),
        )
        for path in _skill_files(skill_root)
    ]


def _checksum_lines(paths: list[Path], relative_to: Path) -> list[str]:
    return [
        f"{hashlib.sha256(path.read_bytes()).hexdigest()}  "
        f"{path.relative_to(relative_to).as_posix()}"
        for path in sorted(
            paths, key=lambda item: item.relative_to(relative_to).as_posix()
        )
    ]


def build_release(root: Path, output: Path) -> ReleaseResult:
    root = root.resolve()
    output = output.resolve()
    skills_root = root / "skills"
    if output in (root, skills_root) or skills_root in output.parents:
        raise ValueError("output directory overlaps repository source")

    findings = validate_repository(root)
    if findings:
        raise ValueError("repository validation failed:\n" + "\n".join(findings))

    output.mkdir(parents=True, exist_ok=True)
    individual_root = output / "skills"
    if individual_root.exists():
        try:
            shutil.rmtree(individual_root)
        except OSError as error:
            message = f"cannot clear output directory {individual_root}: {error}"
            raise ValueError(message) from error
    for old_file in output.glob("*.zip"):
        try:
            old_file.unlink()
        except OSError as error:
            message = f"cannot remove old archive {old_file}: {error}"
            raise ValueError(message) from error

    individual_archives: list[Path] = []
    for name in sorted(EXPECTED_SKILLS):
        archive_path = individual_root / f"{name}-{RELEASE_VERSION}.zip"
        _write_zip(archive_path, _entries_for_skill(root / "skills" / name))
        individual_archives.append(archive_path)

    skill_checksum_lines = _checksum_lines(individual_archives, individual_root)
    bundle_root = "freeflow-claude-web-skills"
    bundle_entries: list[tuple[str, bytes]] = [
        (f"{bundle_root}/README.txt", _BUNDLE_README.encode()),
        (
            f"{bundle_root}/SKILL_CHECKSUMS.sha256",
            ("\n".join(skill_checksum_lines) + "\n").encode(),
        ),
    ]
    bundle_entries.extend(
        (
            f"{bundle_root}/skills/{archive_path.name}",
            archive_path.read_bytes(),
        )
        for archive_path in individual_archives
    )
    bundle_archive = output / BUNDLE_NAME
    _write_zip(bundle_archive, bundle_entries)

    archives = [bundle_archive, *individual_archives]
    checksum_file = output / "CHECKSUMS.sha256"
    checksum_lines = _checksum_lines([bundle_archive], output)
    checksum_file.write_text("\n".join(checksum_lines) + "\n", encoding="utf-8")

    return ReleaseResult(tuple(archives), checksum_file)
