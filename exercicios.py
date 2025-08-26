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
    inicio = 0
    fim = len(lista) - 1
    if inicio <= fim:
        return lista[]
