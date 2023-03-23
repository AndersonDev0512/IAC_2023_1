#Desenvolva um método que identifique o maior e o menor número dentre 5
#números fornecidos pelo usuário.

def identificar_maior_menor():
    numeros = []
    for i in range(5):
        numero = float(input('Digite um número: '))
        numeros.append(numero)
    maior = max(numeros)
    menor = min(numeros)
    print(f'O maior número é {maior} e o menor número é {menor}')

identificar_maior_menor()