from collections import deque
import networkx as nx
import matplotlib as plt

grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
    }


def busca_profundidade(grafo, inicio, visitados=None):
    if visitados is None:
        visitados = set()
    
    visitados.add(inicio)
    print(inicio, end=" ")
        
    for vizinho in grafo[inicio]:
        if vizinho not in visitados:
            busca_profundidade(grafo,vizinho,visitados)
                
print("DFS a partir do nó A:",)
busca_profundidade(grafo, 'A')
print(f"\n")


def busca_largura(grafo, inicio):
    visitados = set()
    fila = deque([inicio])
    
    while fila:
        no = fila.popleft()
        if no not in visitados:
            print(no, end=" ")
            visitados.add(no)
            fila.extend(grafo[no])

print("Procura por largura no nó A: ")            
busca_largura(grafo, 'A')


#criar grafo
G1 = nx.Graph()
arestas1 =[
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('B', 'C', 1),
    ('B', 'D', 5),
    ('C', 'D', 8),
    ('C', 'E', 10),
    ('D', 'E', 2),
    ('D', 'F', 6),
    ('E', 'F', 2)
]

G1.add_weighted_edges_from(arestas1)

caminho1 = nx.dijkstra_path(G1, source='A', target='F')
distancia1 = nx.dijkstra_path_length(G1, source='A', target='F')

print("Caminho mais curto de A até F:", "->".join(caminho1))
print("Distância total:", distancia1, "Km")