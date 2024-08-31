from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, titular: str, numero: int, saldo: float = 0):
        super().__init__(titular, numero, 'Corrente', saldo)

    def fazer_pix(self, valor: float) -> float:
        """Realiza um PIX de uma conta corrente."""
        if valor <= 0:
            raise ValueError("O valor do PIX deve ser positivo.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente para realizar a transação.")
        self.saldo -= valor
        return self.saldo