# Criando a interface minima (classe)
# - independente da rota/metodo, a resposta será sempre a mesma
# - não podemos definir/criar nenhuma rota ainda. é a estrutura/interface minima esperada

from typing import Dict, Callable, List, Optional, Tuple

from webob import Response, Request

class Frasko:

    def __call__(
        self,
        environ: 'Dict',
        start_response: 'Callable[[str, List, Optional[Tuple]], Callable]',
    ):
        request = Request(environ)
        response = self._handle_request(request)

        return response(environ, start_response)
    
    def _handle_request(self, request: 'Request') -> 'Response':
        response = Response("passo 01", 200)

        return response
