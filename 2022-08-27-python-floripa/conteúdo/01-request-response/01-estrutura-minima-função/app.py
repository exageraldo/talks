from wsgiref.simple_server import make_server
from frasko import frasko

# não precisamos nada alem de uma função (callable)
# que receba environ e start_response
app = frasko # apenas pra manter o mesmo formato

if __name__ == "__main__":
    server = make_server('localhost', 8011, app=app)
    server.serve_forever()
