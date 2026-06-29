import os
import json
from flask import Flask, jsonify, abort

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, 'data', 'produtos.json')

def carregar_dados():
    try:
        with open(JSON_PATH, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({
        "nome": "API de Gestão de Produtos - Cloud Computing UNIDAVI",
        "versao": "1.0.0",
        "status": "operacional"
    }), 200

@app.route('/produtos', methods=['GET'])
def get_produtos():
    dados = carregar_dados()
    if not dados:
        return jsonify({"erro": "Banco de dados local não encontrado"}), 500
    return jsonify(dados), 200

@app.route('/produtos/<int:produto_id>', methods=['GET'])
def get_produto_por_id(produto_id):
    dados = carregar_dados()
    produto = next((item for item in dados if item["id"] == produto_id), None)
    if produto is None:
        abort(404)
    return jsonify(produto), 200

@app.errorhandler(404)
def not_found(error):
    return jsonify({"erro": "Recurso não encontrado", "codigo": 404}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)