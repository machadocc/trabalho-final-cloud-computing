
Descrição
- API em Python/Flask que expõe rotas para verificação de status e consulta de produtos simulados.
- Pipeline CI configurado em `.github/workflows/ci.yml` executando testes e lint.

Pré-requisitos
- Python 3.10+ instalado
- Git


Instruções rápidas para quem clonar o repositório

1) Clonar o repositório

2) Pré-requisitos

- Python 3.10+ instalado
- Git

3) Criar e ativar ambiente virtual

```bash
python -m venv .venv
# PowerShell
.\.venv\Scripts\Activate.ps1
# Bash / macOS / WSL
source .venv/bin/activate
```

4) Instalar dependências

```bash
python -m pip install --upgrade pip
python -m pip install -r api/requirements.txt
```

5) Executar a aplicação

```bash
python api/app.py
```

6) Executar os testes

```bash
python -m pytest api/tests/ -v
```

Observação sobre CI

O workflow de CI está em `.github/workflows/ci.yml` e executa lint (flake8) e os testes (pytest) em cada push/pull request nas branches `main`/`master`.

# Commit checkpoint: commit-1
