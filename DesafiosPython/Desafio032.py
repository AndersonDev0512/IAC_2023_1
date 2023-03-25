alunos = ["Ana", "Beatriz", "Carlos", "Daniel", "Eduarda", "Fabiana", "Gabriel", "Hugo", "Isabela", "João",
          "Karina", "Lucas", "Maria", "Natália", "Otávio", "Paula", "Rafael", "Sofia", "Thiago", "Vitor"]
idades = []
for aluno in alunos:
    idade = int(input(f"Qual a idade do(a) aluno(a) {aluno}? "))
    idades.append(idade)
idade_media = sum(idades) / len(idades)
print(f"A idade média da turma é {idade_media:.2f} anos.")
