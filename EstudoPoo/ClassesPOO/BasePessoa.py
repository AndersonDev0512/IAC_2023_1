class BasePessoa:
    def def__init__(self, nome ,dataNasc):
        self._nome = nome
        self._dataNasc = dataNasc
@property
##@abstractmethod / é uma assinatura da classe? porém da warning quando roda
def nome(self):
    pass

@nome.setter
def nome(self, novo_nome):
    pass

@property
##@abstractmethod / é uma assinatura da classe? porém da warning quando roda
def dataNasc(self):
    pass
@dataNasc.setter
##@abstractmethod / é uma assinatura da classe? porém da warning quando roda
def Data(self,nova_dataNasc):
    pass
