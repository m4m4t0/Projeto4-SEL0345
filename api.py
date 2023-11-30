from flask import Flask, request
import json

# funcao encarregada de calcular o fatorial de "numero"
def fatorial(numero):
  if numero == 0:
    return 1
  else:
    return numero * fatorial(numero - 1)

# funcao encarregada de calcular o fibonacci de "numero"
def fibonacci(numero):
  if numero == 0 or numero == 1:
    return numero
  else:
    return fibonacci(numero - 1) + fibonacci(numero - 2)


def app():
  # inicializa o objeto app usando Flask
  app = Flask(__name__)

  
  # endpoint para associal "/fatorial" com a função "fatorial_endpoint()"
  @app.route("/fatorial", methods=["POST"])
  # cria um arquivo .json com a resposta
  def fatorial_endpoint():
    dados = json.loads(request.data)
    numero = dados["numero"]
    resultado = fatorial(numero)
    return json.dumps({"resultado": resultado})

  # endpoint para associal "/fibonacci" com a função "fibonacci_endpoint()"
  @app.route("/fibonacci", methods=["POST"])
  # cria um arquivo .json com a resposta
  def fibonacci_endpoint():
    dados = json.loads(request.data)
    numero = dados["numero"]
    resultado = fibonacci(numero)
    return json.dumps({"resultado": resultado})

  # configuracoes de compilação da api
  if __name__ == "__main__":
    app.run(port=3000, debug=True)

# roda a api
if __name__ == "__main__":
  app()