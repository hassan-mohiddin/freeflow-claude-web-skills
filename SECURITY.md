# Security

Agent Skills contain instructions that can influence Claude's tool use and may include supporting files. Review downloaded skill contents before installing them and install only artifacts from releases you trust.

## Reporting a vulnerability

Do not disclose an exploitable issue in a public GitHub issue. Report it privately through the repository's security reporting feature when available, or contact the maintainer through the upstream [Freeflow repository](https://github.com/hassan-mohiddin/freeflow).

Include the affected skill, version, reproduction steps, potential impact, and any known mitigation. Do not include credentials, personal data, or secrets.

## Safety boundaries

- Installing a skill does not grant a tool or permission Claude does not already have.
- Review sensitive write, deployment, billing, security, or destructive actions at the point of use.
- The Freeflow Interaction Contract reduces accidental action inference; it is not a sandbox or policy enforcement mechanism.
- Verify release checksums when provenance matters.
