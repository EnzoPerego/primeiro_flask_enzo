from flask import Flask, request
import web_pdb


app = Flask(__name__)


@app.route('/', methods=['GET'])
def site():
    return "Hello World!", 200


@app.route('/teste', methods=['GET'])
def teste():
    return "Webs Service Funcionando", 200


alunos = []
@app.route('/cadastro_aluno', methods=['POST'])
def cadastro_aluno():

    entrada_dados = request.json

    web_pdb.set_trace()

    alunos.append(entrada_dados)

    response = "Aluno cadastrado com sucesso!"
    return response, 201


@app.route('/lista_alunos', methods=['GET'])
def lista_alunos():
    return alunos, 200


if __name__ == '__main__':
    app.run(debug=True)