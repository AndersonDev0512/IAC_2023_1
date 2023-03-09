import random
nomes = []

while True:
    nome = input("Digite o nome do aluno (ou 'fim para encerrar'): ")
    if nome == 'fim':
        break
    nomes.append(nome)

nome_ordenada = nomes.sort()
print("Os Nomes dos alunos são:")
for nome in nomes:
    print(nome_ordenada)