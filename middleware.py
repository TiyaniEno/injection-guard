import re
from urllib.parse import unquote
from werkzeug.wrappers import Request, Response

BLOCKED = re.compile(r'[;|&$`]|\\$\\(|\\.\\./|\\n|\\r|%0a|%3b', re.I)

class InjectionGuardMiddleware:
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        req = Request(environ)
        raw = req.path + str(req.query_string) + str(req.get_data())
        payload = unquote(raw)
        if BLOCKED.search(payload):
            res = Response('Blocked by injection-guard', status=403)
            return res(environ, start_response)
        return self.app(environ, start_response)
