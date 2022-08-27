# Roteamento (sem metodos/verbos)
# - agora rotas são especificadas (independente do metodo)
# - se uma rota não for encontrada, vai mostrar apenas (None, 200)

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
    
    def route(self, path: str):
        def wrapper(handler: 'Callable[[Request, Response], None]'):
            self._routes[path] = handler
            return handler

        return wrapper
    
    def _handle_request(self, request: 'Request') -> 'Response':
        response = Response()

        for path, handler in self._routes.items():
            if path == request.path:
                handler(request, response)
                return response

        return response
