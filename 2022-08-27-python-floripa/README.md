# Frasko - Desenvolvendo seu próprio nano web framework

> Versão "Se vira nos 30"

Evento: 65º Python Floripa ([Meetup](https://www.meetup.com/Floripa-Python-Meetup/events/287387578/))

Apresentação: [YouTube](https://youtu.be/b6Ow1eBy7RI?t=1252)

Slides: [PDF](frasko-desenvolvendo-seu-proprio-nano-web-framework.pdf) / [SpeakerDeck](https://speakerdeck.com/exageraldo/65o-python-floripa-frasko-desenvolvendo-seu-proprio-nano-web-framework)

## Changelog

<ul>
    <li><details><summary>30/08/2022</summary>
        <ul>
            <li>Correção de alguns slides</li>
            <li>Remoção do "gunicorn" das dependências</li>
            <li>Criação do material no README</li>
        </ul>
    </details></li>
    <li><details><summary>31/08/2022</summary>
        <ul>
            <li>Revisão textual (Muito obrigado <a target="_blank" href="https://github.com/lucasjct">@lucasjct</a>)</li>
        </ul>
    </details></li>
</ul>

## Conteúdo

- 00 - [Razões, considerações e referências](#00---razões-considerações-e-referências)
- 01 - [Web App, Web Server e WSGI](#01---web-server-web-app-e-wsgi)
- 02 - [Dependências](#02---dependências)
- 03 - [Montando nossos objetos de `Request` e `Response`](#03---montando-nossos-objetos-de-request-e-response)
- 04 - [Roteamento simples, parametrizado e rota padrão (404)](#04---roteamento-simples-parametrizado-e-rota-padrão-404)
- 05 - [Decorando classes e lidando com rotas duplicadas](#05---decorando-classes-e-lidando-com-rotas-duplicadas)

## 00 - Razões, considerações e referências

### Por que vamos criar nosso proprio framework?

- Por que criar um seu proprio ____?
- **Por razões de aprendizado/estudo**;
- por precisar de algo muito específico/não existente ainda;
- Por que não?

### Considerações iniciais

#### Sugestões para melhor acompanhar esse conteúdo

- Já possua alguma familiaridade com Python;
- Possua um conhecimento mínimo sobre web;
- Já tenha utilizado algum framework web.

#### O que é "Frasko"?

É um framework (ou pelo menos a ideia de um) feito para fins de estudo/ensino sobre conceitos básicos/iniciais de um framework web. A maioria das referências foram tiradas do Flask, inclusive o nome (`flask` significa frasco/garrafa em português).

#### O que seria um "nano framework"?

Em questão de números, `Nano` (10^-9) é menor do que `Micro` (10^-6); já documentação do Flask podemos ter uma ideia do que "microframework" significa ([link](https://flask.palletsprojects.com/en/2.1.x/foreword/#what-does-micro-mean)). Dessa forma, podemos tomar a referência de que nosso nano framework vai ser bem simples, com funcionalidades mínimas para seu funcionamento.

#### Código

Os códigos desse tutorial estão disponíveis na pasta `conteúdo`.

Todos eles estão prontos para serem executados, basta instalar as dependências.

#### Por que coloquei as referências no início?

Não tenho nenhuma razão especifica, apenas que considero todos esses trabalhos de extrema importância para a criação desse tutorial.

#### Prévia

```python
from frasko import Frasko, Request, Response

app = Frasko()

@app.route("/home")
def index(request: 'Request', response: 'Response') -> None:
    response.text = "um OLAR do index (GET)!"

@app.route("/user", method="post")
def sobre(request: 'Request', response: 'Response') -> None:
    response.text = "um OLAR do sobre (POST)!"

@app.route("/olar/{vezes:d}")
def olar_x_vezes(
    request: 'Request',
    response: 'Response',
    vezes: int,
) -> None:
    response.text = f"{'OLAR ' * vezes} (GET)"

@app.route("/olar/{nome:w}")
def olar_fulano(
    request: 'Request',
    response: 'Response',
    nome: str,
) -> None:
    response.text = f"OLAR {nome} (GET)"

@app.route("/sobremesas")
class BooksResource:
    def get(self, request: 'Request', response: 'Response') -> None:
        response.text = "um OLAR de sobremesas (GET)!"

    def post(self, request: 'Request', response: 'Response') -> None:
        response.text = "um OLAR de sobremesas (POST)!"

```

[[Link do código](/2022-08-27-python-floripa/conte%C3%BAdo/00-pr%C3%A9via/app.py)]

### Referências

- [How to write a Python web framework (free/blog post version)](https://rahmonov.me/posts/write-python-framework-part-one/) - Jahongir Rahmonov
- [How to write a Python web framework (paid/testdriven.io version)](https://testdriven.io/courses/python-web-framework/) - Jahongir Rahmonov
- [Let's build a web framework! PyCon 2017](https://www.youtube.com/watch?v=7kwnjoAJ2HQ) - Jacob Kaplan Moss
- [Let’s Build A Web Server [Part 2]](https://ruslanspivak.com/lsbaws-part2/) - Ruslan Spivak
- [WGSI Tutorial](link_cinco) - Clodoaldo Pinto Neto
- [EXTRA] [Build Your Own X](https://github.com/codecrafters-io/build-your-own-x) - comunidade/open source

## 01 - Web Server, Web App e WSGI

### Web Server

- Espera pacientemente por uma requisição (`Request`)
- Recebe um request do cliente e envia para o `web_app`/"`PythonApp`"
- Espera pelo processamento da resposta (`Response`)
- Envia a resposta para o cliente de volta
- Exemplos: gunicorn, uwsgi

### Web App

- Recebe a requisição enviada pelo `web server`
- Executa alguns comandos a partir de regras definidas
- Monta a resposta e devolve para o `web server`
- Exemplos: flask, django, bottle

### WSGI

#### Problema

- Quem desenvolvia o app (geralmente) não queria lidar com o server (e vice-versa)
- Incompatibilidade entre app e server limitava bastante as escolhas
- Criar adaptadores entre app e server era complicado e custoso de manter
    - Um dos mais famosos é o [`mod_python`](https://modpython.org/) para Apache

### Solução

- **W**eb **S**erver **G**ateway **I**nterface
- `Não é um servidor, um módulo python, um framework, uma API ou qualquer tipo de software`
- `É uma especificação de comunicação entre o servidor e a aplicação`
- Nada mais é do que uma boa conversa
- Ambos os lados devem aplicar as especificações (`web app` e `web server`)
- `WSGI Server`: deve chamar o objeto *app* com os parametros `environ` (dicionario) e `start_response` (função). (`app(environ, start_response)`)
- `WSGI App`: deve chamar a função `start_response` com o `status_code` e `headers_response` (`start_response(status_code, headers_response, exc_info=None)`) antes de retornar o body para o server.
    - O `exc_info` é uma informação opcional que só será passada caso algum erro/`Exception` aconteça.
- Mais detalhes na [PEP 3333](https://peps.python.org/pep-3333/)

---

![](https://www.fullstackpython.com/img/visuals/wsgi-interface.png)

Imagem do [FullStackPython - WSGI Servers](https://www.fullstackpython.com/wsgi-servers.html)

---

![](https://bs-uploads.toptal.io/blackfish-uploads/uploaded_file/file/192775/image-1582505123212-d71812e36fd836399c48a034f9e70128.png)

Imagem do [Toptal/Developers - WSGI: The Server-Application Interface for Python](https://www.fullstackpython.com/wsgi-servers.html)

---

## 02 - Dependências

### webob

- Fornece objetos para requisições (`request`) e respostas (`response`) HTTP.
- São objetos de fácil escrita/leitura
- [webob no pypi](https://pypi.org/project/WebOb/)

### parse

- "`parse()` é o oposto de `format()`"
- Analisa strings a partir de padrões definidos
- [parse no pypi](https://pypi.org/project/parse/)

## 03 - Montando nossos objetos de `Request` e `Response`

Não precisamos nada além de uma função (`Callable`) que receba `environ` e `start_response`.

```python
# app.py
from frasko import frasko

# apenas pra manter o mesmo formato
app = frasko
```

[[Link do código](/2022-08-27-python-floripa/conte%C3%BAdo/01-request-response/01-estrutura-minima-fun%C3%A7%C3%A3o/app.py)]

```python
# frasko.py
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
```

[[Link do código](/2022-08-27-python-floripa/conte%C3%BAdo/01-request-response/01-estrutura-minima-fun%C3%A7%C3%A3o/frasko.py)]

Exemplo de como retorna o `environ`:

```python
sample_environ = {
    'HTTP_ACCEPT': '*/*',
    'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br',
    'HTTP_CONNECTION': 'close',
    'HTTP_HOST': '127.0.0.1:8000',
    'HTTP_USER_AGENT': 'Thunder Client (https://www.thunderclient.com)',
    'PATH_INFO': '/',
    'QUERY_STRING': '',
    'RAW_URI': '/',
    'REMOTE_ADDR': '127.0.0.1',
    'REMOTE_PORT': '59398',
    'REQUEST_METHOD': 'GET',
    'SCRIPT_NAME': '',
    'SERVER_NAME': '127.0.0.1',
    'SERVER_PORT': '8000',
    'SERVER_PROTOCOL': 'HTTP/1.1',
    'SERVER_SOFTWARE': 'gunicorn/20.0.4',
    'gunicorn.socket': <socket.socket fd=9, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8000), raddr=('127.0.0.1', 59398)>, # object
    'wsgi.errors': <gunicorn.http.wsgi.WSGIErrorsWrapper object at 0x10e0369b0>, # object
    'wsgi.file_wrapper': <class 'gunicorn.http.wsgi.FileWrapper'>, # object
    'wsgi.input': <gunicorn.http.body.Body object at 0x10e301960>, # object
    'wsgi.input_terminated': True,
    'wsgi.multiprocess': False,
    'wsgi.multithread': False,
    'wsgi.run_once': False,
    'wsgi.url_scheme': 'http',
    'wsgi.version': (1, 0)
}
```

### Melhorando nossa interface

Agora temos uma classe que pode ser chamada (responsabilidade do `__call__`), essa vai ser a cara do nosso framework.

```python
# app.py
from frasko import Frasko

app = Frasko()
```

[[Link do código](/2022-08-27-python-floripa/conte%C3%BAdo/01-request-response/02-estrutura-minima-classe/app.py)]

```python
# frasko.py
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
```

[[Link do código](/2022-08-27-python-floripa/conte%C3%BAdo/01-request-response/02-estrutura-minima-classe/frasko.py)]

## 04 - Roteamento simples, parametrizado e rota padrão (404)

Agora vamos poder definir os caminhos das rotas que desejarmos, porém sem definir os verbos/métodos por enquanto.

```python
# app.py
from frasko import Frasko, Request, Response

app = Frasko()

@app.route("/")
def barra(request: 'Request', response: 'Response') -> None:
    response.text = "passo 02 - BARRA"


@app.route("/menu")
def menu(request: 'Request', response: 'Response') -> None:
    response.text = "passo 02 - MENU"
```

[[Link do código](/2022-08-27-python-floripa/conte%C3%BAdo/02-roteamento-simples-parametrizado-404/01-rotas-simples-sem-metodos/app.py)]

```python
# frasko.py
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
```

[[Link do código](/2022-08-27-python-floripa/conte%C3%BAdo/02-roteamento-simples-parametrizado-404/01-rotas-simples-sem-metodos/frasko.py)]

### Definindo rotas com verbos/métodos (explícitos)

```python
# app.py
from frasko import Frasko, Request, Response

app = Frasko()

@app.route("/", method="get")
def get_barra(request: 'Request', response: 'Response') -> None:
    response.text = "passo 03 - BARRA GET"


@app.route("/", method="post")
def post_barra(request: 'Request', response: 'Response') -> None:
    response.text = "passo 03 - BARRA POST"
```

[[Link do código](/2022-08-27-python-floripa/conte%C3%BAdo/02-roteamento-simples-parametrizado-404/02-rotas-simples-com-metodos/app.py)]

```python
# frasko.py
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
    
    def _handle_request(self, request: 'Request') -> 'Response':
        response = Response()
        routes = self._routes.get(request.method.lower(), {})
        for path, handler in routes.items():
            if path == request.path:
                handler(request, response)
                return response

        return response
```

[[Link do código](/2022-08-27-python-floripa/conte%C3%BAdo/02-roteamento-simples-parametrizado-404/02-rotas-simples-com-metodos/frasko.py)]

### Parametrizando as rotas

```python
# app.py
from frasko import Frasko, Request, Response

app = Frasko()

@app.route("/olar/{vezes:d}")
def olar_x_vezes(request: 'Request', response: 'Response', vezes: int) -> None:
    response.text = f"passo 05 - GET {'OLAR ' * vezes}"

@app.route("/olar/{nome:w}")
def olar_fulano(request: 'Request', response: 'Response', nome: str) -> None:
    response.text = f"passo 05 - OLAR {nome} GET"
```

[[Link do código](/2022-08-27-python-floripa/conte%C3%BAdo/02-roteamento-simples-parametrizado-404/04-rotas-parametrizadas/app.py)]

```python
# frasko.py
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
```

[[Link do código](/2022-08-27-python-floripa/conte%C3%BAdo/02-roteamento-simples-parametrizado-404/04-rotas-parametrizadas/frasko.py)]

## 05 - Decorando classes e lidando com rotas duplicadas

```python
# app.py
from frasko import Frasko, Request, Response

app = Frasko()

@app.route("/book")
class BooksResource:
    def get(self, request: 'Request', response: 'Response'):
        response.text = "passo 06 - BOOK GET"

    def post(self, request: 'Request', response: 'Response'):
        response.text = "passo 06 - BOOK POST"
```

[[Link do código](/2022-08-27-python-floripa/conte%C3%BAdo/03-decorando-classes-e-rotas-duplicadas/02-rotas-duplicadas/app.py)]

```python
# frasko.py
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
```

[[Link do código](/2022-08-27-python-floripa/conte%C3%BAdo/03-decorando-classes-e-rotas-duplicadas/02-rotas-duplicadas/frasko.py)]
