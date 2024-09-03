from flask import Flask, jsonify, request

app = Flask(__name__)
postagens = [
    {
        'titulo': 'Minha História',
        'autor': 'Amanda Dias'
    },
    {
        'titulo': 'Novoo Dispositivo Sony',
        'autor': 'Howard Stringer'
    },
    {
        'titulo': 'Lançamento do Ano',
        'autor': 'Jeff Bezos'
    }
]
# Rota Padrão - GET http://localhost:8000
@app.route('/')
def obter_postagens():
    return jsonify(postagens)

# Obter postagem por id - GET http://localhost:8000/postagem/1
@app.route('/postagem/<int:indice>', methods=['GET'])
def obter_postagem_por_indice(indice):
    return jsonify(postagens[indice])

# Criar uma nova postagem - POST http://localhost:8000/postagem
@app.route('/postagem', methods=['POST'])
def nova_postagem():
    postagem = request.get_json()
    postagens.append(postagem)
    
    return jsonify(postagem, 200)

# Alterar uma postagem existente - PUT http://localhost:8000/postagem/0
@app.route('/postagem/<int:indice>',methods=['PUT'])
def alterar_postagem(indice):
    postagem_alterada = request.get_json()
    postagens[indice].update(postagem_alterada)
    
    return jsonify(postagens[indice], 200)

# Excluir uma postagem - DELETE http://localhost:8000/postagem/1
@app.route('/postagem/<int:indice>', methods=['DELETE'])
def excluir_postagem(indice):
    try:
        if postagens[indice] is not None:
            del postagens[indice]
            return jsonify(f'Foi excluido a postagem {postagens[indice]}', 200)
    except:
        return jsonify(f'Não foi possível encontrar a postagem para exclusão', 404)


app.run(port=8000, host='localhost', debug=True)