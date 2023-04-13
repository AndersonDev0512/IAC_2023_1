from datetime import date


class Produto:

    codigo = 0
    codigoCategoria = 0
    codigoSubcategoria = 0
    descricao = ''
    status = False
    dataInclusao = date.today()

    def __init__(self):
        self.codigo = 0
        self.codigoCategoria = 0
        self.codigoSubcategoria = 0
        self.descricao = ''
        self.status = False
        self.dataInclusao = date.today()

    def tostring(self):
        print(f'Codigo = {self.codigo} | ', end='')
        print(f'CodigoCategoria = {self.codigoCategoria} | ', end='')
        print(f'CodigoSubcategoria = {self.codigoSubcategoria} | ', end='')
        print(f'Descricao = {self.descricao} | ', end='')
        print(f'Status = {self.status} | ', end='')
        print(f'Data de Inclusão = {self.dataInclusao} ')
