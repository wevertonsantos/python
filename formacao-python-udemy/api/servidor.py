from flask import jsonify, Flask
from pyngrok import ngrok

app = Flask(__name__) # criando aplicação flask

# Abre o túnel ngrok na porta 5000
public_url = ngrok.connect(5000)
print(f"* ngrok tunnel: {public_url}")  # Mostra a URL pública no terminal

@app.route('/')
def padrao():
    return "Escolha um dos métodos"

@app.route('/cotacao/') # rota para acessar o endereço e executar função
def cotacao():
    return '5.34'

app.run() #executando aplicação