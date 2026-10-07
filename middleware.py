import re
from urllib.parse import unquote
from werkzeug.wrappers import Request, Response

BLOCKED = re.compile(r'(;|\||\$\(|`|\${|\.\./|\n|\r)', re.I)

class InjectionGuardMiddleware:
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        req = Request(environ)
        qs = req.query_string.decode('utf-8', 'ignore')
        # don't consume body, read limited
        raw = req.path + "?" + qs
        payload = unquote(raw).lower()
        if BLOCKED.search(payload) or BLOCKED.search(raw.lower()):
            res = Response('Blocked by injection-guard-waf', status=403)
            return res(environ, start_response)
        return self.app(environ, start_response)
