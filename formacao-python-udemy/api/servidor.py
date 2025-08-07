from flask import jsonify, Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__) # criando aplicação flask
run_with_ngrok(app) # rodar ngrok com aplicação flask

app.run() #executando aplicação