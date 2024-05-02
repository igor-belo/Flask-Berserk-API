from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Função para carregar os dados dos personagens do arquivo personagens.json
def carregar_personagens():
    with open('personagens.json', 'r', encoding='utf-8') as file:
        return json.load(file)

# Função para salvar os dados dos personagens no arquivo personagens.json
def salvar_personagens(personagens):
    with open('personagens.json', 'w', encoding='utf-8') as file:
        json.dump(personagens, file, indent=4, ensure_ascii=False)

# Carregar os personagens ao iniciar a aplicação
personagens = carregar_personagens()

# Rota para listar todos os personagens ou criar um novo personagem
@app.route('/personagens', methods=['GET', 'POST'])
def manipular_personagens():
    if request.method == 'GET':
        return jsonify(personagens)
    elif request.method == 'POST':
        novo_personagem = request.json
        if 'id' not in novo_personagem or 'name' not in novo_personagem or 'description' not in novo_personagem:
            return jsonify({"mensagem": "Campos 'id', 'name' e 'description' são obrigatórios"}), 400
        personagens.append(novo_personagem)
        salvar_personagens(personagens)
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
        dados_atualizados = request.json
        for personagem in personagens:
            if personagem['id'] == personagem_id:
                personagem.update(dados_atualizados)
                salvar_personagens(personagens)
                return jsonify({"mensagem": "Personagem atualizado com sucesso"})
        return jsonify({"mensagem": "Personagem não encontrado"}), 404
    elif request.method == 'DELETE':
        for index, personagem in enumerate(personagens):
            if personagem['id'] == personagem_id:
                del personagens[index]
                salvar_personagens(personagens)
                return jsonify({"mensagem": "Personagem excluído com sucesso"})
        return jsonify({"mensagem": "Personagem não encontrado"}), 404

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
