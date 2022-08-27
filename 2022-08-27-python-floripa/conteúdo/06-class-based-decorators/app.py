from webob import Request, Response
from .frasko import Frasko

app = Frasko()


@app.route("/")
def home(request: 'Request', response: 'Response') -> None:
    response.text = "passo 06 - BARRA"


@app.route("/olar/{nome:w}")
def olar_fulano(request: 'Request', response: 'Response', nome: str) -> None:
    response.text = f"passo 06 - OLAR {nome}"


@app.route("/book")
class BooksResource:
    def get(self, request: 'Request', response: 'Response'):
        response.text = "passo 06 - BOOK GET"

    def post(self, request: 'Request', response: 'Response'):
        response.text = "passo 06 - BOOK POST"

# gunicorn conteúdo.06.app:app
