from FakeDB import FakeDB

#GetPorData
fakeDB = FakeDB()
anoPesquisa = int(input("Informe ano desejado do contrato: "))

print(f'\nFuncionarios que fazem aniversario de contrato - em {anoPesquisa}')
for funcionario in fakeDB.Funcionarios:
    if funcionario.getDataCadastro().year == anoPesquisa:
        print(f'Nome: {funcionario.getNome()} / data: {funcionario.getDataCadastro()}')