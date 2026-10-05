# 🛡️ injection-guard

Industrial WAF middleware that blocks OS command injection in 2 lines.

Stops attacks like:
- `; ls -la`
- `&& cat /etc/passwd`
- `| whoami`
- `$(id)`

## Install
```bash
pip install git+https://github.com/TiyaniEno/injection-guard.git
