# injection-guard-waf

Lightweight WAF middleware for Python. First line of defense against OS command injection.

Stops basic payloads like `; ls -la`, `| cat /etc/passwd`, `$()`, `../`

# injection-guard-waf

### Install
```bash
pip install injection-guard-waf
```

### Use
```python
from middleware import InjectionGuardMiddleware
``` 

### Use (Flask example)
from flask import Flask
from middleware import InjectionGuardMiddleware

app = Flask(__name__)
app.wsgi_app = InjectionGuardMiddleware(app.wsgi_app)

### What it does and doesn't do
- ✅ Blocks common injection chars: ; | & $ ` () {} ../ %0a %3b
- ✅ Checks URL, querystring and body with unquote
- ⚠️ This is NOT a replacement for proper input validation, allow-lists, or a certified WAF. Use as one layer only.

### 💼 Enterprise & Support
Free for personal use & learning. MIT License.

| Plan | Price | What you get |
|------|-------|--------------|
| Free | R0 | Basic WAF middleware (as-is) |
| Starter | R750 once | Help installing + 30 min call |
| Business | R2500/mo | Custom rules for your app + WhatsApp support (best-effort) |
| Enterprise | R15000 once | 4-hour consultation + integration guidance + review of your usage (Not a certified security audit) |

Contact: via GitHub Issues / Discussions. Sponsor button at top of page.
