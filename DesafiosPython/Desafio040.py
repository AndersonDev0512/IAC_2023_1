
nomes = ['João', 'Maria', 'Pedro', 'Lucas', 'Ana', 'Márcia', 'Felipe', 'Fernanda', 'José', 'Carlos']

alturas = []
matriculas = []

def solicitarAltura():

    for i in nomes:

        altura = float(input(f'Digite a altura do {i}'))
        alturas.append(altura)

        matricula = int(input(f'Digite a altura do {i}'))
        matriculas.append(matricula)

    if max(alturas):
        alt = max(alturas)
        index = alturas.index(alt)
        print(f'O Aluno mais alto tem {max(alturas)} matricula: {matriculas[index]}')

    if min(alturas):
        alt = max(alturas)
        index = alturas.index(alt)
        print(f'O Aluno mais alto tem {min(alturas)} matricula: {matriculas[index]}')


solicitarAltura()
