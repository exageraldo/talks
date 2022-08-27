from webob import Request, Response
from .frasko import Frasko


app = Frasko()

@app.route("/")
def barra(request: 'Request', response: 'Response') -> None:
    response.text = "passo 02 - BARRA"


@app.route("/menu")
def menu(request: 'Request', response: 'Response') -> None:
    response.text = "passo 02 - MENU"

# gunicorn conteúdo.02.app:app
