from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Função para carregar os dados dos personagens do arquivo personagens.json
def carregar_personagens():
    with open('personagens.json', 'r') as file:
        return json.load(file)

# Carregar os personagens ao iniciar a aplicação
personagens = carregar_personagens()

# Rota para listar todos os personagens ou criar um novo personagem
@app.route('/personagens', methods=['GET', 'POST'])
def manipular_personagens():
    if request.method == 'GET':
        return jsonify(personagens)
    elif request.method == 'POST':
        novo_personagem = request.json
        personagens.append(novo_personagem)
        # Atualizar o arquivo JSON com o novo personagem
        with open('personagens.json', 'w') as file:
            json.dump(personagens, file, indent=4)
        return jsonify({"mensagem": "Personagem criado com sucesso"}), 201

# Rota para visualizar, atualizar ou excluir um personagem específico
@app.route('/personagens/<int:personagem_id>', methods=['GET', 'PUT', 'DELETE'])
def manipular_personagem(personagem_id):
    if request.method == 'GET':
        for personagem in personagens:
            if personagem['id'] == personagem_id:
                return jsonify(personagem)
        return jsonify({"mensagem": "Personagem não encontrado"}), 404
    elif request.method == 'PUT':
        for personagem in personagens:
            if personagem['id'] == personagem_id:
                dados_atualizados = request.json
                personagem.update(dados_atualizados)
                # Atualizar o arquivo JSON com os dados atualizados
                with open('personagens.json', 'w') as file:
                    json.dump(personagens, file, indent=4)
                return jsonify({"mensagem": "Personagem atualizado com sucesso"})
        return jsonify({"mensagem": "Personagem não encontrado"}), 404
    elif request.method == 'DELETE':
        for index, personagem in enumerate(personagens):
            if personagem['id'] == personagem_id:
                del personagens[index]
                # Atualizar o arquivo JSON sem o personagem excluído
                with open('personagens.json', 'w') as file:
                    json.dump(personagens, file, indent=4)
                return jsonify({"mensagem": "Personagem excluído com sucesso"})
        return jsonify({"mensagem": "Personagem não encontrado"}), 404

app.run(port=5000, host='localhost', debug=True)
