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
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def par(lista):
    if not lista:
        return 0
    else:
        if lista[0] % 2 == 0:
            return lista[0] + par(lista[1:])
        else:
            return par(lista[1:])

print(par(lista))


#ex 3
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
       


#ex 4
#Exercicio que procura em arquivos json (Dicionarios) os nomes dos membros da familia
familia = {
    'nome': 'Roberto Souza',
    'filhos': [
        {
            'nome': 'Fernanda Souza',
            'filhos': [
                {'nome': 'Isabela Souza'},
                {'nome': 'Mateus Souza'}
        }
    ]
}

def PessoasFamilia(dicionario):
    nomes = []  # Lista para armazenar os nomes

    if 'nome' in dicionario:
        nomes.append(dicionario['nome'])  # Adiciona o nome da pessoa à lista

    # Caso a pessoa tenha filhos, fazemos a recursão
    if 'filhos' in dicionario and dicionario['filhos']:
        # Chama a função recursivamente para o primeiro filho
        primeiro_filho = dicionario['filhos'][0]
        nomes.extend(PessoasFamilia(primeiro_filho))  # Chamada recursiva para o primeiro filho

        # Depois, chamamos a função recursivamente para o próximo filho, sem usar 'for'
        if len(dicionario['filhos']) > 1:
            # Chama para os filhos restantes (sem o primeiro)
            filhos_restantes = dicionario['filhos'][1:]
            nomes.extend(PessoasFamilia({'filhos': filhos_restantes}))  # Chama para o restante dos filhos
            
            
 #Ex 5
 while True:
     print(menu())
     
     
def menu():
    print("===MENU===")
    print("1 - Cadastrar nome")
    print("2 - Listar pessoas")
    print("3 - Buscar um nome")
    print("4 - Sair do programa")
    
    escolha = int(input("Digite qual programa deseja entrar: "))
    if escolha == 1:
        print(cadastraPessoa(familia))
    elif escolha == 2:
        print(PessoasFamilia(familia))
    elif escolha == 3:
        print(buscaNome(familia))
    elif escolha == 4:
        print(deletaNome)
    elif escolha == 5:
        print("Saindo...")
        break
    else:
        print("escolha inválida")
        
 
 def cadastraPessoa(familia):
     nome = input("Digite o nome da pessoa que deseja cadastrar: ")
     familia.append(nome)
     print(f"{nome}Pessoa cadastrada com sucesso")


def buscaNome(familia):
    busca = input("Digite o nome que deseja achar: ").strip()
    if busca in familia:
        print(f"{busca} está na familia")
    else:
        print(f"{busca} não foi encontrado na familia")
        
        
def deletaNome(familia):
    nome = input("Digite o nome que deseja achar: ").strip()
    if nome in familia:
        familia.remove(nome)
    else:
        print(f"{nome} não foi encontrado na familia")
      
#Ex 1 gpt
lista = ()

while True:
    def menu()


def menu():
    print("Digite os números que você deseja na lista! (Digite 0 para sair)")
    numeros = int(input("Números: "))
    if numeros == 0:
        print("Saindo")
        break
    else:
        numeros.append(lista)

def soma(lista):
    if not lista:
        return 0
    else:
        return lista[0] + soma(lista[1:])
        
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

def buscaDicioario(dados, busca):
    if not dados:
        return False
    elif 'busca'in dados:
        return True
    else:
        return False
        
#Ex 5
dados = {
    "nome": "Ana",
    "endereco": {
        "rua": "X",
        "cidade": "Y"
    },
    "profissao": "Dev"
}

def percorre(dados):
    if not dados:
        return none
    elif [none]