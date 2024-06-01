from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/<int:id>')
def pessoa(id):
    return jsonify({'id': id,'nome': 'vitor', 'profissao': 'desenvolvedor'})

@app.route('/soma', methods=['POST', 'PUT', 'GET'])
def soma():
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['valores'])
        return jsonify({'soma': total})

    elif request.method == 'GET':
        total = 10 + 10
        return jsonify({'soma': total})

    elif request.method == 'PUT':
        return 'Sem dados.'

    return 'Método Incorreto'

if __name__ == '__main__':
    app.run(debug=True)