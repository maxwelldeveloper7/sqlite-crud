from models.models import criar_banco_e_tabelas
from views.views import (
    menu_principal,
    input_responsavel,
    input_crianca,
    confirmar_exclusao,
    exibir_resposavel,
    input_id,
    input_atualizacao
)
import controllers.controllers as controller

def main():
    criar_banco_e_tabelas()
    while True:
        opcao = menu_principal()
        
        if opcao == '1':
            nome, endereco, telefone = input_responsavel()
            controller.criar_responsavel(nome, endereco, telefone)
            print("Responsável inserido com sucesso!")
        elif opcao == '2':
            nome, idade, responsavel_id = input_crianca()
            if controller.criar_crianca(nome, idade, responsavel_id):
                print("Criança inserida com sucesso!")
            else:
                print("Responsável não encontrado. Por favor, insira um ID de responsável válido.")
        
        elif opcao == '3':
            responsaveis = controller.listar_responsaveis()
            exibir_resposavel(responsaveis)
        elif opcao == '4':
            responsavel_id = input_id("Digite o ID do responsável a ser atualizado: ")
            responsavel = controller.consultar_responsavel(responsavel_id=responsavel_id)
            if not responsavel:
                print("Responsável não encontrado. Por favor, insira um ID de responsável válido.")
                continue
            novo_nome, novo_endereco, novo_telefone = input_atualizacao(responsavel)
            if controller.atualizar_responsavel()