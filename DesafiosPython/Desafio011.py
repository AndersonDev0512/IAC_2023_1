nomes = []

while True:
    nome = input("Digite o nome do aluno (ou 'fim para encerrar'): ")
    if nome == 'fim':
        break
    nomes.append(nome)

print("Os Nomes dos alunos são:")
for nome in nomes:
    print(nome)