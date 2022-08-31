from wsgiref.simple_server import make_server
from frasko import Frasko, Request, Response

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

if __name__ == "__main__":
    server = make_server('localhost', 8031, app=app)
    server.serve_forever()
