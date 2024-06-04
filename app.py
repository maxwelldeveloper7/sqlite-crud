# Importar as bibliotecas necessárias
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Conectar ao banco de dados SQLite (cria se não existir)
engine = create_engine('sqlite:///creche.db')

# Base para nossos modelos
Base = declarative_base()

# Criar uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# Definir a tabela para 'Responsáveis'
class Responsavel(Base):
    __tablename__ = 'responsaveis'
    
    id = Column(Integer, primary_key=True) # Chave primária
    nome = Column(String, nullable=False) # Nome do responsável
    endereco = Column(String) # Endereço
    telefone = Column(String) # Telefone
    
    # Relacionamento com crianças
    criancas = relationship("Crianca", back_populates="responsavel")

# Definir a tabela para 'Crianças'
class Crianca(Base):
    __tablename__ = 'criancas'
    
    id = Column(Integer, primary_key=True) # Chave primária
    nome = Column(String, nullable=False) # Nome da criança
    idade = Column(Integer, nullable=False) # Idade da criança
    responsavel_id = Column(Integer, ForeignKey('responsaveis.id')) # Chave estrangeira
    
    # Relacionamento com Responsável
    responsavel = relationship("Responsavel", back_populates="criancas")

# Criar todas as tabelas definidas
Base.metadata.create_all(engine)

# Adicionar responsáveis
resp1 = Responsavel(nome='Ana', endereco='Rua A, 123', telefone='1234-5678')
resp2 = Responsavel(nome='Bruna', endereco='Rua B, 456', telefone='2345-6789')

# Adicionar crianças para esses responsáveis
crianca1 = Crianca(nome='Pedro', idade=3, responsavel=resp1)
crianca2 = Crianca(nome='Maria', idade=4, responsavel=resp2)
crianca3 = Crianca(nome='Lucas', idade=2, responsavel=resp1)

# Adicionar ao banco de dados e salvar
session.add(resp1)
session.add(resp2)
session.commit() # Sempre realizar commit para persistir alterações