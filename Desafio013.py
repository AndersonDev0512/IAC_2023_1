import random
nomes = []

while True:
    nome = input("Digite o nome do aluno (ou 'fim para encerrar'): ")
    if nome == 'fim':
        break
    nomes.append(nome)

nome_ordenada = nomes.sort()
aluno_escolhido = random.choice(nomes)
print(f'O Aluno escolhido para apagar o quadro foi: {aluno_escolhido}')