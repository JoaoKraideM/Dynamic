# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 19:35:25 2025

@author: labsfiap
"""

#Quick Sort

lista = [10, 80, 30,  90, 40, 50, 70]
def quick_sort(lista):
    if len(lista) <=1 :
        return lista

    pivo = lista[-1]
    #X passa como index na lista e faz alocação dos dados em respectivas listas, comparando com pivo:
    menores = [x for x in lista [:-1] if x <= pivo]
    maiores = [x for x in lista [:-1] if x > pivo]
    return quick_sort(menores) + [pivo] + quick_sort(maiores)

print(quick_sort(lista))

#Ex.1
lista = [1,2,3,4,5,6,7,8,9,10]

numeros = [x for x in lista if x % 2 == 0]
print(numeros)

#Ex.2

Lista = ['a','b','c','d', 'e']

numeros = (i for i, letra in enumerate(lista) if letra in ('b', 'c'))
print(numeros)

#Ex. 3 
lista = [1,2,3,4,5,6,7,8,9,10]
numeros = [x*2 for x in lista if x % 2 != 0]
print(numeros)

#Ex. 4 
lista = [4,8,2,9,1,7]
pivo = 5

resultado1 = [x for x in lista[:-1] if x <= pivo]
resultado2 = [x for x in lista[:-1] if x > pivo]

print(resultado1)
print(resultado2)