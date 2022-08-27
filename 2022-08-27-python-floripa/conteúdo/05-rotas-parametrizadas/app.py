from webob import Request, Response
from .frasko import Frasko

app = Frasko()


@app.route("/", method="post")
def home(request: 'Request', response: 'Response') -> None:
    response.text = "passo 05 - BARRA POST"


@app.route("/olar/{vezes:d}")
def olar_x_vezes(request: 'Request', response: 'Response', vezes: int) -> None:
    response.text = f"passo 05 - GET {'OLAR ' * vezes}"


@app.route("/olar/{nome:w}")
def olar_fulano(request: 'Request', response: 'Response', nome: str) -> None:
    response.text = f"passo 05 - OLAR {nome} GET"

# gunicorn conteúdo.05.app:app
