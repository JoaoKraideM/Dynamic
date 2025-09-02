import json

def exibe_nomes(dicionario):
    if 'filhos' not  in dicionario:
        print(dicionario['nome'])
        return
    else:
        for c, v in dicionario.items():
            print(c)
        print(dicionario['nome'])
        for dic in dicionario['filhos']:
            exibe_nomes(dic)

arquivo = input("nome do arquivo: ")
with open(arquivo + '.json', 'r') as file:
    dicionario = json.load(file)
    exibe_nomes(dicionario)