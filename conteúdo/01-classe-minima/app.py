from .frasko import Frasko


# agora temos uma classe que pode ser chamada (__call__/callable)
# essa vai ser a cara do nosso framework
app = Frasko()

# gunicorn conteúdo.01.app:app
