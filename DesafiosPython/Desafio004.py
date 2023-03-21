numero = int(input('Digite um número inteiro'))

print("Tabuada de", numero)

for i in range(1, 11):
    resultado = numero * 1
    print(f'{numero},x,{i},=,{resultado}')
