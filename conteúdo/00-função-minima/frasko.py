# Criando a interface minima (função)
# - independente da rota/metodo, a resposta será sempre a mesma
# - não podemos definir/criar nenhuma rota ainda. é a estrutura/interface minima esperada

from typing import Dict, Callable, List, Optional, Tuple

from webob import Response, Request


def frasko(
    environ: 'Dict',
    start_response: 'Callable[[str, List, Optional[Tuple]], Callable]',
):
    '''
    environ: the environ dictionary is required to contain these CGI environment variables
    start_response: start_response(status, response_headers, exc_info=None) -> write(text_in_bytes)
    '''

    request = Request(environ) # vamos usar jaja
    response = Response()
    response.text = "passo 00"
    response.status_code = 200

    return response(environ, start_response)


# sample_environ = {
#     'HTTP_ACCEPT': '*/*',
#     'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br',
#     'HTTP_CONNECTION': 'close',
#     'HTTP_HOST': '127.0.0.1:8000',
#     'HTTP_USER_AGENT': 'Thunder Client (https://www.thunderclient.com)',
#     'PATH_INFO': '/',
#     'QUERY_STRING': '',
#     'RAW_URI': '/',
#     'REMOTE_ADDR': '127.0.0.1',
#     'REMOTE_PORT': '59398',
#     'REQUEST_METHOD': 'GET',
#     'SCRIPT_NAME': '',
#     'SERVER_NAME': '127.0.0.1',
#     'SERVER_PORT': '8000',
#     'SERVER_PROTOCOL': 'HTTP/1.1',
#     'SERVER_SOFTWARE': 'gunicorn/20.0.4',
#     'gunicorn.socket': "<socket.socket fd=9, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8000), raddr=('127.0.0.1', 59398)>", # object
#     'wsgi.errors': "<gunicorn.http.wsgi.WSGIErrorsWrapper object at 0x10e0369b0>", # object
#     'wsgi.file_wrapper': "<class 'gunicorn.http.wsgi.FileWrapper'>", # object
#     'wsgi.input': "<gunicorn.http.body.Body object at 0x10e301960>", # object
#     'wsgi.input_terminated': True,
#     'wsgi.multiprocess': False,
#     'wsgi.multithread': False,
#     'wsgi.run_once': False,
#     'wsgi.url_scheme': 'http',
#     'wsgi.version': (1, 0)
# }
