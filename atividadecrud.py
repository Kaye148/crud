import os
import time
from dataclasses import dataclass
os.system("cls || clear") #Limpar o terinal em windowns e 

lista_clientes = []

@dataclass
class Cliente:
    # Atributos da classe.
    # Atributos são variáveis que pertencem á classe.
    nome: str
    email: str
    telefone: str

    def mostrar_dados(self):
        print(f"Nome: {self.nome}  \nE-mail: {self.email} \nTelefone: {self.telefone}")

def lista_esta_vazia(lista_clientes):
    if not lista_clientes:
        print("\nNão há clientes cadastrados.")
        return True
    return False

def adicionar_clientes(lista_clientes):
    print("\n---Adicionar novo cliente ---")
    nome = input("digite seu nome: ")
    email = input("digite seu e-mail: ")
    telefone = input("digite seu telefone: ")

    novo_cliente = Cliente(nome=nome, email=email, telefone=telefone)
    lista_clientes.append(novo_cliente)
    print(f"\nCliente {nome} adicionado com sucesso! ")

# Função para encontar um cliente na lista.
def encontar_cliente_por_email(lista_clientes, email_buscar):
    email_buscar_lower = email_buscar.lower()
    for cliente in lista_clientes:
        if cliente.nome.lower() == email_buscar_lower:
            return cliente
    return None # None significa retornar vazio, sem conteúdo.

# Função para mostar todos os clientes.
def mostrar_todos_clientes(lista_clientes):
    if lista_esta_vazia(lista_clientes):
        return
    
    print("\n--- Lista de Clientes ---")
    for cliente in lista_clientes:
        cliente.mostrar_dados()

# Função para atualizar clientes.
def atualizar_clientes(lista_clientes):
    if lista_esta_vazia(lista_clientes):
        return
    # Mostar a lista para ajudar o usuário.
    mostrar_todos_clientes(lista_clientes)
    print("--- Atualizar dados do cliente ---")
    email_buscar = input("\nDigite o email: ")
    cliente_para_atualizar = encontar_cliente_por_email(lista_clientes, email_buscar)

    if cliente_para_atualizar:
        print("\nPessoa encontrada.")
        print("\n Digite os novos dados ou deixe em branco para manter o valor atual.")

        print(f"\nNome atual: {cliente_para_atualizar.nome}")
        novo_nome = input("Novo nome: ")

        print(f"\nE-mail atual: {cliente_para_atualizar.email}")
        novo_email = input("Novo E-mail: ")

        print(f"\nTelefone atual: {cliente_para_atualizar.telefone}")
        novo_telefone = input(" Novo Telefone: ")

        if novo_nome:
            cliente_para_atualizar.nome = novo_nome
        if novo_email:
            cliente_para_atualizar.email = novo_email
        if novo_telefone:
            cliente_para_atualizar.telefone = novo_telefone
        
        print(f"\nDados do cliente: {email_buscar} atualizados com sucesso!") 
    else:
        print(f"\nCliente com nome { email_buscar} não encontrado.")

#Função para excluir um cliente.
def excluir_cliente(lista_cliente):
    if lista_esta_vazia(lista_cliente):
        return
    
    mostrar_todos_clientes(lista_clientes)

    email = input("\nDigite o nome do cliente que deseja excluir: ")

    cliente_para_remover = encontar_cliente_por_email(lista_clientes, email)

    if cliente_para_remover:
        lista_clientes.remove(cliente_para_remover)
        print(f"\nCliente com o nome {email} excluido. ")
    else:
        print(f"\nCliente com o email {email} não encontrado ")

#Mostar menu.
while True:
    print("""
--- Gerenciador de Clientes ---
1 - Adicionar
2 - Mostar todos
3 - Atualizar 
4 - Excluir
0 - Sair
""")
    
    opcao = int(input("Digite uma das opções acima: "))

    match opcao:
        case 1:
            adicionar_clientes(lista_clientes)
        case 2:
            mostrar_todos_clientes(lista_clientes)
        case 3:
            atualizar_clientes(lista_clientes)
        case 4:
            excluir_cliente(lista_clientes)
        case 0:
            print("\nSaindo do programa. . . ")
        case _:
            print("\nOpção inválida. \nTente novamente. . . ")

    if opcao != 1 and opcao != 0:
        time.sleep(4)
    elif opcao == 1:
        time.sleep(1)
