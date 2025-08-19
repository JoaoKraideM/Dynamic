#Recursivamente
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)
    
    
print(fatorial(1))


#Exercicio 1 
def soma(n):
    # N não é menor, não vai parar
    if n < 0:
        return "Não aceitamos números negativos"
    #
    elif n == 0:
        return 0
    else:
        return n + soma(n-1)
    
    
print(soma(5))

#Exercicio 2
def mdc(x,y):
    if x >= y and x % y == 0:
        return y
    elif x < y:
        return mdc(y,x)
    else:
        return mdc(y, x % y)
    
    
print(mdc(10,20))

#Exercicio 3
def fat(a, b):
    if b == 0:
        return 1
    else:
        return a * fat(a, b -1)
    
print(fat(10,2))

#Exercicio 4
def busca_recursiva(lista, item):
    # Caso base: lista vazia → não encontrou
    if not lista:
        return False
    
    # Caso base: o primeiro elemento é o item procurado
    if lista[0] == item:
        return True
    
    # Passo recursivo: chama a função com o resto da lista
    return busca_recursiva(lista[1:], item)


# Exemplo de uso
numeros = [10, 20, 30, 40, 50]

print(busca_recursiva(numeros, 30))  # True


#Exercicio 5:
def contar_ocorrencias(lista, n):
    # Caso base: lista vazia → não há ocorrências
    if not lista:
        return 0
    
    # Verifica se o primeiro elemento é igual a N
    if lista[0] == n:
        return 1 + contar_ocorrencias(lista[1:], n)
    else:
        return contar_ocorrencias(lista[1:], n)


# Exemplo de uso
numeros = [1, 2, 3, 2, 4, 2, 5]

print(contar_ocorrencias(numeros, 2))  # 3

      