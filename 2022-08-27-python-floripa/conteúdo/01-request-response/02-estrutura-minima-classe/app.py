from wsgiref.simple_server import make_server
from frasko import Frasko

# agora temos uma classe que pode ser chamada (__call__/callable)
# essa vai ser a cara do nosso framework
app = Frasko()

if __name__ == "__main__":
    server = make_server('localhost', 8012, app=app)
    server.serve_forever()
