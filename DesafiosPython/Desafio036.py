nomes = ['João', 'Maria', 'Pedro', 'Lucas', 'Ana', 'Márcia', 'Felipe', 'Fernanda', 'José', 'Carlos']
idades = []
nacionalidades = []
aptos = 0

for nome in nomes:
    idade = int(input(f"Digite a idade de {nome}: "))
    nacionalidade = input(f"Informe a nacionalidade de {nome}: ")
    idades.append(idade)
    nacionalidades.append(nacionalidade)

    if idade > 16 and nacionalidade.lower() == 'brasil':
        aptos += 1
        print(f'{nome} pode votar!')
    else:
        print(f'{nome} não pode votar.')

print(f'Total de pessoas aptas a votar: {aptos}')