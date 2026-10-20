from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    { 'id': 1, "titulo": "Harry Potter e a Pedra Filosofal", "autor": "J.K. Rowling", "preco": 19.90 },
    { 'id': 2, "titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien", "preco": 25.90 },
    { 'id': 3, "titulo": "O Hobbit", "autor": "J.R.R. Tolkien", "preco": 15.90 },
    { 'id': 4, 'titulo': 'O Código do Destino', 'autor': 'Ana Silva', 'preco': 46.12 },
    { 'id': 5, 'titulo': 'A Sombra da Ilusão', 'autor': 'Fernanda Oliveira', 'preco': 26.89 },
    { 'id': 6, 'titulo': 'A Herança do Destino', 'autor': 'Lucas Gomes', 'preco': 18.47 },
    { 'id': 7, 'titulo': 'O Último de Gelo', 'autor': 'Rodrigo Martins', 'preco': 61.74 },
    { 'id': 8, 'titulo': 'A Herança da Alvorada', 'autor': 'Vanessa Oliveira', 'preco': 45.17 },
    { 'id': 9, 'titulo': 'O Código do Rei', 'autor': 'Pedro Alves', 'preco': 60.02 },
    { 'id': 10, 'titulo': 'O Vento das Estrelas', 'autor': 'Carlos Machado', 'preco': 23.33 },
]

# Rota para obter todos os livros
@app.route('/livros', methods=['GET'])
def obter_todos_os_livros():
    return jsonify(livros)

# FUNÇÃO AUXILIAR CORRIGIDA: Retorna o dicionário ou None (sem jsonify aqui)
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return livro  # Retorna o dicionário diretamente
    return None

# Rota para obter um livro por ID com tratamento de erro
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro(id):
    livro = obter_livro_por_id(id)
    
    if livro:
        return jsonify(livro)
    
    # Se o livro for None, retorna o erro 404
    return jsonify({'message': 'Livro não encontrado'}), 404

def editar_livro(id, novo_titulo=None, novo_autor=None, novo_preco=None):
    livro = obter_livro_por_id(id)
    
    if livro:
        if novo_titulo is not None:
            livro['titulo'] = novo_titulo
        if novo_autor is not None:
            livro['autor'] = novo_autor
        if novo_preco is not None:
            livro['preco'] = novo_preco
        return True  # Indica que a edição foi bem-sucedida
    
    return False  # Indica que o livro não foi encontrado

def incluir_livro(novo_id, novo_titulo, novo_autor, novo_preco):
    # Verifica se o ID já existe
    if obter_livro_por_id(novo_id) is not None:
        return False  # Indica que o livro com o mesmo ID já existe
    
    novo_livro = {
        'id': novo_id,
        'titulo': novo_titulo,
        'autor': novo_autor,
        'preco': novo_preco
    }
    livros.append(novo_livro)
    return True  # Indica que a inclusão foi bem-sucedida

# Função auxiliar para remover livro usando .pop() (remove e retorna o livro removido)
def excluir_livro_por_id(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            return livros.pop(indice)  # pop remove pelo índice e retorna o elemento
    return None

# Função auxiliar alternativa usando comando del do Python (apenas deleta)
def excluir_livro_com_del(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]  # del deleta da lista pelo índice
            return True
    return False

@app.route('/livros', methods=['POST'])
def criar_livro():
    dados = request.get_json(silent=True)

    if not isinstance(dados, dict):
        return jsonify({'message': 'O corpo da requisição deve ser um objeto JSON'}), 400

    titulo = dados.get('titulo')
    autor = dados.get('autor')
    preco = dados.get('preco')

    if not isinstance(titulo, str) or not titulo.strip():
        return jsonify({'message': 'O campo "titulo" é obrigatório e deve ser um texto'}), 400
    if not isinstance(autor, str) or not autor.strip():
        return jsonify({'message': 'O campo "autor" é obrigatório e deve ser um texto'}), 400
    if isinstance(preco, bool) or not isinstance(preco, (int, float)) or preco < 0:
        return jsonify({'message': 'O campo "preco" é obrigatório e deve ser um número não negativo'}), 400

    novo_id = max((livro['id'] for livro in livros), default=0) + 1
    incluir_livro(novo_id, titulo.strip(), autor.strip(), preco)
    return jsonify(obter_livro_por_id(novo_id)), 201

# Rota HTTP DELETE para excluir um livro por ID usando pop
@app.route('/livros/<int:id>', methods=['DELETE'])
def deletar_livro(id):
    livro_removido = excluir_livro_por_id(id)

    if livro_removido:
        return jsonify({
            'message': 'Livro excluído com sucesso',
            'livro_removido': livro_removido
        }), 200

    return jsonify({'message': 'Livro não encontrado'}), 404

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
