from FakeDB import FakeDB

#GetAll
fakeDB = FakeDB()
mesdesejado = input("Digite O MÊS Desejado").lower()

for funcionario in fakeDB.Funcionarios:
    if funcionario.getDataCadastro().month() == mesdesejado:
        print(f'{funcionario.getNome()} || {funcionario.getDataCadastro()}')