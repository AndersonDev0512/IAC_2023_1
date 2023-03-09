def reajuste_salarial () :
    salario = float(input('Digite seu salário'))
    if salario <1700 :
        salario_novo = salario + 300
        print(f'Seu salário com reajuste é {salario_novo}')
    else:
        salario_novo = salario + 200
        print(f'Seu salário com reajuste é {salario_novo}')
print(reajuste_salarial())