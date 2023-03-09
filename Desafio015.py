import random

lista_alunos = []

while True:
    nome_aluno = input('Digite o nome do Aluno: "para sair digite fim" ')
    if nome_aluno == 'fim':
        break
    lista_alunos.append(nome_aluno)
sorteio_embaralhado = random.choice(lista_alunos)
sorteio_ordem = random.sample(lista_alunos, len(lista_alunos))
print(sorteio_ordem)



