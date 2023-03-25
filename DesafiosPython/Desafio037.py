# Utilizando uma lista de nomes de funcionários previamente carregada,
# desenvolva um método que solicite o salário de cada um, e armazene em uma lista
# paralela. Em seguida, calcule e exiba o salário reajustado, de acordo com a seguinte
# regra: Salário até R$ 300,00, reajuste de 50%; Salários maiores que R$ 300,00, reajuste de
# 30%.


nomes = ['João', 'Maria', 'Pedro', 'Lucas', 'Ana', 'Márcia', 'Felipe', 'Fernanda', 'José', 'Carlos']
salarios = []

def solicitaSalario():
    for i in nomes:
        salario = float (input (f'Digite o salário do {i}: '))
        if salario <= 300:
            reajuste = 0.5
        else:
            reajuste = 0.3
        novoSalario = salario + (salario * reajuste)
        salarios.append (novoSalario)
        print (f'Seu novo salário é R${novoSalario :.2f}')

solicitaSalario()