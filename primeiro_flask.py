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
    

    alunos.append(entrada_dados)

    response = "Aluno cadastrado com sucesso!"
    return response, 201


@app.route('/lista_alunos', methods=['GET'])
def lista_alunos():
    return alunos, 200

@app.route('/aluno_id', methods=['POST'])
def achar_aluno():
    entrada_dados = request.json

    for aluno in alunos:
        if aluno["id"] == entrada_dados:
            especifico_aluno = aluno
    return especifico_aluno, 200



disciplinas = []
@app.route('/cadastrar_disciplinas', methods=['POST'])
def cadastrar_disciplinas():

    entrada_dados = request.json
    

    disciplinas.append(entrada_dados)

    response = "Disciplina cadastrada com sucesso!"
    return response, 201

@app.route('/lista_disciplinas', methods=['GET'])
def lista_disciplinas():
    return disciplinas, 200

@app.route('/disciplina_id', methods=['POST'])
def achar_disciplina():
    entrada_dados = request.json

    for disciplina in disciplinas:
        if disciplina["id"] == entrada_dados:
            especifica_disciplina = disciplina
    return especifica_disciplina, 200



matriculas = []
@app.route('/cadastrar_matriculas', methods=['POST'])
def cadastrar_matriculas():

    entrada_dados = request.json
    

    matriculas.append(entrada_dados)

    response = "Matricula cadastrada com sucesso!"
    return response, 201

@app.route('/matricula_id', methods=['POST'])
def matricula_id():
    entrada_dados = request.json

    for matricula in matriculas:
        if matricula["id"] == entrada_dados:
            disciplina_id = matricula["disciplina"]
    return disciplina_id, 200

#web_pdb.set_trace()

if __name__ == '__main__':
    app.run(debug=True)