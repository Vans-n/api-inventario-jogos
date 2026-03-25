# Importando a biblioteca SQLite
import sqlite3


# Criando o banco e a tabela
def criar_banco():

    conn = sqlite3.connect("inventario_jogos.db")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jogos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  
            titulo TEXT NOT NULL,                  
            genero TEXT NOT NULL,                 
            plataforma TEXT NOT NULL,              
            ano_lancamento INTEGER NOT NULL,       
            quantidade INTEGER NOT NULL            
        )
    """)

    cursor.execute("""
    INSERT INTO jogos (titulo, genero, plataforma, ano_lancamento, quantidade)
    VALUES
    ('Harry Potter: Hogwarts Legacy', 'Ação/RPG', 'PC', 2023, 6),
    ('The Sims 4', 'Simulação', 'PC', 2014, 7),
    ('Super Mario Odyssey', 'Aventura', 'Nintendo Switch', 2017, 4)
    """)

    conn.commit()

    conn.close()

    print("Banco de dados, tabela e jogos inseridos com sucesso!")


if __name__ == "__main__":
    criar_banco()
