#Desenvolva um método que calcule o volume de uma esfera. Para tanto,
#pesquise como calcular o volume de uma esfera.
def calcular_volume_esfera() :
    raio = float(input('Digite o Raio da esfera: '))
    volume = (4/3) * 3.14159 * raio **3
    print(f'o Volume da esfera é: {volume}')

calcular_volume_esfera()