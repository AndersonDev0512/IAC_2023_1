def imprimir_multiplos_de_tres():
    for numero in range(1, 101):
        if numero % 3 == 0:
            print(f'o multiplo de 3 é: {numero}')
imprimir_multiplos_de_tres()