# Security Checks

This project uses two security tools in pull requests:
1. `bandit`: Analyzes Python code for security issues
2. `detect-secrets`: Scans for hardcoded secrets and credentials

## Running Security Checks Locally

The security tools are included in requirements.txt. After installing dependencies, you can run:

```bash
# Scan code for security issues
bandit -r . --severity-level medium --confidence-level medium -f txt -x "./venv-*/*,./tests/*,./chroma_*/*"

# Scan for hardcoded secrets
detect-secrets scan --exclude-files 'venv-*/*|tests/*|.*\.pyc|.*\.git/*|chroma_*/*' .
```

Note: Never commit API keys or sensitive information to the repository.
