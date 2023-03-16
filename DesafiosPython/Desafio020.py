def troca_nome ():
    nome_entrada = input('Digite uma frase: ')
    nome_nova = nome_entrada.replace('A','&').replace('a','&')
    print("Nova frase ", nome_nova)
print(troca_nome())