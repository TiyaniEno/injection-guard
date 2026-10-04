import re
from werkzeug.wrappers import Request, Response

BLOCKED = re.compile(r'[;|&$`\(\)\{\}\n\r]|\.\./')

class InjectionGuardMiddleware:
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        req = Request(environ)
        payload = str(req.args) + str(req.form) + req.path
        if BLOCKED.search(payload):
            res = Response('Blocked by injection-guard', status=403)
            return res(environ, start_response)
        return self.app(environ, start_response)
