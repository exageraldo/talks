from wsgiref.simple_server import make_server
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


if __name__ == "__main__":
    server = make_server('localhost', 8000, app=app)
    server.serve_forever()