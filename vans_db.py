# Importando a aplicação e o banco do app
from app import app, db, Jogo


# Função para criar o banco e inserir jogos iniciais
def criar_banco():
    with app.app_context():
        # ALTERAÇÃO: Agora cria as tabelas com SQLAlchemy
        db.create_all()

        # ALTERAÇÃO: Verifica se já existem jogos cadastrados antes de inserir
        if Jogo.query.count() == 0:
            jogos = [
                Jogo(
                    titulo="Harry Potter: Hogwarts Legacy",
                    genero="Ação/RPG",
                    plataforma="PC",
                    ano_lancamento=2023,
                    quantidade=6
                ),
                Jogo(
                    titulo="The Sims 4",
                    genero="Simulação",
                    plataforma="PC",
                    ano_lancamento=2014,
                    quantidade=7
                ),
                Jogo(
                    titulo="Super Mario Odyssey",
                    genero="Aventura",
                    plataforma="Nintendo Switch",
                    ano_lancamento=2017,
                    quantidade=4
                )
            ]

            # ALTERAÇÃO:  Inseri os jogos usando db.session
            db.session.add_all(jogos)
            db.session.commit()

        print("Banco de dados, tabela e jogos inseridos com sucesso!")


if __name__ == "__main__":
    criar_banco()
