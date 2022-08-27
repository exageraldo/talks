from webob import Request, Response
from .frasko import Frasko


app = Frasko()

@app.route("/", method="get")
def get_barra(request: 'Request', response: 'Response') -> None:
    response.text = "passo 03 - BARRA GET"


@app.route("/", method="post")
def post_barra(request: 'Request', response: 'Response') -> None:
    response.text = "passo 03 - BARRA POST"

# gunicorn conteúdo.02.app:app
