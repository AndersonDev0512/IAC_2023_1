#Desenvolva um método que calcule o consumo de combustível, ou seja a
#quantidade de litros consumidos em uma viagem de veículo.

def calcular_consumo():
    distancia = float(input('Digite a distância em Km: '))
    consumo_por_litro = float(input('Digite o consumo do seu veiculo por litro: '))
    consumo = distancia / consumo_por_litro
    print(f'o Consumo de combustivel é: {consumo} km por litro')

calcular_consumo()