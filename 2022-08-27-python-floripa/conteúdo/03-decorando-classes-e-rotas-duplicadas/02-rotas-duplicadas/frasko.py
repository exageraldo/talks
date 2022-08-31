from typing import Dict, Callable, List, Optional, Tuple
import inspect
from webob import Response, Request
from parse import parse

class FraskoException(Exception):
    """ A base class for exceptions used by frasko. """
    pass

class Frasko:
    def __init__(self) -> None:
        self._routes = {}

    def __call__(
        self,
        environ: 'Dict',
        start_response: 'Callable[[str, List, Optional[Tuple]], Callable]',
    ):
        request = Request(environ)
        response = self._handle_request(request)

        return response(environ, start_response)
    
    def _default_response(self, response: 'Response') -> None:
        response.text = "NOT FOUND"
        response.status_code = 404
    
    def route(self, path, method="get"):
        def wrapper(handler):
            self.add_route(path, handler, method)
            return handler
        return wrapper

    def add_route(self, path, handler, method="get"):
        if inspect.isclass(handler):
            methods = set(vars(handler).keys()) & set(
                ["get", "post", "put", "delete"]
            )
            for method in methods:
                routes = self._routes.setdefault(method, {})
                if path in routes:
                    raise FraskoException("Such route already exists.")
                routes[path] = getattr(handler(), method)
        else:
            routes = self._routes.setdefault(method, {})
            if path in routes:
                raise FraskoException("Such route already exists.")
            routes[path] = handler
    
    def _handle_request(self, request: 'Request') -> 'Response':
        response = Response()
        routes = self._routes.get(request.method.lower(), {})
        for path, handler in routes.items():
            parse_result = parse(path, request.path)
            if parse_result is None:
                continue

            handler(request, response, **parse_result.named)
            return response

        self._default_response(response)
        return response
