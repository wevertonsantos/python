from flask import jsonify, Flask,request
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

@app.route('/conversao/<float:val>')
def conversao(val):
    return str(val * 5.34)

@app.route('/cotacaocompleta')
def cotacaocompleta():
    argumentos = request.args # pegando argumentos quando passado as rotas
    valor = float(argumentos.get('valor'))
    mes = argumentos.get('mes')

    total = 0.0
    if mes == 'Janeiro':
        total = valor * 5.34
    elif mes == 'Fevereiro':
        total = valor * 5.22
    elif mes == 'Marco':
        total = valor * 5.19

    return str(total)

@app.route('/tabela/')
def tabela():
    return jsonify(Janeiro='5.34',Fevereiro='5.22',Marco='5.33') # transformando parametros em um json

app.run() #executando aplicação