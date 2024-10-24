import os
import time  

# lista com as bandas cadastradas
lista = [
    {"nome": "metallica", "integrantes": "james hetfield, lars ulrich, kirk hammett, robert trujillo", "albuns": 10, "vendas": 125.0, "ano": 1981},
    {"nome": "pink floyd", "integrantes": "david gilmour, roger waters, nick mason, richard wright", "albuns": 15, "vendas": 75.0, "ano": 1965},
    {"nome": "nirvana", "integrantes": "kurt cobain, krist novoselic, dave grohl", "albuns": 3, "vendas": 30.0, "ano": 1987},
    {"nome": "beatles", "integrantes": "john lennon, paul mccartney, george harrison, ringo starr", "albuns": 13, "vendas": 600.0, "ano": 1960},
    {"nome": "led zeppelin", "integrantes": "robert plant, jimmy page, john paul jones, john bonham", "albuns": 8, "vendas": 300.0, "ano": 1968},
    {"nome": "queen", "integrantes": "freddie mercury, brian may, roger taylor, john deacon", "albuns": 15, "vendas": 300.0, "ano": 1970}
]

def menu():  # Menu inicial a ser impresso
    print(""" 
    BEM VINDO AO SISTEMA DE CADASTRO DE BANDAS!
    
    O que você deseja fazer?
    
    1 - Novo cadastro
    2 - Procurar por Banda Cadastrada
    3 - Verificar todas as bandas cadastradas
    4 - Remover uma banda
    5 - Editar uma banda
    6 - Verificar banda com maior número de vendas
    7 - verificar banda mais antiga
    8 - verificar banda mais recente
    9 - Listar intervalo
    0 - Sair
""")
    time.sleep(1)  # Pausa para que o usuário possa ler

def escolha():  # Função para escolher a opção do menu
    try:
        escolha = int(input("Escolha uma opção: "))
        if escolha == 1:
            novo_cadastro()
        elif escolha == 2:
            buscar()
        elif escolha == 3:
            verificar_tudo()
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
        elif escolha == 9:
            listar_intervalo()
        elif escolha == 0:
            print("Saindo do sistema")
            time.sleep(1)  
            exit()
        else:
            print("Opção inválida")
            time.sleep(1)  
    except ValueError:
        print("Erro: Por favor, insira valores válidos.")
        time.sleep(1)  # Pausa após um erro

def novo_cadastro():  # Função adiciona uma nova banda a lista
    try:    
        nome = input("Digite o nome da banda: ").lower()
        integrantes = input("Digite o nome de seus integrantes: ").lower()
        albuns = int(input("Digite a quantidade de álbuns da banda: "))
        if albuns < 0:
            print("Erro: A quantidade de álbuns não pode ser negativa.")
            time.sleep(1)
            return
        vendas = float(input("Digite a quantidade aproximada de álbuns vendidos em milhões: "))
        if vendas < 0:
            print("Erro: A quantidade de vendas não pode ser negativa.")
            time.sleep(1)
            return
        ano = int(input("Digite o ano de formação da banda: "))
        if ano <= 0:
            print("Erro: O ano deve ser positivo.")
            time.sleep(1)
            return
    except ValueError:
        print("Erro: Por favor, insira valores válidos.")
        time.sleep(1)
        return
    banda = {"nome": nome, "integrantes": integrantes, "albuns": albuns, "vendas": vendas, 'ano': ano}
    lista.append(banda)
    print("Banda cadastrada com sucesso\nLista atualizada")
    time.sleep(1)  # Pausa para o usuário ler

def buscar():  # Função para buscar uma banda baseada em suas especificações
    print("""
    1 - Nome da Banda
    2 - Integrantes da banda
    3 - Quantidade de álbuns da banda
    4 - Quantidade de álbuns vendidos
    5 - Ano de formação da banda
    """)
    time.sleep(1)  # Pausa para o usuário ler
    
    busca = int(input("Escolha o tipo de busca: "))
    try:
        if busca == 1:
            termo = input("Digite o Nome da banda a ser procurada: ")
            for i in range(len(lista)):
                if termo in lista[i]['nome']:
                    print(f"Nome: {lista[i]['nome']}\nIntegrantes: {lista[i]['integrantes']}\nÁlbuns: {lista[i]['albuns']}\nVendas em milhões: {lista[i]['vendas']}\nAno de formação: {lista[i]['ano']}")
                    time.sleep(1)  # Pausa após exibir a banda encontrada

        elif busca == 2:
            termo = input("Digite o nome do integrante a ser procurado: ")
            for i in range(len(lista)):
                if termo in lista[i]['integrantes']:
                    print(f"Nome: {lista[i]['nome']}\nIntegrantes: {lista[i]['integrantes']}\nÁlbuns: {lista[i]['albuns']}\nVendas em milhões: {lista[i]['vendas']}\nAno de formação: {lista[i]['ano']}")
                    time.sleep(1)

        elif busca == 3:
            termo = input("Digite a quantidade de álbuns a ser procurada: ")
            for i in range(len(lista)):
                if int(termo) == lista[i]['albuns']:
                    print(f"Nome: {lista[i]['nome']}\nIntegrantes: {lista[i]['integrantes']}\nÁlbuns: {lista[i]['albuns']}\nVendas em milhões: {lista[i]['vendas']}\nAno de formação: {lista[i]['ano']}")
                    time.sleep(1)

        elif busca == 4:
            termo = input("Digite a quantidade de álbuns vendidos a ser procurada: ")
            for i in range(len(lista)):
                if float(termo) == lista[i]['vendas']: 
                    print(f"Nome: {lista[i]['nome']}\nIntegrantes: {lista[i]['integrantes']}\nÁlbuns: {lista[i]['albuns']}\nVendas em milhões: {lista[i]['vendas']}\nAno de formação: {lista[i]['ano']}")
                    time.sleep(1)

        elif busca == 5:
            termo = input("Digite o Ano de formação da banda a ser procurado: ")
            for i in range(len(lista)):
                if int(termo) == lista[i]['ano']:
                    print(f"Nome: {lista[i]['nome']}\nIntegrantes: {lista[i]['integrantes']}\nÁlbuns: {lista[i]['albuns']}\nVendas em milhões: {lista[i]['vendas']}\nAno de formação: {lista[i]['ano']}")
                    time.sleep(1)
        else:
            print("Opção inválida.") 
            time.sleep(1)  # Pausa após um erro
    except ValueError: 
        print("Erro: Por favor, insira valores válidos")    
        time.sleep(1)  

