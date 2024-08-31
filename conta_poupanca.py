from conta import Conta

class ContaPoupanca(Conta):
    TAXA_PIX = 0.10

    def __init__(self, titular: str, numero: int, saldo: float = 0):
        super().__init__(titular, numero, 'Poupança', saldo)

    def calcular_valor_pix(self, valor: float) -> float:
        return valor * (1 + self.TAXA_PIX)

    def fazer_pix(self, valor: float) -> float:
        if valor <= 0:
            raise ValueError("O valor do PIX deve ser positivo.")
        valor_total = self.calcular_valor_pix(valor)
        if valor_total > self.saldo:
            raise ValueError("Saldo insuficiente para realizar a transação.")
        self.saldo -= valor_total
        return self.saldo