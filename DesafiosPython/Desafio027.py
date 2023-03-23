#Desenvolva um método que leia dois números reais e efetue as quatro
#operações entre eles.
def operacoes_basicas():
    numero1 = float(input('Digite o 1º Número: '))
    numero2 = float(input('Digite o 2º Número: '))
    soma = numero1 + numero2
    subtracao = numero1 - numero2
    multiplicacao = numero1 * numero2
    divisao = numero1 / numero2
    resultado =[soma,subtracao,multiplicacao,divisao]
    print("Soma: ", resultado[0])
    print("Subtração: ", resultado[1])
    print("Multiplicação: ", resultado[2])
    print("Divisão: ", resultado[3])

operacoes_basicas()
