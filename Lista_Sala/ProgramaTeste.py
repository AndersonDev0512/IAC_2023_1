from FakeDB import FakeDB
from Categoria import Categoria
from Subcategoria import Subcategoria
from Produto import Produto


fakeDB = FakeDB()

for prod in fakeDB.Produtos:
    prod.tostring()