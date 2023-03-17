def nomes ():
    valor = input('Digite seu nome: ')

    qtdeLetras = valor.replace(' ','').count()

    qtdePrimeiroNome = len(valor.split()[0])
    print(f'Seu nome maisculo {valor.upper()}\n'
          f'Seu nome minusculo {valor.lower()}\n'
          f'Quantidade de letras {qtdeLetras}\n'
          f'quantidade de letras do primeiro nome:\n'
          f'{qtdePrimeiroNome}')
nomes()