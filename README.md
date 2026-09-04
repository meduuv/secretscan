# SecretScan

> Find accidental secrets before they leave the machine.

SecretScan is a lightweight, local source scanner for spotting common API keys, tokens, passwords, and credential-like values in project files.

## Highlights

- Scans source and configuration files for common secret patterns
- Read-only analysis
- Designed to avoid printing discovered secret values
- Useful for local pre-commit and security-review workflows
- Lightweight and easy to integrate into developer tooling

## Usage

```bash
secretscan .
secretscan ./src
```

Use the scanner against code and configuration you are authorized to inspect. Treat any finding as potentially sensitive and rotate exposed credentials when appropriate.

## Workflow

```text
project files
     ↓
pattern matching
     ↓
findings
     ↓
review / remediation
```

## Why it exists

Accidental credentials often enter repositories through configuration files, debug output, copied examples, or temporary development files. SecretScan provides a small local check that can sit alongside other defensive tooling.

## Development

```bash
python -m unittest discover -s tests -v
```

## Security

SecretScan is an inspection tool. It does not authenticate to services, exfiltrate findings, or modify scanned files.

## License

MIT

Built by **Meduuv**.

[More projects](https://github.com/meduuv?tab=repositories) · [guns.lol/meduu](https://guns.lol/meduu)
