from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

BANCO = "inventario_jogos.db"

def executar_query(query, *args, fetch=False, commit=False):
    conn = sqlite3.connect(BANCO)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    resultado = None

    try:
        cursor.execute(query, args)

        if commit:
            conn.commit()

        if fetch:
            resultado = cursor.fetchall()

    finally:
        conn.close()

    return resultado

@app.route("/")
def inicio():
    return jsonify({"mensagem": "API de inventario de jogos funcionando!"}), 200

@app.route("/jogos", methods=["GET"])
@app.route("/jogos/<int:id>", methods=["GET"])
def listar_ou_buscar_jogo(id=None):
    if id is not None:
        jogo = executar_query(
            "SELECT * FROM jogos WHERE id = ?",
            id,
            fetch=True
        )

        if jogo:
            return jsonify(dict(jogo[0])), 200

        return jsonify({"erro": "Jogo nao encontrado"}), 404

    jogos = executar_query(
        "SELECT * FROM jogos",
        fetch=True
    )

    lista_jogos = [dict(jogo) for jogo in jogos]
    return jsonify(lista_jogos), 200

@app.route("/jogos", methods=["POST"])
def criar_jogo():
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "JSON invalido ou nao enviado"}), 400

    campos_obrigatorios = ["titulo", "genero", "plataforma", "ano_lancamento", "quantidade"]
    for campo in campos_obrigatorios:
        if campo not in dados:
            return jsonify({"erro": f"Campo obrigatorio ausente: {campo}"}), 400

    executar_query(
        """
        INSERT INTO jogos (titulo, genero, plataforma, ano_lancamento, quantidade)
        VALUES (?, ?, ?, ?, ?)
        """,
        dados["titulo"],
        dados["genero"],
        dados["plataforma"],
        dados["ano_lancamento"],
        dados["quantidade"],
        commit=True
    )

    return jsonify({"mensagem": "Jogo cadastrado com sucesso!"}), 201

@app.route("/jogos/<int:id>", methods=["PUT"])
def atualizar_jogo(id):
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "JSON invalido ou nao enviado"}), 400

    jogo = executar_query(
        "SELECT * FROM jogos WHERE id = ?",
        id,
        fetch=True
    )

    if not jogo:
        return jsonify({"erro": "Jogo nao encontrado"}), 404

    campos_obrigatorios = ["titulo", "genero", "plataforma", "ano_lancamento", "quantidade"]
    for campo in campos_obrigatorios:
        if campo not in dados:
            return jsonify({"erro": f"Campo obrigatorio ausente: {campo}"}), 400

    executar_query(
        """
        UPDATE jogos
        SET titulo = ?, genero = ?, plataforma = ?, ano_lancamento = ?, quantidade = ?
        WHERE id = ?
        """,
        dados["titulo"],
        dados["genero"],
        dados["plataforma"],
        dados["ano_lancamento"],
        dados["quantidade"],
        id,
        commit=True
    )

    return "", 204

@app.route("/jogos/<int:id>", methods=["DELETE"])
def deletar_jogo(id):
    jogo = executar_query(
        "SELECT * FROM jogos WHERE id = ?",
        id,
        fetch=True
    )

    if not jogo:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    executar_query(
        "DELETE FROM jogos WHERE id = ?",
        id,
        commit=True
    )

    return "", 204

if __name__ == "__main__":
    app.run(debug=True)