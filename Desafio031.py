def verificar_numero():
    numero= input(print('Digite o número que você quer verificar'))
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")

    if numero % 2 == 0:
        print("O número é múltiplo de 2.")
    else:
        print("O número não é múltiplo de 2.")

    if numero % 3 == 0:
        print("O número é múltiplo de 3.")
    else:
        print("O número não é múltiplo de 3.")

    if numero % 5 == 0:
        print("O número é múltiplo de 5.")
    else:
        print("O número não é múltiplo de 5.")
verificar_numero()
