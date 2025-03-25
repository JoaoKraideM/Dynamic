# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 17:18:02 2025

@author: João
"""
numeros = []
def menu(lista):
    while True:
        numeros = int(input("Digite os numeros (para sair digite 0): "))
        if (numeros == 0):
            break
        else:
            lista.append(numeros)
    while True:
        escolha = input(f"1 - soma dos numeros na lista \n2 - Maior numero da lista \n3 - Menor numero da lista \n4 - Media da lista \nDigite a escolha que você deseja(digite Sair caso deseja para o processo): ")
        if (escolha == "Sair"):
            print("Saindo...")
            break
    
        elif (escolha == "1"):
            print(somaLista(lista))
    
        elif(escolha == "2"):
            print(maiorNumero(lista))
    
        elif(escolha == "3"):
            print(menorNumero(lista))
    
        elif(escolha == "4"):
            print(media(lista))
    
        else:
            print("Por favor insira um número valido!")


def somaLista(lista): 
    soma = sum(lista)
    print(f"{soma} é a soma dos números da lista!")        

def maiorNumero(lista):
    for i in range(len(lista)):
        if i == 0:
            maior = lista[i]
        elif lista[i] > maior:
            maior = lista[i]
    
    print(f"Esse {maior} é o maior numero da lista!")
    
def menorNumero(lista):
    for i in range(len(lista)):
        if i == 0:
            menor = lista[i]
        elif lista[i] < menor:
            menor = lista[i]
    
    print(f"Esse {menor} é o menor numero da lista!")
        
def media(lista):
    soma = 0
    for i in range(len(lista)):
        i = lista[i]
        soma = soma + i
    
    media = soma/len(lista)
    print(f"{media} é a media da lista!")
    
    
print(menu(numeros))