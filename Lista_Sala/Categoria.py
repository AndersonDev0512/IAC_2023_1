from datetime import date


class Categoria:

    codigo = 0
    descricao = ''
    status = False
    dataInclusao = date.today()

    def __init__(self):
        self.codigo = 0
        self.descricao = ''
        self.status = False
        self.dataInclusao = date.today()

    def tostring(self):
        print(f'Codigo = {self.codigo} | ', end='')
        print(f'Descricao = {self.descricao} | ', end='')
        print(f'Status = {self.status} | ', end='')
        print(f'Data de Inclusão = {self.dataInclusao} ')