def verificar_tudo():  # Função para imprimir todas as bandas cadastradas
    for i in range(len(lista)):
        print(f"Nome: {lista[i]['nome']}\nIntegrantes: {lista[i]['integrantes']}\nÁlbuns: {lista[i]['albuns']}\nVendas em milhões: {lista[i]['vendas']}\nAno de formação: {lista[i]['ano']}\n")
        time.sleep(0.5)  # Pausa após exibir cada banda

def remover():  # Função para remover uma banda
    remove = input("Digite o Nome da banda a ser removida: ")
    for i in range(len(lista)):
        if remove == lista[i]['nome']:
            del lista[i]
            print("Banda removida com sucesso\nLista atualizada")
            time.sleep(1)  
            break
    else:
        print("Banda não encontrada")
        time.sleep(1)  

def edit():  # Função para editar as características da banda
    edit = input("Digite o nome da banda a ser editada: ")
    for i in range(len(lista)):
        if edit == lista[i]['nome']:
            print("""
                1 - Nome
                2 - Integrantes
                3 - Álbuns
                4 - Quantidade de álbuns vendidos
                5 - Ano de formação
            """)
            time.sleep(1)  # Pausa para que o usuário leia
            try:
                escolha = int(input("Qual o item a ser editado? "))
                if escolha == 1:
                    lista[i]['nome'] = input("Digite o novo nome: ")
                    print("Lista atualizada com sucesso!")
                    time.sleep(1)  # Pausa após editar
                elif escolha == 2:
                    lista[i]['integrantes'] = input("Digite o nome dos integrantes: ")
                    print("Lista atualizada com sucesso!")
                    time.sleep(1)
                elif escolha == 3:
                    lista[i]['albuns'] = int(input("Digite a nova quantidade de álbuns: "))
                    print("Lista atualizada com sucesso!")
                    time.sleep(1)
                elif escolha == 4:
                    lista[i]['vendas'] = float(input("Digite a nova quantidade de álbuns vendidos: "))
                    print("Lista atualizada com sucesso!")
                    time.sleep(1)
                elif escolha == 5:
                    lista[i]['ano'] = int(input("Digite o novo ano de formação da banda: "))
                    print("Lista atualizada com sucesso!")
                    time.sleep(1)
            except ValueError:
                print("Erro: Por favor, digite valores válidos. ")
                time.sleep(1)  

def verificar_vendas():  # Função para verificar o número de vendas
    maior = 0
    banda_maior = ""
    
    for i in range(len(lista)):
        vendas = lista[i]['vendas']
        if vendas > maior:
            maior = vendas
            banda_maior = lista[i]['nome']

    print(f"A banda com maior número de vendas é: {banda_maior} com {maior} milhões de álbuns vendidos")
    time.sleep(2) 

def banda_antiga():  # Função para verificar a banda mais antiga
    ano = lista[0]['ano']  
    banda_mais_antiga = lista[0]['nome']  
    
    for i in range(len(lista)):  
        ano_banda = lista[i]['ano']
        if ano_banda < ano:  
            ano = ano_banda
            banda_mais_antiga = lista[i]['nome']

    print(f"A banda mais antiga é {banda_mais_antiga}, formada no ano de {ano}")
    time.sleep(2)  # Pausa para que o usuário leia a mensagem

def banda_recente():  # Função para verificar a banda mais recente
    ano = lista[0]['ano']  
    banda_mais_recente = lista[0]['nome']  

    for i in range(len(lista)):  
        ano_banda = lista[i]['ano']
        if ano_banda > ano:  
            ano = ano_banda
            banda_mais_recente = lista[i]['nome']

    print(f"A banda mais recente é {banda_mais_recente}, formada no ano de {ano}")
    time.sleep(2)  

def listar_intervalo():  # Função para listar um intervalo de índices
    try:
        inicio = int(input("Digite o índice inicial: "))
        fim = int(input("Digite o índice final: "))
        if (inicio < 0) or (fim > len(lista)) or (inicio >= fim):
            print("Os valores digitados não são válidos.")
            time.sleep(1)  # Pausa após erro
        else:
            for i in range(inicio, fim):
                print(lista[i])
                time.sleep(1)  # Pausa após exibir cada banda
    except ValueError:
        print("Erro: Por favor, digite valores válidos.")
        time.sleep(1)  


while True:
    menu()
    escolha()
