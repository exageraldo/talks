from wsgiref.simple_server import make_server
from frasko import Frasko, Request, Response

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

if __name__ == "__main__":
    server = make_server('localhost', 8024, app=app)
    server.serve_forever()

