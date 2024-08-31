from conta import Conta

class Conta_corrente(Conta):
    def __init__(self, titular, numero, saldo=0):
        super().__init__(titular, numero, 'Corrente', saldo)