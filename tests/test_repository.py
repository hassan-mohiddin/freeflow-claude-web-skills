import hashlib
import tempfile
import unittest
import zipfile
from pathlib import Path

from scripts.repository import (
    BUNDLE_NAME,
    EXPECTED_SKILLS,
    RELEASE_VERSION,
    build_release,
    discover_skills,
    interaction_contract_from_readme,
    validate_repository,
)

ROOT = Path(__file__).resolve().parents[1]


class RepositoryStructureTests(unittest.TestCase):
    def test_claude_skill_inventory_is_exact(self) -> None:
        self.assertEqual(EXPECTED_SKILLS, set(discover_skills(ROOT)))

    def test_local_state_and_artifacts_are_gitignored(self) -> None:
        ignore_rules = (ROOT / ".gitignore").read_text(encoding="utf-8").splitlines()
        for required_rule in (".freeflow/", ".serena/", "dist/"):
            with self.subTest(required_rule=required_rule):
                self.assertIn(required_rule, ignore_rules)

    def test_required_public_files_exist(self) -> None:
        for relative_path in (
            "README.md",
            "LICENSE",
            "INTERACTION_CONTRACT.md",
            "MANIFEST.md",
            "CHANGELOG.md",
            "SECURITY.md",
        ):
            with self.subTest(relative_path=relative_path):
                self.assertTrue((ROOT / relative_path).is_file())

    def test_readme_contract_matches_canonical_file(self) -> None:
        expected = (ROOT / "INTERACTION_CONTRACT.md").read_text(encoding="utf-8")
        actual = interaction_contract_from_readme(ROOT / "README.md")
        self.assertEqual(expected.rstrip(), actual.rstrip())

    def test_repository_validation_has_no_findings(self) -> None:
        self.assertEqual([], validate_repository(ROOT))


class ReleasePackagingTests(unittest.TestCase):
    def test_release_contains_bundle_and_individual_skill_archives(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = Path(temporary_directory)
            result = build_release(ROOT, output)

            bundle = output / BUNDLE_NAME
            self.assertTrue(bundle.is_file())
            self.assertEqual(1 + len(EXPECTED_SKILLS), len(result.archives))

            for skill in EXPECTED_SKILLS:
                archive_path = output / "skills" / f"{skill}-{RELEASE_VERSION}.zip"
                self.assertTrue(archive_path.is_file())
                with zipfile.ZipFile(archive_path) as archive:
                    roots = {name.split("/", 1)[0] for name in archive.namelist()}
                    self.assertEqual({skill}, roots)
                    self.assertIn(f"{skill}/SKILL.md", archive.namelist())
                    self.assertFalse(
                        any("/agents/" in name for name in archive.namelist())
                    )

            with zipfile.ZipFile(bundle) as archive:
                names = set(archive.namelist())
                bundle_root = "freeflow-claude-web-skills"
                self.assertIn(f"{bundle_root}/README.txt", names)
                self.assertIn(f"{bundle_root}/SKILL_CHECKSUMS.sha256", names)
                for skill in EXPECTED_SKILLS:
                    expected = (
                        f"{bundle_root}/skills/{skill}-{RELEASE_VERSION}.zip"
                    )
                    self.assertIn(expected, names)

    def test_release_is_reproducible_and_checksums_match(self) -> None:
        with (
            tempfile.TemporaryDirectory() as first_directory,
            tempfile.TemporaryDirectory() as second_directory,
        ):
            first = Path(first_directory)
            second = Path(second_directory)
            build_release(ROOT, first)
            build_release(ROOT, second)

            first_files = {
                path.relative_to(first): hashlib.sha256(
                    path.read_bytes()
                ).hexdigest()
                for path in first.rglob("*.zip")
            }
            second_files = {
                path.relative_to(second): hashlib.sha256(
                    path.read_bytes()
                ).hexdigest()
                for path in second.rglob("*.zip")
            }
            self.assertEqual(first_files, second_files)

            checksum_lines = (first / "CHECKSUMS.sha256").read_text(
                encoding="utf-8"
            ).splitlines()
            expected_lines = [
                f"{digest}  {path.as_posix()}"
                for path, digest in sorted(first_files.items())
            ]
            self.assertEqual(expected_lines, checksum_lines)


if __name__ == "__main__":
    unittest.main()
