from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://fernandopacheco:ZmVybmFuZG9w@jobs.visie.com.br/fernandopacheco'
db = SQLAlchemy(app)

class Pessoa(db.Model):
    __tablename__ = 'pessoas'
    id_pessoa = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    rg = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(100), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    data_admissao = db.Column(db.Date, nullable=False)
    funcao = db.Column(db.String(100))

@app.route('/pessoas', methods=['POST'])
def criar_pessoa():
    data = request.get_json()
    nova_pessoa = Pessoa(**data)
    db.session.add(nova_pessoa)
    db.session.commit()
    return jsonify({'mensagem': 'Pessoa criada com sucesso'}), 201

@app.route('/pessoas', methods=['GET'])
def listar_pessoas():
    pessoas = Pessoa.query.all()
    pessoas_serializadas = []
    for pessoa in pessoas:
        pessoa_dict = {
            'id_pessoa': pessoa.id_pessoa,
            'nome': pessoa.nome,
            'rg': pessoa.rg,
            'cpf': pessoa.cpf,
            'data_nascimento': pessoa.data_nascimento.strftime('%Y-%m-%d'),
            'data_admissao': pessoa.data_admissao.strftime('%Y-%m-%d'),
            'funcao': pessoa.funcao
        }
        pessoas_serializadas.append(pessoa_dict)
    return jsonify(pessoas_serializadas)

@app.route('/pessoas/<int:id_pessoa>', methods=['GET'])
def obter_pessoa(id_pessoa):
    pessoa = Pessoa.query.get(id_pessoa)
    if pessoa:
        pessoa_dict = {
            'id_pessoa': pessoa.id_pessoa,
            'nome': pessoa.nome,
            'rg': pessoa.rg,
            'cpf': pessoa.cpf,
            'data_nascimento': pessoa.data_nascimento.strftime('%Y-%m-%d'),
            'data_admissao': pessoa.data_admissao.strftime('%Y-%m-%d'),
            'funcao': pessoa.funcao
        }
        return jsonify(pessoa_dict)
    return jsonify({'mensagem': 'Pessoa não encontrada'}), 404

@app.route('/pessoas/<int:id_pessoa>', methods=['PUT'])
def atualizar_pessoa(id_pessoa):
    pessoa = Pessoa.query.get(id_pessoa)
    if not pessoa:
        return jsonify({'mensagem': 'Pessoa não encontrada'}), 404

    data = request.get_json()
    for key, value in data.items():
        setattr(pessoa, key, value)

    db.session.commit()
    return jsonify({'mensagem': 'Pessoa atualizada com sucesso'})

@app.route('/pessoas/<int:id_pessoa>', methods=['DELETE'])
def deletar_pessoa(id_pessoa):
    pessoa = Pessoa.query.get(id_pessoa)
    if not pessoa:
        return jsonify({'mensagem': 'Pessoa não encontrada'}), 404

    db.session.delete(pessoa)
    db.session.commit()
    return jsonify({'mensagem': 'Pessoa excluída com sucesso'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

