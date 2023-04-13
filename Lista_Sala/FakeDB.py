from datetime import date
from datetime import datetime
from Categoria import Categoria
from Subcategoria import Subcategoria
from Produto import Produto

import csv

class FakeDB:

    Categorias = []
    Subcategorias = []
    Produtos = []

    def AutoFillCategorias(self):
        with open('categorias.txt') as csvfile:
            linereader = csv.reader(csvfile, delimiter=',')
            for row in linereader:
                obj = Categoria()
                obj.codigo = int(row[0])
                obj.descricao = row[1]
                if row[2] == 0:
                    obj.status = False
                else:
                    obj.status = True
                obj.dataInclusao = datetime.strptime(row[3], '%Y-%m-%d').date()
                self.Categorias.append(obj)

    def AutoFillSubcategorias(self):
        with open('subcategorias.txt') as csvfile:
            linereader = csv.reader(csvfile, delimiter=';')
            for row in linereader:
                obj = Subcategoria()
                obj.codigo = int(row[0])
                obj.codigoCategoria = int(row[1])
                obj.descricao = row[2]
                if row[3] == 0:
                    obj.status = False
                else:
                    obj.status = True
                obj.dataInclusao = datetime.strptime(row[4], '%Y-%m-%d').date()
                self.Subcategorias.append(obj)


    def AutoFillProdutos(self):
        with open('produtos.txt') as csvfile:
            linereader = csv.reader(csvfile, delimiter=';')
            for row in linereader:
                obj = Produto()
                obj.codigo = int(row[0])
                obj.codigoCategoria = int(row[1])
                obj.codigoSubcategoria = int(row[2])
                obj.descricao = row[3]
                if row[4] == 0:
                    obj.status = False
                else:
                    obj.status = True
                obj.dataInclusao = datetime.strptime(row[5], '%Y-%m-%d').date()
                self.Produtos.append(obj)


    def __init__(self):
        self.AutoFillCategorias()
        self.AutoFillSubcategorias()
        self.AutoFillProdutos()

