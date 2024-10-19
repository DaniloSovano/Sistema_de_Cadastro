#Trabalho final algoritmos

import os

lista =[
    {"nome": "metallica", "integrantes": "james hetfield, lars ulrich, kirk hammett, robert trujillo", "albuns": 10, "vendas": 125.0, "ano": 1981},
    {"nome": "pink floyd", "integrantes": "david gilmour, roger waters, nick mason, richard wright", "albuns": 15, "vendas": 75.0, "ano": 1965},
    {"nome": "nirvana", "integrantes": "kurt cobain, krist novoselic, dave grohl", "albuns": 3, "vendas": 30.0, "ano": 1987},
    {"nome": "beatles", "integrantes": "john lennon, paul mccartney, george harrison, ringo starr", "albuns": 13, "vendas": 600.0, "ano": 1960},
    {"nome": "led zeppelin", "integrantes": "robert plant, jimmy page, john paul jones, john bonham", "albuns": 8, "vendas": 300.0, "ano": 1968},
    {"nome": "queen", "integrantes": "freddie mercury, brian may, roger taylor, john deacon", "albuns": 15, "vendas": 300.0, "ano": 1970}

    ]





def menu():
    print(""" 
    BEM VINDO AO SISTEMA DE CADASTRO DE BANDAS!
    
    O que você deseja fazer?
    
    1 - Novo cadastro
    2 - Procurar por Banda Cadastrada
    3 - Verificar Bandas cadastradas
    4 - Remover uma banda
    5 - Editar uma banda
    6 - Verificar banda com maior numero de vendas
    7 - verificar banda mais antiga
    8 - verificar banda mais recente
""")

def escolha():
    escolha = int(input("Escolha uma opção: "))
    if escolha == 1:
        novo_cadastro()
    elif escolha == 2:
        buscar()
    elif escolha == 3:
        verify_all()
    elif escolha == 4:
        remover()
    elif escolha == 5:
        edit()
    elif escolha == 6:
        verificar_vendas()
    elif escolha == 7:
        banda_antiga()
    elif escolha == 8:
        banda_recente()
def novo_cadastro():
    nome = input("Digite o nome da banda: ").lower()
    integrantes = input("Digite o nome de seus integrantes: ").lower()
    albuns = int(input("Digite a quantidade de albuns da banda: "))
    vendas = float(input("Digite a quantidade aproximada de albuns vendidos em milhões: "))
    ano = int(input("Digite o ano de formação da banda: "))
    banda = {"nome": nome, "integrantes": integrantes, "Albuns": albuns, "vendas": vendas, 'ano': ano}
    lista.append(banda)

    print("Banda cadastrada com sucesso\nlista atualizada")


def buscar():
    print("""
    1 - Nome da Banda
    2 - Integrantes da banda
    3 - Quantidade de albuns da banda
    4 - Quantidade de albuns vendidos
    5 - Ano de formação da banda
    """)
    
    busca = int(input("Escolha o tipo de busca: "))
    
    if busca == 1:
        termo = input("Digite o Nome da banda a ser procurada: ")
        for i in range(len(lista)):
            if termo in lista[i]['nome']:
                print(f"Nome: {lista[i]['nome']}\nIntegrantes: {lista[i]['integrantes']}\nAlbuns: {lista[i]['albuns']}\nVendas: {lista[i]["vendas"]}\nAno de formação: {lista[i]['ano']}")

    elif busca == 2:
        termo = input("Digite o nome do integrante a ser procurado: ")
        for i in range(len(lista)):
            if termo in lista[i]['integrantes']:
                print(f"Nome: {lista[i]['nome']}\nIntegrantes: {lista[i]['integrantes']}\nAlbuns: {lista[i]['albuns']}\nVendas: {lista[i]["vendas"]}\nAno de formação: {lista[i]['ano']}")

    elif busca == 3:
        termo = input("Digite a quantidade de albuns a ser procurado: ")
        for i in range(len(lista)):
            if int(termo) == lista[i]['albuns']:
                print(f"Nome: {lista[i]['nome']}\nIntegrantes: {lista[i]['integrantes']}\nAlbuns: {lista[i]['albuns']}\nVendas: {lista[i]["vendas"]}\nAno de formação: {lista[i]['ano']}")
                
    elif busca == 4:
        termo = input("Digite a quantidade de albuns vendidos a ser procurada: ")
        for i in range(len(lista)):
            if int(termo) == lista[i]['vendas']:
                print(f"Nome: {lista[i]['nome']}\nIntegrantes: {lista[i]['integrantes']}\nAlbuns: {lista[i]['albuns']}\nVendas: {lista[i]["vendas"]}\nAno de formação: {lista[i]['ano']}")

    elif busca == 5:
        termo = input("Digite o Ano de formação da banda a ser procurado: ")
        for i in range(len(lista)):
            if int(termo) == lista[i]['ano']:
                print(f"Nome: {lista[i]['nome']}\nIntegrantes: {lista[i]['integrantes']}\nAlbuns: {lista[i]['albuns']}\nVendas: {lista[i]["vendas"]}\nAno de formação: {lista[i]['ano']}")
        
