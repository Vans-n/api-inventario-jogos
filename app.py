# Importando o Flask
from flask import Flask, jsonify, request

# alteração / usando o Flask-SQLAlchemy no lugar do sqlite3
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# alterando a configuração da conexão com o banco SQLite usando SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///inventario_jogos.db"

# Desativa aviso desnecessário do SQLAlchemy
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# ALTERAÇÃO: Criando o objeto db, que será responsável por gerenciar o banco
db = SQLAlchemy(app)


# ALTERAÇÃO: aqui cria uma classe modelo para representar a tabela jogos, em vez de escrever SQL diretamente nas rotas, usamos essa classe
class Jogo(db.Model):
    __tablename__ = "jogos"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(200), nullable=False)
    genero = db.Column(db.String(100), nullable=False)
    plataforma = db.Column(db.String(100), nullable=False)
    ano_lancamento = db.Column(db.Integer, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)

    # ALTERAÇÃO:Método auxiliar para transformar o objeto em dicionário JSON
    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "genero": self.genero,
            "plataforma": self.plataforma,
            "ano_lancamento": self.ano_lancamento,
            "quantidade": self.quantidade
        }

@app.route("/")
def inicio():
    return jsonify({"mensagem": "API de inventario de jogos funcionando!"}), 200


# Rota GET para listar todos os jogos ou buscar por id
@app.route("/jogos", methods=["GET"])
@app.route("/jogos/<int:id>", methods=["GET"])
def listar_ou_buscar_jogo(id=None):

    # ALTERAÇÃO: Usando o model Jogo para buscar no banco
    if id is not None:
        jogo = Jogo.query.get(id)

        if jogo:
            return jsonify(jogo.to_dict()), 200

        return jsonify({"erro": "Jogo nao encontrado"}), 404

    jogos = Jogo.query.all()

    lista_jogos = [jogo.to_dict() for jogo in jogos]

    return jsonify(lista_jogos), 200


# Rota POST para cadastrar um novo jogo
@app.route("/jogos", methods=["POST"])
def criar_jogo():

    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "JSON invalido ou nao enviado"}), 400

    campos_obrigatorios = ["titulo", "genero", "plataforma", "ano_lancamento", "quantidade"]

    for campo in campos_obrigatorios:
        if campo not in dados:
            return jsonify({"erro": f"Campo obrigatorio ausente: {campo}"}), 400

    # ALTERAÇÃO: criando um objeto da classe Jogo em vez de usar INSERT SQL
    novo_jogo = Jogo(
        titulo=dados["titulo"],
        genero=dados["genero"],
        plataforma=dados["plataforma"],
        ano_lancamento=dados["ano_lancamento"],
        quantidade=dados["quantidade"]
    )

    # ALTERAÇÃO:Adiciona e salva no banco usando SQLAlchemy
    db.session.add(novo_jogo)
    db.session.commit()

    return jsonify({"mensagem": "Jogo cadastrado com sucesso!"}), 201


@app.route("/jogos/<int:id>", methods=["PUT"])
def atualizar_jogo(id):

    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "JSON invalido ou nao enviado"}), 400

    # ALTERAÇÃO: Busca o jogo pelo id usando SQLAlchemy
    jogo = Jogo.query.get(id)

    if not jogo:
        return jsonify({"erro": "Jogo nao encontrado"}), 404

    campos_obrigatorios = ["titulo", "genero", "plataforma", "ano_lancamento", "quantidade"]

    for campo in campos_obrigatorios:
        if campo not in dados:
            return jsonify({"erro": f"Campo obrigatorio ausente: {campo}"}), 400

    # ALTERAÇÃO: Atualizando os atributos do objeto
    jogo.titulo = dados["titulo"]
    jogo.genero = dados["genero"]
    jogo.plataforma = dados["plataforma"]
    jogo.ano_lancamento = dados["ano_lancamento"]
    jogo.quantidade = dados["quantidade"]

    # ALTERAÇÃO: Salva as alterações no banco
    db.session.commit()

    return "", 204


# Rota DELETE para remover um jogo
@app.route("/jogos/<int:id>", methods=["DELETE"])
def deletar_jogo(id):

    # ALTERAÇÃO:Busca o jogo pelo id usando SQLAlchemy
    jogo = Jogo.query.get(id)

    if not jogo:
        return jsonify({"erro": "Jogo nao encontrado"}), 404

    # ALTERAÇÃO: Remove o objeto e salva a alteração no banco
    db.session.delete(jogo)
    db.session.commit()

    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
