from dataclasses import dataclass
import time 
import os 
os.system("cls || clear")

lista_alunos = []

@dataclass
class Endereco:
    logradouro = str
    numero = str
    cidade = str
    estado = str

@dataclass
class Aluno:
    nome = str
    data_nasc = str
    r_a = str
    curso = str
    endereco = (Endereco)


def mostrar_dados(self):
    print(f"Nome: {self.nome} \nData de Nascimento: {self.data_nasc} \nR.A: {self.r_a} \nCurso: {self.curso} \nEndereço: {self.logradouro} Número: {self.numero} Cidade: {self.cidade} Estado: {self.estado}")


def lista_vazia(lista_alunos):
    if not lista_alunos:
        print("\nNão há alunos cadastrados.")
        return True
    return False

def novo_aluno():
    print("==== Adicionar novo aluno ====")
    nome =  input("Digite seu nome: ")
    data_nasc = input ("infome sua data de nascimento: ")
    r_a = input ("Informe seu R.A: ")
    curso = input ("Infome o seu curso: ")
    novo_aluno = Aluno(nome=nome, data_nasc=data_nasc, r_a=r_a, curso=curso, ) 
    


    
print("""
=== Menu ===
1 - Adicionar 
2 - Exibir Dados
3 - Atualizar
4 - Excluir
0 - Sair
""")

opcao = int(input("digite uma das opções acima!.: "))
