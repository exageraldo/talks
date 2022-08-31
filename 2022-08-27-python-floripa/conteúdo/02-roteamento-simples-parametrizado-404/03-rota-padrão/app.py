from wsgiref.simple_server import make_server
from frasko import Frasko, Request, Response

app = Frasko()

@app.route("/")
def barra(request: 'Request', response: 'Response') -> None:
    response.text = "passo 04 - BARRA"


@app.route("/menu")
def menu(request: 'Request', response: 'Response') -> None:
    response.text = "passo 04 - MENU"

if __name__ == "__main__":
    server = make_server('localhost', 8023, app=app)
    server.serve_forever()
