def calcula_volume_cilindro():
    raio = float(input('Digite o Raio do cilindro : '))
    altura = float(input('Digite a altura do cilindro: '))
    area_base = 3.14159 * raio ** 2
    volume = area_base * altura
    print(f'O Volume de um cilindro é: {volume}')
calcula_volume_cilindro()
