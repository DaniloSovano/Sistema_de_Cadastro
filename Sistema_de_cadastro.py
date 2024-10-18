#Trabalho final algoritmos

import os

lista =[
    {"nome": "metallica", "integrantes": "james hetfield, lars ulrich, kirk hammett, robert trujillo", "albuns": 10},
    {"nome": "pink floyd", "integrantes": "david gilmour, roger waters, nick mason, richard wright", "albuns": 15},
    {"nome": "nirvana", "integrantes": "kurt cobain, krist novoselic, dave grohl", "albuns": 3},
    {"nome": "beatles", "integrantes": "john lennon, paul mccartney, george harrison, ringo starr", "albuns": 13},
    {"nome": "led zeppelin", "integrantes": "robert plant, jimmy page, john paul jones, john bonham", "albuns": 8},
    {"nome": "queen", "integrantes": "freddie mercury, brian may, roger taylor, john deacon", "albuns": 15}
]





def menu():
    print(""" 
    BEM VINDO AO SISTEMA DE CADASTRO DE BANDAS!
    
    O que você deseja fazer?
    
    1 - Novo cadastro
    2 - Verificar Bandas cadastradas
    3 - Verificar informações de bandas cadastradas
    4 - Procurar por Banda Cadastrada
""")

def escolha():
    escolha = int(input("Escolha uma opção: "))
    if escolha == 1:
        novo_cadastro()
    elif escolha == 2:
        buscar()

def novo_cadastro():
    nome = input("Digite o nome da banda: ").lower()
    integrantes = input("Digite o nome de seus integrantes: ").lower()
    albuns = int(input("Digite a quantidade de albuns da banda: "))

    banda = {"nome": nome, "integrantes": integrantes, "Albuns": albuns}
    lista.append(banda)

    print("Banda cadastrada com sucesso\nlista atualizada")


def buscar():
    print("""
    1 - Nome da Banda
    2 - Integrantes da banda
    3 - Quantidade de albuns da banda
    """)
    
    busca = int(input("Escolha o tipo de busca: "))
    
    if busca == 1:
        termo = input("Digite o Nome da banda a ser procurada: ")
        for i in range(len(lista)):
            if termo in lista[i]['nome']:
                print(f"nome: {lista[i]['nome']}\nintegrantes: {lista[i]['integrantes']}\nalbuns: {lista[i]['albuns']}")

    elif busca == 2:
        termo = input("Digite o nome do integrante a ser procurado: ")
        for i in range(len(lista)):
            if termo in lista[i]['integrantes']:
                print(f"nome: {lista[i]['nome']}\nintegrantes: {lista[i]['integrantes']}\nalbuns: {lista[i]['albuns']}")

    elif busca == 3:
        termo = input("Digite a quantidade de albuns a ser procurado: ")
        for i in range(len(lista)):
            if int(termo) == lista[i]['albuns']:
                print(f"nome: {lista[i]['nome']}\nintegrantes: {lista[i]['integrantes']}\nalbuns: {lista[i]['albuns']}")


while True:
    menu()
    escolha()
