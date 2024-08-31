from abc import ABC, abstractmethod
from typing import Optional
import uuid

class Conta(ABC):
    def __init__(self, titular: str, numero: int, tipo_conta: str, saldo: float = 0):
        self.titular: str = titular
        self.saldo: float = saldo
        self.numero: int = numero
        self.tipo_conta: str = tipo_conta
        self._chave_pix: Optional[str] = None

    def adicionar_saldo(self, valor: float) -> float:
        """Adiciona saldo à conta."""
        if valor <= 0:
            raise ValueError("O valor a ser depositado deve ser positivo.")
        self.saldo += valor
        return self.saldo

    @abstractmethod
    def fazer_pix(self, valor: float) -> float:
        """Método abstrato para realizar um PIX."""
        pass

    def exibir_dados(self) -> None:
        """Exibe os dados da conta."""
        print(f'Titular: {self.titular:<20} '
              f'Numero: {self.numero:<10} '
              f'Tipo da Conta: {self.tipo_conta:<15} '
              f'Saldo: R${self.saldo:<10.2f} '
              f'Chave PIX: {self.chave_pix}')

    def set_chave_pix(self, chave: str) -> None:
        """Define a chave PIX da conta."""
        self._chave_pix = chave
        print(f'Chave PIX cadastrada com sucesso: {self._chave_pix}')

    @property
    def chave_pix(self) -> Optional[str]:
        """Retorna a chave PIX da conta."""
        return self._chave_pix
