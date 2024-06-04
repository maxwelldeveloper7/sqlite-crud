def menu_principal():
    print("\n=== Menu ===")
    print("1. Inserir Responsável")
    print("2. Inserir Criança")
    print("3. Consultar Responsáveis e Crianças")
    print("4. Atualizar Responsável")
    print("5. Excluir Criança")
    print("6. Sair do Programa")
    
    opcao = input("Escolha uma opção: ")
    return opcao

def input_responsavel():
    nome = input("Digite o nome do responsável: ")
    endereco = input("Digite o endereço do responsável: ")
    telefone = input("Digite o telefone do responsável: ")
    return nome, endereco, telefone

def input_crianca():
    nome = input("Digite o nome da criança: ")
    idade = input("Digite a idade da criança: ")
    responsavel_id = input("Digite o ID do responsável: ")
    return nome, idade, responsavel_id

def confirmar_exclusao(nome):
    confirmacao = input(f"Tem certeza que deseja excluir {nome}? (sim/não): ")
    return confirmacao.lower() == 'sim'

def exibir_resposavel(responsaveis):
    if not responsaveis:
        print("Nenhum responsável encontrado.")
    for responsavel in responsaveis:
        print(f"\nResponsável ID: {responsavel.id}")
        print(f"Nome: {responsavel.nome}")
        print(f"Endereço: {responsavel.endereco}")
        print(f"Telefone: {responsavel.telefone}")
        print("Crianças:") 
        if not responsavel.crianca:
            print("Nenhuma criança encontrada.")
        else:
            for crianca in responsavel.crianca:
                print(f"    Criança ID: {crianca.responsavel_id}")
                print(f"    Nome: {crianca.nome}")
                print(f"    dade: {crianca.idade}")
                print("-------------------------------------")

def input_id(mensagem):
    return int(input(mensagem))

def input_atualizacao(responsavel):
    nome = input(f"Digite o novo nome (atual: {responsavel.nome}): ")
    endereco = input(f"Digite o novo endereço (atual: {responsavel.endereco}): ")
    telefone = input(f"Digite o novo telefone (atual: {responsavel.telefone}): ")
    return nome, endereco, telefone
