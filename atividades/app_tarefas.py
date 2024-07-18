import json

from flask import Flask, jsonify, request

app = Flask(__name__)

tarefas = [
    {
        'id': 0,
        'responsavel': 'Vitor',
        'tarefa': 'Fazer a atividade',
        'status': 'Não Realizada'
    }
]


@app.route('/')
def home():
    return jsonify(tarefas)


@app.route('/tarefa/', methods=['POST'])
def adicionar_tarefas():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(tarefas)
        dados['id'] = posicao

        tarefas.append(dados)

        return jsonify(tarefas[posicao])

@app.route('/tarefa/<int:id>/', methods=['PUT', 'GET', 'DELETE'])
def atualiza_tarefa(id):
    if request.method == 'PUT':
        status_tarefa = tarefas[id]['status']

        if status_tarefa == 'Realizada':
            tarefas[id]['status'] = 'Não Realizada'
        else:
            tarefas[id]['status'] = 'Realizada'

        return jsonify(tarefas[id])

    elif request.method == 'GET':
        try:
            response = tarefas[id]
        except IndexError:
            mensagem = f'Tarefa de ID {id} não encontrada'
            response = {'status': 'error', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'error', 'mensagem': mensagem}
        return jsonify(response)

    elif request.method == 'DELETE':
            tarefas.pop(id)
            return json({'status': 'sucesso', 'mensagem': 'Registro excluído'})

if __name__ == '__main__':
    app.run(port=1001, debug=True)