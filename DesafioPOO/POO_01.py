#Crie um programa que liste os funcionários pelo nome, utilizando as 3
#primeiras letras do nome, informadas pelo usuário. Por exemplo, procure todos os
#funcionários cujo nome comece com as letras MAR.

from FakeDB import FakeDB

#GetAll
fakeDB = FakeDB()
letrasNome = input("Digite as 3 primeiras letras no Nome do Funcionario").lower()

for funcionario in fakeDB.Funcionarios:
    if funcionario.getNome().lower().startswith(letrasNome):
        print(f'{funcionario.getNome()}')