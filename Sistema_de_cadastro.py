#Trabalho final algoritmos

lista = []
indice = 0
def menu():
    print(""" 
    BEM VINDO AO SISTEMA DE CADASTRO DE BANDAS!
    
    O que você deseja fazer?
    
    1 - Novo cadastro
    2 - Verificar Bandas cadastradas
    3 - Verificar informações de bandas cadastradas
    4 - Procurar por Banda Cadastrada
""")


def novo_cadastro():
    nome = input("Digite o nome da banda: ")
    integrantes = input("Digite o nome de seus integrantes: ")
    albuns = int(input("Digite a quantidade de albuns da banda: "))

    banda = {"nome" : nome, "integrantes" : integrantes, "Albuns" : albuns}
    lista.append(banda)

    print("Banda cadastrada com sucesso\nlista atualizada")
menu()
novo_cadastro()


def buscar():
    busca = input("Digite o termo a ser buscado: ").lower
     