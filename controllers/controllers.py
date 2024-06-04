from models import session, Responsavel, Crianca

def inserir_responsavel(nome, endereco, telefone):
    novo_responsavel = Responsavel(nome=nome, endereco=endereco, telefone=telefone)
    session.add(novo_responsavel)
    session.commit()

def inserir_crianca(nome, idade, responsavel_id):
    responsavel = session.query(Responsavel).filter_by(id=responsavel_id).first()
    if not responsavel:
        return False
    nova_crianca = Crianca(nome=nome, idade=idade, responsavel_id=responsavel_id)
    session.add(nova_crianca)
    session.commit()
    return True

def consultar_responsaveis():
    return session.query(Responsavel).all()

def atualizar_responsavel(responsavel_id, novo_nome, novo_endereco, novo_telefone):
    responsavel = session.query(Responsavel).filter_by(id=responsavel_id).first()
    if not responsavel:
        return False
    if novo_nome:
        responsavel.nome = novo_nome
    if novo_endereco:
        responsavel.endereco = novo_endereco
    if novo_telefone:
        responsavel.telefone = novo_telefone
        
    session.commit()
    return True

def excluir_crianca(crianca_id):
    crianca = session.query(Crianca).filter_by(id=crianca_id).first()
    if not crianca:
        return False
    session.delete(crianca)
    session.commit()
    return True
