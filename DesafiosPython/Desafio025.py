#Desenvolva um método que calcule o quadrado da diferença entre dois
#números quaisquer. Para tanto, pesquise como funciona os métodos matemáticos em
#Python.
def calcular_quadrado_da_diferenca():
    numero1 = float(input('Digite o 1º Número: '))
    numero2 = float(input('Digite o 2º Número: '))
    quadrado_da_diferenca = (numero1 - numero2) ** 2
    print(f'O quadrado da diferença é: {quadrado_da_diferenca}')

calcular_quadrado_da_diferenca()