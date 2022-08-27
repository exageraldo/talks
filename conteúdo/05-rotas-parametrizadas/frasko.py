# Parametrização das rotas
# - parametros podem ser definidos nas rotas e serão
#   passados via parametros para as funções

from typing import Dict, Callable, List, Optional, Tuple

from webob import Response, Request
from parse import parse


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
    
    def route(self, path: str, method="get"):
        routes = self._routes.setdefault(method, {})
        def wrapper(handler: 'Callable[[Request, Response], None]'):
            routes[path] = handler
            return handler

        return wrapper
    
    def _default_response(self, response: 'Response') -> None:
        response.text = "NOT FOUND"
        response.status_code = 404
    
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
