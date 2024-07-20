import sys

# Ativar o ambiente virtual
activate_this = '/supermessenger-main/.venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Adicionar o caminho do projeto ao sys.path
sys.path.insert(0, '/supermessenger-main')

from app import app

if __name__ == "__main__":
    app.run()
