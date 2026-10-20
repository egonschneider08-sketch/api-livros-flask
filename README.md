# 📚 API de Livros (Flask REST API)

Uma API REST simples e eficiente desenvolvida em Python com o framework Flask para gerenciamento de um acervo de livros. A API oferece operações de consulta, cadastro e exclusão de itens com validação de dados e tratamento de erros.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Flask**: Framework web para criação dos endpoints REST.
- **Git & GitHub**: Versionamento de código.

---

## 🚀 Como Executar o Projeto Localmente

### 1. Clonar o Repositório
```bash
git clone https://github.com/egonschneider08-sketch/api-livros.git
cd api-livros
```

### 2. Criar e Ativar o Ambiente Virtual

- **No Windows (PowerShell):**
  ```powershell
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  ```

- **No Linux/macOS:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### 3. Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 4. Iniciar o Servidor Flask
```bash
python app.py
```
O servidor iniciará por padrão em: **`http://localhost:5000`** (ou `http://127.0.0.1:5000`).

---

## 📌 Rotas e Endpoints da API

A URL base da aplicação é `http://localhost:5000`.

| Método | Endpoint | Descrição | Status Sucesso | Status Erro |
| :--- | :--- | :--- | :--- | :--- |
| **GET** | `/livros` | Lista todos os livros cadastrados | `200 OK` | - |
| **GET** | `/livros/<id>` | Busca um livro específico pelo seu ID | `200 OK` | `404 Not Found` |
| **POST** | `/livros` | Cadastra um novo livro na coleção | `201 Created` | `400 Bad Request` |
| **DELETE** | `/livros/<id>` | Remove um livro específico pelo seu ID | `200 OK` | `404 Not Found` |

---

## 🧪 Como Testar no Postman (Passo a Passo)

Abra o **Postman** e siga os passos abaixo para testar cada funcionalidade da API:

---

### 1. Obter Todos os Livros (`GET /livros`)

Retorna a lista completa com todos os livros disponíveis no acervo.

- **Método**: `GET`
- **URL**: `http://localhost:5000/livros`
- **Headers**: Nenhum obrigatório
- **Body**: Nenhum

#### Exemplo de Resposta (`200 OK`):
```json
[
  {
    "id": 1,
    "titulo": "Harry Potter e a Pedra Filosofal",
    "autor": "J.K. Rowling",
    "preco": 19.9
  },
  {
    "id": 2,
    "titulo": "O Senhor dos Anéis",
    "autor": "J.R.R. Tolkien",
    "preco": 25.9
  }
]
```

---

### 2. Obter Livro por ID (`GET /livros/<id>`)

Busca e retorna apenas o livro correspondente ao ID informado na URL.

- **Método**: `GET`
- **URL**: `http://localhost:5000/livros/1`
- **Headers**: Nenhum obrigatório
- **Body**: Nenhum

#### Exemplo de Resposta de Sucesso (`200 OK`):
```json
{
  "id": 1,
  "titulo": "Harry Potter e a Pedra Filosofal",
  "autor": "J.K. Rowling",
  "preco": 19.9
}
```

#### Exemplo de Resposta se não existir (`404 Not Found`):
```json
{
  "message": "Livro não encontrado"
}
```

---

### 3. Cadastrar Novo Livro (`POST /livros`)

Cria um novo livro. O ID é gerado e incrementado automaticamente pela aplicação.

- **Método**: `POST`
- **URL**: `http://localhost:5000/livros`
- **Headers**:
  - `Content-Type`: `application/json`
- **Body**:
  - Selecione a aba **Body**
  - Escolha a opção **raw**
  - Selecione o formato **JSON**

#### Exemplo de Envio no Body:
```json
{
  "titulo": "Clean Code",
  "autor": "Robert C. Martin",
  "preco": 85.50
}
```

#### Exemplo de Resposta (`201 Created`):
```json
{
  "id": 11,
  "titulo": "Clean Code",
  "autor": "Robert C. Martin",
  "preco": 85.50
}
```

#### Validações automáticas da rota:
- O corpo deve ser um JSON válido.
- O campo `titulo` é obrigatório e deve ser uma string não vazia.
- O campo `autor` é obrigatório e deve ser uma string não vazia.
- O campo `preco` é obrigatório e deve ser um número maior ou igual a zero.
- Caso algum campo seja inválido, a API retornará `400 Bad Request` com a mensagem descritiva do erro.

---

### 4. Excluir um Livro (`DELETE /livros/<id>`)

Remove um livro existente pelo seu ID utilizando o método `.pop()`, retornando os dados do item removido.

- **Método**: `DELETE`
- **URL**: `http://localhost:5000/livros/1`
- **Headers**: Nenhum obrigatório
- **Body**: Nenhum

#### Exemplo de Resposta de Sucesso (`200 OK`):
```json
{
  "livro_removido": {
    "autor": "J.K. Rowling",
    "id": 1,
    "preco": 19.9,
    "titulo": "Harry Potter e a Pedra Filosofal"
  },
  "message": "Livro excluído com sucesso"
}
```

#### Exemplo de Resposta se o ID não existir (`404 Not Found`):
```json
{
  "message": "Livro não encontrado"
}
```

---

## 💡 Detalhes de Implementação: `.pop()` vs `del`

No arquivo `app.py`, foram implementadas e demonstradas duas abordagens para remoção em listas Python:

1. **`livros.pop(indice)` (Utilizado na rota DELETE)**:
   - Remove o item pelo seu índice na lista e **retorna o item removido**.
   - Permite que a API devolva exatamente qual livro foi excluído na resposta JSON.
2. **`del livros[indice]`**:
   - Deleta a referência do item na lista sem retornar o seu valor.

---

## 📄 Licença

Este projeto é de cunho educacional e está sob a licença MIT.
