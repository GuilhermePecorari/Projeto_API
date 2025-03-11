from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def exemplo():
    dados = {'mensagem': 'Bem-vindo a minha API Flask'}
    return jsonify(dados)

if __name__ == '__main__':
    app.run(debug=True)
