from flask import jsonify, Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__) # criando aplicação flask
run_with_ngrok(app) # rodar ngrok com aplicação flask

@app.route('/cotacao/') # rota para acessar o endereço e executar função
def cotacao():
    return '5.34'

app.run() #executando aplicação