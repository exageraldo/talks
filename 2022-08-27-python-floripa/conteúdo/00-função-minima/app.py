from .frasko import frasko


# não precisamos nada alem de uma função (callable)
# que receba environ e start_response
app = frasko # apenas pra manter o mesmo formato

# gunicorn conteúdo.00.app:app
