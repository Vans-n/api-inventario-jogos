#  API de Inventário de Jogos

## **Introdução**

Este projeto foi desenvolvido com o objetivo de criar uma API para gerenciamento de um inventário de jogos, utilizando Python, Flask e SQLite.

A ideia é simular um sistema simples onde é possível cadastrar, visualizar, atualizar e excluir jogos, como se fosse um controle de estoque ou até uma coleção pessoal.

---

## **Objetivo**

O principal objetivo deste projeto é colocar em prática os conceitos aprendidos em desenvolvimento backend, como:

- Criação de rotas com Flask  
- Uso dos métodos HTTP (GET, POST, PUT, DELETE)  
- Manipulação de dados em JSON  
- Integração com banco de dados SQLite  

Além disso, o projeto também busca aplicar boas práticas, como organização do código e tratamento de erros.

---

## **Funcionalidades**

A API permite realizar as seguintes operações:

- 📋 Listar todos os jogos cadastrados  
- 🔍 Buscar um jogo específico pelo ID  
- ➕ Cadastrar novos jogos  
- ✏️ Atualizar informações de um jogo  
- ❌ Remover jogos do inventário  

---

##  **Tecnologias Utilizadas**

- Python  
- Flask  
- SQLite  
- JSON  

---

## **Estrutura do Projeto**

```bash
inventario-jogos/
├── app.py
├── init_db.py
├── inventario_jogos.db
└── README.md

Como Executar o Projeto
1. Instalar o Flask
pip install flask
2. Criar o banco de dados
python init_db.py
3. Rodar a aplicação
python app.py
4. Acessar no navegador
http://127.0.0.1:5000/jogos

Endpoints da API
Método	Rota	Descrição
GET	/jogos	Lista todos os jogos
GET	/jogos/{id}	Busca jogo por ID
POST	/jogos	Cadastra novo jogo
PUT	/jogos/{id}	Atualiza jogo existente
DELETE	/jogos/{id}	Remove jogo

Testes com cURL
➤ Inserir jogo
curl -X POST http://127.0.0.1:5000/jogos -H "Content-Type: application/json" -d "{\"titulo\":\"The Last of Us\",\"genero\":\"Ação\",\"plataforma\":\"PS5\",\"ano_lancamento\":2020,\"quantidade\":2}"
➤ Listar jogos
curl http://127.0.0.1:5000/jogos
➤ Buscar por ID
curl http://127.0.0.1:5000/jogos/1
➤ Atualizar jogo
curl -X PUT http://127.0.0.1:5000/jogos/1 -H "Content-Type: application/json" -d "{\"titulo\":\"The Last of Us\",\"genero\":\"Ação e Aventura\",\"plataforma\":\"PS5\",\"ano_lancamento\":2020,\"quantidade\":5}"
➤ Deletar jogo
curl -X DELETE http://127.0.0.1:5000/jogos/1

Códigos de Status
200 → Sucesso
201 → Criado com sucesso
204 → Sucesso sem retorno
400 → Erro na requisição
404 → Não encontrado

Exemplo de JSON
{
  "titulo": "The Last of Us",
  "genero": "Ação",
  "plataforma": "PS5",
  "ano_lancamento": 2020,
  "quantidade": 2
}
```

**Conclusão**

Com esse projeto, foi possível entender melhor como funciona uma API na prática, desde a criação das rotas até a comunicação com o banco de dados.

Também ajudou a reforçar o uso dos métodos HTTP e a importância de organizar bem o código. Mesmo sendo um projeto simples, ele representa bem como funciona um sistema real de backend.
