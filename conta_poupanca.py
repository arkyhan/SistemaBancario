from conta import Conta

class Conta_poupanca(Conta):
    def __init__(self, titular, numero, saldo=0):
        super().__init__(titular, numero, 'Poupança', saldo)

    def calcular_valor_pix(self, valor):
        juros = valor * 0.10
        return valor + juros

    def fazer_pix(self):
        valor = float(input('Digite o valor da transação: '))
        valor_total = self.calcular_valor_pix(valor)
        if valor_total <= self.saldo:
            self.saldo -= valor_total
            print(f'Transação realizada. Valor: R${valor:.2f}, Juros: R${valor_total - valor:.2f}')
        else:
            print('Saldo insuficiente para realizar a transação.')