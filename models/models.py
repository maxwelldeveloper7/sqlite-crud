from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

engine = create_engine('sqlite:///:creche.db')

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

class Responsavel(Base):
    __tablename__ = 'responsavel'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    endereco = Column(String)
    telefone = Column(String)
    
    crianca = relationship('Crianca', back_populates='responsavel')

class Crianca(Base):
    __tablename__ = 'crianca'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)
    responsavel_id = Column(Integer, ForeignKey('responsavel.id'))
    
    responsavel = relationship('Responsavel', back_populates='crianca')

def criar_banco_e_tabelas():
    Base.metadata.create_all(engine)
