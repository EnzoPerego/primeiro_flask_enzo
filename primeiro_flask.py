from flask import Flask


app = Flask(__name__)


@app.route('/', methods=['GET'])
def site():
    return "Hello World!", 200


@app.route('/teste', methods=['GET'])
def teste():
    return "Testando", 200


@app.route('/cadastrar_aluno', methods=['POST'])
def cadastrar_aluno():
    response = "OK!"
    return response, 201


if __name__ == '__main__':
    app.run(debug=True)