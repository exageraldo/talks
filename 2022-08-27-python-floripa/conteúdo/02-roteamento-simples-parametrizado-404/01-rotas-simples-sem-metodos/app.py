from wsgiref.simple_server import make_server
from frasko import Frasko, Request, Response

app = Frasko()

@app.route("/")
def barra(request: 'Request', response: 'Response') -> None:
    response.text = "passo 02 - BARRA"

@app.route("/menu")
def menu(request: 'Request', response: 'Response') -> None:
    response.text = "passo 02 - MENU"

if __name__ == "__main__":
    server = make_server('localhost', 8021, app=app)
    server.serve_forever()
