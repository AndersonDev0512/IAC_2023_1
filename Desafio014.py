import random

nomes_lista = []
for i in range(4) :
    nome = input(f'Digite o nome do {i+1}º Aluno: ')
    nomes_lista.append(nome)
nome_sorteados = random.sample(nomes_lista, len(nomes_lista))
print(f'{nome_sorteados}')
