from wsgiref.simple_server import make_server
from frasko import Frasko, Request, Response

app = Frasko()

@app.route("/", method="get")
def get_barra(request: 'Request', response: 'Response') -> None:
    response.text = "passo 03 - BARRA GET"

@app.route("/", method="post")
def post_barra(request: 'Request', response: 'Response') -> None:
    response.text = "passo 03 - BARRA POST"

if __name__ == "__main__":
    server = make_server('localhost', 8022, app=app)
    server.serve_forever()
