from flask import Flask, jsonify, request

app = Flask(__name__)
cancoes = [
    {
        'cancao': 'Adventure Time',
        'estilo': 'Infantil'
        
    },
    {
        'cancao': 'Numb',
        'estilo': 'Rock'
    },
    {
        'cancao': 'Bring me to life',
        'estilo': 'Rock'
    },
    {
        'cancao': 'Pode ficar',
        'estilo': 'Poesia'
    },
    {
        'cancao': 'Te liguei',
        'estilo': 'Poesia'
    }
]

#Consulta Padrão - GET
@app.route('/')
def obter_cancoes():
    return jsonify(cancoes)

#Consulta por ID - GET
@app.route('/cancoes/<int:indice>',methods=['GET'])
def obter_cancoes_id(indice):
    return jsonify(cancoes[indice])

#Adicionar musicas - POST
@app.route('/cancoes',methods=['POST'])
def adicionar_cancoes():
    musicas = request.get_json()
    cancoes.append(musicas)
    return jsonify(musicas, 200)

#Alterar Musicas - PUT
@app.route('/cancoes/<int:indice>', methods=['PUT'])
def alterar_cancoes(indice):
    cancao_alterada = request.get_json()
    cancoes[indice].update(cancao_alterada)
    
    return jsonify(cancoes[indice], 200)

#Excluir Musicas - DELETE
@app.route('/cancoes/<int:indice>',methods=['DELETE'])
def delete_cancoes(indice):
    try:
        if cancoes[indice] is not None:
            del cancoes[indice]
            return jsonify(f'Foi excluida a música{cancoes[indice]}', 200)
    except:
        return jsonify(f'Não foi possível excluir', 404)
    



app.run(port=5000, host='localhost', debug=True)