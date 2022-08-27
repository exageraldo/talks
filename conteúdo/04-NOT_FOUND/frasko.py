# 404 - "NOT FOUND"
# - sempre que uma rota não for encontrada, vai enviar o
#   status code 404 e a mensagem "NOT FOUND" na resposta

from typing import Dict, Callable, List, Optional, Tuple

from webob import Response, Request


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

    def _set_default_response(self, response: 'Response') -> None:
        response.text = "NOT FOUND"
        response.status_code = 404
    
    def _handle_request(self, request: 'Request') -> 'Response':
        response = Response()
        routes = self._routes.get(request.method.lower(), {})
        for path, handler in routes.items():
            if path != request.path:
                continue

            handler(request, response)
            return response

        self._set_default_response(response)
        return response
