"""Main application file"""
from flask import Flask, request
app = Flask(__name__)

@app.route('/outraRota')
def outra_rota():
    return 'Rota Funcionando'

@app.route('/bhaskara', methods=['POST'])
def rota_bhaskara():
    a = request.json.get('a')
    b = request.json.get('b')
    c = request.json.get('c')
    return bhaskara(a, b, c)


def bhaskara(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    x1 = divisao((-b + (((b ** 2) - (multiplicacao(multiplicacao(4, a), c))) ** (1/2))), (2 * a))
    x2 = divisao((-b - (((b ** 2) - (multiplicacao(multiplicacao(4, a), c))) ** (1/2))), (2 * a))
    return (str([x1, x2]))

def multiplicacao(a, b):
    return float(a) * float(b)

def divisao(a, b):
    return float(a) / float(b)

def soma(a, b):
    return float(a) + float(b)

@app.route('/')
def index():
    """Test http connection"""
    return "App Funcionando"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)