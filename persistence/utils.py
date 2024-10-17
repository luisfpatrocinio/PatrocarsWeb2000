from sqlmodel import create_engine

## Função para obter a engine de conexão com o banco de dados (atalho)
def get_engine():
  engine = create_engine('sqlite:///montadoras.db')
  return engine