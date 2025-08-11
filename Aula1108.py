#Ex 1 - Fatorial
#Exemplo da função recursiva
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

print(fatorial(5))

#Fatorial iteração
def fatorial_it(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

print(fatorial_it(5))


#Inverter string Iteração
def reverteString(Texto):
    invertida = ''
    for caractere in Texto:
        invertida = caractere + invertida

    print(invertida)

reverteString("Palavra")

#Inverter Recursão
def reverteStringRec(Texto):
    if len(Texto) <= 1:
        return Texto
    return reverteStringRec(Texto[1:]) + Texto[0]

print(reverteStringRec("Palavra"))