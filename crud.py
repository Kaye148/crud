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
def encontar_cliente_por_nome(lista_clientes, nome_buscar):
    nome_buscar_lower = nome_buscar.lower()
    for cliente in lista_clientes:
        if cliente.nome.lower() == nome_buscar_lower:
            return cliente
    return None # None significa retornar vazio, sem conteúdo.

# Função para mostar todos os clientes.
def mostar_todos_clientes(lista_clientes):
    if lista_esta_vazia(lista_clientes):
        return
    
    print("\n--- Lista de Clientes ---")
    for cliente in lista_clientes:
        print(f"{cliente.mostar_dados()}")

# Função para atualizar clientes.
def atualizar_clientes(lista_clientes):
    if lista_esta_vazia(lista_clientes):
        return
    # Mostar a lista para ajudar o usuário.
    mostar_todos_clientes(lista_clientes)
    print("--- Atualizar dados do cliente ---")
    nome_buscar = input("\nDigite o nome do cliente: ")
    cliente_para_atualizar = encontar_cliente_por_nome(lista_clientes, nome_buscar)

    if cliente_para_atualizar:
        print("\nPessoa encontrada.")
        print("\n Digite os novos dados ou deixe em branco para manter o valor atual.")

        print("\nNome atual: {cliente_para_atualizar.nome}")
        novo_nome = input("novo_nome")

        print("\nE-mail atual: {cliente_para_atualizar.email}")
        novo_email = input("Novo E-mail")

        print("\nTelefone atual: {cliente_para_atualizar.telefone}")
        novo_telefone = input(f" Novo mome: ()")

        if novo_nome:
            cliente_para_atualizar.nome = novo_nome
        if novo_email:
            cliente_para_atualizar.email = novo_email
        if novo_telefone:
            cliente_para_atualizar.telefone = novo_telefone
        
        print(f"\nDados do cliente: {nome_buscar} atualizados com sucesso!")
    else:
        print(f"\nCliente com nome { nome_buscar} não encontrado.")
