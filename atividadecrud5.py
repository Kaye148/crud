from dataclasses import dataclass
import time 
import os 
os.system("cls||clear")

lista_produtos = []
lista_produtos = []

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str
    endereco: str

    def mostrar_cliente(self):
        print(f"Nome: {self.nome}, \nE-mail: {self.email},\nTelefone: {self.telefone}, \nEndereço: {self.endereco} ")

@dataclass
class Produto:
    nome: str
    quantidade: str
    lote: str
    validade: str


    def mostrar_produto(self):
        print(f"Nome: {self.nome}, \nQuantidade: {self.quantidade}, \nLote: {self.lote}, \nValidade: {self.validade}")

def lista_vazia_clientes(lista_produtos):
    if not lista_produtos:
        print("Não há clientes cadastrados.")
        return True
    return False

def lista_vazia_produtos(lista_produtos):
    if not lista_produtos:
        print("Não há produtos cadastrados.")
        return True
    return False

def adicionar_cliente(lista_produtos):
    print("Fazer novo cadastro")
    nome = input("Informe seu nome: ")
    email = input("Informe seu E-mail: ")
    telefone = input("Informe seu Telefone: ")
    endereco = input("Informe o seu Endereço: ")

    novo_cliente = Cliente(nome=nome, email=email, telefone=telefone, endereco=endereco)
    lista_produtos.append(novo_cliente)
    print("Adicionados com sucesso")

def adicionar_produto(lista_produtos):
    print ("cadastra novo produto")
    nome = input("Informe o nome do produto: ")
    quantidade = input("informe a quantidade de produtos: ")
    lote = input("informe o Lote")
    validade = input("informe a quantidade: ")

    novo_produto = Produto(nome=nome,quantidade=quantidade, lote=lote, validade=validade)
    lista_produtos.append(novo_produto)
    print("adicionado com sucesso")

def encontrar_por_nome(lista_produtos, nome_buscar):
    nome_buscar_lower = nome_buscar.lower()
    for nome in lista_produtos or  lista_produtos:
        return nome
    return None

def encontrar_por_nome( lista_clientes, nome_buscar):
    nome_buscar_lower = nome_buscar.lower()
    for nome in lista_produtos or  lista_produtos:
        return nome
    return None

def mostrar_dados(lista_produtos):
    if lista_vazia_clientes (lista_produtos):
        return
    
    print("Lista")
    for nome in lista_produtos:
        nome.mostrar_dados()
    
def atualizar_dados(lista_produtos):
    if lista_vazia_clientes:
        return
    
def mostrar_dados(lista_produtos):
    if lista_vazia_produtos (lista_produtos):
        return
    
    print("Lista")
    for produto in lista_produtos :
        produto.mostrar_dados()
    
def atualizar_dados(lista_produtos):
    if lista_vazia_clientes:
        return
    
    mostrar_dados(lista_produtos)
    print("atualizar dados")
    nome_buscar = input("Informe o nome: ")
    dados_para_atualizar = encontrar_por_nome(lista_produtos, nome_buscar)

    mostrar_dados(lista_produtos)
    print("atualizar dados")
    nome_buscar = input("Informe o nome: ")
    dados_para_atualizar = encontrar_por_nome(lista_produtos, nome_buscar)

    if dados_para_atualizar:
        print("Dados encontrado")
        print("atualize as informações")

        print(f"Nome atual: {dados_para_atualizar.nome}")
        novo_nome = input("Informe o novo nome: ")

        print(f"E-mail atual: {dados_para_atualizar.email}")
        novo_email = input("Informe um novo E-mail: ")

        print(f"Telefone atual: {dados_para_atualizar.telefone}")
        novo_telefone = input("Informe um novo Telefone: ")

        print(f"Endereço atual: {dados_para_atualizar.endereco}")
        novo_endereco = input("informe um novo endereço: ")
    elif quantidade:
        print(f"quantidade atual: {dados_para_atualizar.quantidade}")
        nova_quantidade = input("informe uma nova quantidade: ")
    elif lote:
        print(f"quantidade de lotes atual: {dados_para_atualizar.lote}")
        novo_lote = input("Informe um novo lote: ")
    else:
        validade(f"validades atual: {dados_para_atualizar.validade} ")
        nova_validate = input("Informe uma nova validade: ")

def excluir_dados(lista_produtos):
    if lista_vazia_clientes or lista_vazia_produtos(lista_produtos):
        return
    
    mostrar_dados(lista_clientes)

    nome_buscar = input("Informe o nome do que deseja excluir: ")

    cliente_ou_produto_remover = encontrar_por_nome(lista_clientes)

    if cliente_ou_produto_remover:
        lista_clientes (cliente_ou_produto_remover)
        print("Excluido com sucesso")

while True:
    print("""
====Menu====
1 - Adicionar
2 - Exibir dados
3 - Atualizar dados
4 - Excluir dados
0 - sair
""")
    
    opcao = int(input("informe uma das opções acima: "))

    match opcao:
        case 1:
            adicionar_cliente (lista_clientes)
        case 2:
            mostrar_dados(lista_clientes)
        case 3:
            atualizar_dados(lista_clientes)
        case 4:
            excluir_dados(lista_clientes)
        case 0:
            print("saindo do programa . . .")
        case _:
            print("opção invalida \n tente novamente")

    if opcao != 1 and opcao != 0:
        time.sleep(2)
    elif opcao == 1:
        time.sleep(1)
    opcao = int(input("informe uma das opções acima: "))

    match opcao:
        case 1:
            adicionar_produto (lista_produtos)
        case 2:
            mostrar_dados(lista_produtos)
        case 3:
            atualizar_dados(lista_produtos)
        case 4:
            excluir_dados(lista_produtos)
        case 0:
            print("saindo do programa . . .")
        case _:
            print("opção invalida \n tente novamente")

    if opcao != 1 and opcao != 0:
        time.sleep(2)
    elif opcao == 1:
        time.sleep(1)
            