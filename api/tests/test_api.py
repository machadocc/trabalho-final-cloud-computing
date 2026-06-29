import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_produtos_status_200(client):
    response = client.get('/produtos')
    assert response.status_code == 200

def test_validar_estrutura_json_produtos(client):
    response = client.get('/produtos')
    dados = response.get_json()
    assert len(dados) > 0
    primeiro_registro = dados[0]
    assert "id" in primeiro_registro
    assert "nome" in primeiro_registro
    assert "categoria" in primeiro_registro
    assert "preco" in primeiro_registro

def test_get_produto_inexistente_404(client):
    response = client.get('/produtos/9999')
    assert response.status_code == 404
    dados = response.get_json()
    assert dados["erro"] == "Recurso não encontrado"

def test_validar_tipo_dados_id(client):
    response = client.get('/produtos/1')
    assert response.status_code == 200
    dados = response.get_json()
    assert isinstance(dados["id"], int)
    assert isinstance(dados["preco"], (int, float))