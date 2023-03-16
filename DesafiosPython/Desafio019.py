def verifica_idade ():
    idade = int(input('Digite sua idade:'))
    if idade <18:
        print('\033[31mSem Permissão\033[0m')
    else:
        print('\033[32mPermissão Concedida\033[0m')
print(verifica_idade())