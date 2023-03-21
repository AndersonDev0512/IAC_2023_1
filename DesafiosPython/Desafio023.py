def calcular_volume_cda():
    comprimento = float(input('Digite o comprimento: '))
    largura = float(input('Digite a Largura: '))
    altura = float(input('Digite a altura: '))
    area_base = comprimento * largura
    volume = area_base * altura
    print(f"o Volume da caixa d'água é: {volume}")
calcular_volume_cda()
