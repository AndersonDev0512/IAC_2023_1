nomes = ['João', 'Maria', 'Pedro', 'Lucas', 'Ana', 'Márcia', 'Felipe', 'Fernanda', 'José', 'Carlos']
idades = []
for nome in nomes:
    idade = int(input(f"Digite a idade de {nome}: "))
    idades.append(idade)
mais_de_18 = 0
for idade in idades:
    if idade > 18:
        mais_de_18 += 1
print(f"Das {len(nomes)} pessoas, {mais_de_18} possuem mais de 18 anos.")
