def potencia (base,expoente):
    if expoente == 0:
            return 1
    else:
        return base * potencia(base, expoente - 1)



lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def busca(lista, x):
        if not lista:
            return False
        else:
            if lista[0] == x:
                return True
            else:
                return busca(lista[1:], x)


print(busca(lista, 2))


lista = [1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def conta(lista, n):
    if n not in lista:
        return False
    else:
        if lista[0] == n:
            return 1 + conta(lista[1:], n)
        else:
            return conta(lista[1:], n)

print(conta(lista,2))


#ex 1
def calculo(x,y):
    if y == 0 or  x == 0:
        return 0
    else:
        return y + calculo(x - 1, y)

print(calculo(10,10))

#ex 2
def busca(lista, x):
    if not lista:
        return False
    else:
        if lista[0] == x:
            return True
        else:
            return busca(lista[1:], x)

def conta(lista, n):
    if not lista:
        return 0
    else:
        if lista[0] == n:
            return 1 + conta(lista[1:], n)
        else:
            return conta(lista[1:], n)

print(busca([1, 2, 3, 4, 5], 3))  # Example use
print(conta([1, 2, 2, 2, 3, 4], 2))  # Example use



#ex 3
def busca_binaria(lista, elemento, inicio, fim):
    if inicio > fim:
        return False
    meio = (inicio + fim) // 2

    if lista[meio] == elemento:
        return True
    elif elemento < lista[meio]:
        return busca_binaria(lista, elemento, inicio, meio - 1)
    else:
        return busca_binaria(lista, elemento, meio + 1, fim)

       


#ex 4
#Exercicio que procura em arquivos json (Dicionarios) os nomes dos membros da familia
def busca_binaria(lista, elemento, inicio, fim):
    if inicio > fim:
        return -1
    meio = (inicio + fim) // 2

    if lista[meio] == elemento:
        return meio
    elif elemento < lista[meio]:
        return busca_binaria(lista, elemento, inicio, meio - 1)
    else:
        return busca_binaria(lista, elemento, meio + 1, fim)


print(busca_binaria([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7, 0, 9))
   
            
#Ex 5
familia = []

"""def menu():
    while True:
        print("===MENU===")
        print("1 - Cadastrar nome")
        print("2 - Listar pessoas")
        print("3 - Buscar um nome")
        print("4 - Deletar um nome")
        print("5 - Sair do programa")

        escolha = int(input("Digite qual programa deseja entrar: "))
        if escolha == 1:
            cadastraPessoa(familia)
        elif escolha == 2:
            print(PessoasFamilia(familia))
        elif escolha == 3:
            buscaNome(familia)
        elif escolha == 4:
            deletaNome(familia)
        elif escolha == 5:
            print("Saindo...")
            break  # Exit the loop
        else:
            print("Escolha inválida")

def cadastraPessoa(familia):
    nome = input("Digite o nome da pessoa que deseja cadastrar: ")
    familia.append(nome)
    print(f"{nome} cadastrado com sucesso.")

def buscaNome(familia):
    busca = input("Digite o nome que deseja achar: ").strip()
    if busca in familia:
        print(f"{busca} está na família.")
    else:
        print(f"{busca} não foi encontrado na família.")

def deletaNome(familia):
    nome = input("Digite o nome que deseja deletar: ").strip()
    if nome in familia:
        familia.remove(nome)
        print(f"{nome} foi removido da família.")
    else:
        print(f"{nome} não foi encontrado na família.")

def PessoasFamilia(familia):
    if not familia:
        return "A família está vazia."
    return "Pessoas na família: " + ", ".join(familia)

# Start the menu
menu()"""

      
"""#Ex 1 gpt
def menu():
    lista = []  # Define lista here
    while True:
        print("Digite os números que você deseja na lista! (Digite 0 para sair)")
        numeros = int(input("Número: "))
        if numeros == 0:
            print("Saindo")
            break  # Exit the loop
        else:
            lista.append(numeros)  # Append to lista

    print("Lista final:", lista)  # Print the final list
    print("Soma da lista:", soma(lista))  # Call soma to calculate the sum

def soma(lista):
    if not lista:
        return 0
    else:
        return lista[0] + soma(lista[1:])  # Recursive sum

menu()  # Call the menu function to start the program"""
    
#Ex 2
lista = (["a","b", "c"])

def contaLista(lista):
    if not lista:
        return 0
    else:
        return lista[0] + contaLista(lista[1:])
        
        
 #Ex 3
dados = {
    "pessoa1": {"nome": "João"},
    "pessoa2": {
        "nome": "Carlos",
        "filhos": {
            "filho1": {"nome": "Maria"}
        }
    }
}

def buscaDicioario(dados):
    if not dados:
        return False
    elif 'Maria' in dados:
        return True
    else:
        return False
        
print(buscaDicioario(dados))