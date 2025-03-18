"""
Aula 4 - Dynammic Programming

Ex 1 - Busca Binária (while)


def busca_binaria(lista, alvo):
    #igual a fazer l  = 0, h = len(lista) - 1
    l, h = 0, len(lista) - 1
    iteracao = 0
    
    while l <= h:
        
        iteracao += 1
        m = (l + h) // 2
        print(f"iteração {iteracao}: l{l}, h{h}, m{m}")
        
        if lista[m] == alvo:
            return m
        elif lista[m] < alvo:
            l = m + 1
        else:
            h = m - 1
            
    return -1


lista_teste = [11, 17, 18, 45, 50, 71, 95]
alvo = 50

resultado = busca_binaria(lista_teste, alvo)
print(resultado)
"""

"""
Ex 2 - Busca Binária (for)

def busca_binaria(lista, alvo):
    #igual a fazer l  = 0, h = len(lista) - 1
    l, h = 0, len(lista) - 1
    
    for iteracao in range(len(lista)):
     
        m = (l + h) // 2
        print (f"iteração {iteracao+1}: l{l}, h{h}, m{m}")
        
        if lista[m] == alvo:
            return m
        elif lista[m] < alvo:
            l = m + 1
        else:
            h = m - 1
            
    return -1

lista_teste = [11, 17, 18, 45, 50, 71, 95]
alvo = 50

resultado = busca_binaria(lista_teste, alvo)
print(resultado)

"""

"""
Ex 3  

fila = ['Cliente 1','Cliente 2', 'Cliente 3' ]
print(fila)

cliente = fila.pop(0)
print(fila)
print(cliente)

cliente = fila.pop(0)
print(fila)

"""

"""
Ex 4


fila = []
fila.append('Cliente 1')
fila.append('Cliente 2')
fila.append('Cliente 3')

print(fila)

cliente = fila.pop(0)
print(fila)
"""

"""
Ex 5


fila = ['cliente 1', 'cliente 2', 'cliente 3' ]
while fila:
    cliente = fila.pop(0)
    print(cliente)
"""

"""
Ex 6

fila = ['cliente 1', 'cliente 2', 'cliente 3' ]
i = 0
for i in range(len(fila)):
    cliente = fila.pop(0)
    print(cliente)
"""    

"""
Ex 7
"""
fila_clientes = []

while True:
    cliente = input("Digie o nome do cliente (ou fim para sair)")
    if cliente.lower() == 'fim':
        break
    fila_clientes.append(cliente)
    print(fila_clientes)
 
while fila_clientes:
    atendido = fila_clientes.pop()
    print(f"atendendo: {atendido}")
    print("Todos clientes foram atendidos")
            
            