def verify_all():
    for i in range(len(lista)):
        print(f"Nome: {lista[i]['nome']}\nIntegrantes: {lista[i]['integrantes']}\nalbuns: {lista[i]['albuns']}\nVendas: {lista[i]["vendas"]}\nAno de formação: {lista[i]['ano']}\n")

def remover():
    remove = input("Digite o Nome da banda a ser removida: ")
    for i in range(len(lista)):
        if remove == lista[i]['nome']:
            del lista[i]
            print("Banda removida com sucesso\nLista atualizada")
            break
    else:
        print("Banda não encontrada")

def edit():
    edit = input("Digite o nome da banda a ser editada: ")
    for i in range(len(lista)):
        if edit == lista[i]['nome']:
            print("""
                1 - Nome
                2 - integrantes
                3 - Albuns
                4 - Quantidade de albuns vendidos
                5 - Ano de formação
            """)
            escolha = int(input("Qual o item a ser editado?"))
            if escolha == 1:
                lista[i]['nome'] = input("Digite o novo nome: ")
                print("Lista atualizada com sucesso!")
            elif escolha == 2:
                lista[i]['integrantes'] = input("Digite o nome dos integrantes: ")
                print("Lista atualizada com sucesso!")
            elif escolha == 3:
                lista[i]['albuns'] = int(input("Digite a nova quantidade de albuns: "))
                print("Lista atualizada com sucesso!")
            elif escolha == 4:
                lista[i]['vendas'] = float(input("Digite a nova quantidade de albuns vendidos: "))
            elif escolha == 5:
                lista[i]['ano'] = int(input("Digite o novo ano de formação da banda: "))

def verificar_vendas():
    maior = 0

    for i in range(len(lista)):
        vendas = lista[i]['vendas']
        if vendas > maior:
            maior = vendas
            banda_maior = lista[i]['nome']

    print(f"A banda com maior número de vendas é: {banda_maior} com {maior} álbuns vendidos")

def banda_antiga():
    ano = lista[0]['ano']  
    banda_mais_antiga = lista[0]['nome']  
    
    for i in range(len(lista)):  
        ano_banda = lista[i]['ano']
        if ano_banda < ano:  
            ano = ano_banda
            banda_mais_antiga = lista[i]['nome']

    print(f"A banda mais antiga é {banda_mais_antiga}, formada no ano de {ano}")

def banda_recente():
    ano = lista[0]['ano']  
    banda_mais_recente = lista[0]['nome']  

    for i in range(len(lista)):  
        ano_banda = lista[i]['ano']
        if ano_banda > ano:  
            ano = ano_banda
            banda_mais_recente = lista[i]['nome']

    print(f"A banda mais recente é {banda_mais_recente}, formada no ano de {ano}")

            






while True:
    menu()
    escolha()
