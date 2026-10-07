from .middleware import InjectionGuardMiddleware

__version__ = "1.0.0"
__all__ = ["InjectionGuardMiddleware"]

# alias for backward compat
InjectionGuard = InjectionGuardMiddleware
