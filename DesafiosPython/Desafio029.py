#Desenvolva um método que calcule o valor de uma prestação em atraso,
#baseado em uma taxa de juros informada pelo usuário.

def calcular_juros_prestacao():
    valor_original = float(input('Digite o valor original da prestação: '))
    taxa_juros = float(input('Digite a taxa de juros: '))
    dias_em_atraso = int(input('Digite o dias de atraso da prestação'))
    valor_atualizado = valor_original + (valor_original * taxa_juros * dias_em_atraso / 30)
    print(f'o valor atualizado é: {valor_atualizado}')
calcular_juros_prestacao()