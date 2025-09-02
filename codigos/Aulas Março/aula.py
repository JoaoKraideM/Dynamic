"""
Aula do dia 24/03/2025

Resolução do exercício da aula 5

-Exercícios sobre filas - 06
-Informações sobre o cp2

Dia: 07/04/2025

Conteúdo: Busca binária, estrutura com filas e pilhas

- Poderá ser realizada em trio.
- Terão 24 horas para entregar (50% da nota).
- Apresentarão as estruturas em sala de aula (50% da nota).

Livro: Problems Solve Algorithms



#Crie uma estrutura qual o número 1 seja possível adicionar cientes, 2 seja possível atender o primeiro cliente, 3 sair da estrutura
"""
documentos = []

def menuAtendimento():
    while True:
        escolha = input(" Digite a escolha que deseja: 1-Add documento 2-Atender e 3-Sair: ")
        if escolha == '1':
            k = addLista(documentos) 
            print(k)
        elif escolha == '2':
            AteLista(documentos)
        
        elif escolha == '3':
            print ("Saindo do menu...")
            break
        else:
            print("Escolha invalida!!!")

def addLista(fila):
    while True:
        print ("Bem-vindo a adicionar arquivo, para sair digite Sair")
        escolha = input("Digite o nome do arquivo: ")
        if (escolha == "Sair"):
            print(documentos)
            break
        else:
            fila.append(escolha)
      
def AteLista(fila):
    atendido = fila.pop(0)
    print(f"Atendendo {atendido}")
    
    

    

"""
Exercicio 2 - Fila de impressão uma impressora recebe pedidos de diferentes usuários
"""
alta = [] 
baixa = []

def menuImpressora():
    while True:
        escolha = input("Digite a escola que deseja: 1-add lista 2-Atender 3- Sair: ")
        if escolha == "1":
            addlista(alta,baixa)
        elif escolha == "2":
            atender(alta,baixa)
        elif escolha == "3":
            break
        else:
            print("escolha invalida")
      
def addlista(Alta, Baixa):
    while True:
        escolha = input("Digite o documento que será adicionado (Escreva Sair caso deseje voltar): ")     
        if (escolha == "Sair"):
            print("Saindo.. ")
            break
        decisao = input("ele é alta ou baixa prioridade (digite Alta ou Baixa)? ")
        if (decisao == 'Alta'):
            Alta.append(escolha)
        elif (decisao == "Baixa"):
            Baixa.append(escolha)
        else:
            print("Não foi escolhido")

def atender(Alta, Baixa):
    while True:
        print("Atenderemos por prioridade, primeiro faremos o atendimento do de Alta e após os de Baixa")
        while len(alta) > 0:
            impressao = Alta.pop(0)
            print(f"{impressao} foi atendida")
        while len(baixa)> 0:
            impressao = Baixa.pop(0)
            print(f"{impressao} foi atendida")
        break
        
    
#Menu 3 com as duas opções para o usuário escolher
def menu():
    while True:
        escolha = input("Digite qual menu deseja utilizar: 1-Menu Atendimento 2-Menu Atendimento Alto e Baixo: ")
        if (escolha == "Sair"):
            print("Parando o menu...")
            break
        elif (escolha == "1"):
            print(menuAtendimento())
        elif (escolha == "2"):
            print(menuImpressora())
        else:
            print("Opção Invalida!!!")
            
while True:
    print(menu())