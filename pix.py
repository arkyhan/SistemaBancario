import uuid
from typing import List, Optional

class Pix:
    def __init__(self):
        self._chaves_pix: List[str] = []

    def gerar_chave_aleatoria(self) -> str:
        return str(uuid.uuid4())

    def validar_chave(self, chave: str, tipo: str) -> bool:
        # Implementar validações específicas para cada tipo de chave
        if tipo == 'CPF':
            return len(chave) == 11 and chave.isdigit()
        elif tipo == 'Email':
            return '@' in chave and '.' in chave
        elif tipo == 'Celular':
            return len(chave) == 11 and chave.isdigit()
        elif tipo == 'Aleatoria':
            return len(chave) == 36 and '-' in chave
        return False

    def cadastrar_chave(self, tipo: str, valor: Optional[str] = None) -> str:
        if tipo not in ['CPF', 'Email', 'Celular', 'Aleatoria']:
            raise ValueError("Tipo de chave PIX inválido.")

        if tipo == 'Aleatoria':
            chave = self.gerar_chave_aleatoria()
        elif valor is None:
            raise ValueError("Valor da chave PIX não fornecido.")
        else:
            chave = valor

        if not self.validar_chave(chave, tipo):
            raise ValueError("Chave PIX inválida.")

        if chave in self._chaves_pix:
            raise ValueError("Esta chave PIX já está cadastrada.")

        self._chaves_pix.append(chave)
        return chave

    def remover_chave(self, chave: str) -> None:
        if chave not in self._chaves_pix:
            raise ValueError("Chave PIX não encontrada.")
        self._chaves_pix.remove(chave)

    @property
    def chaves_pix(self) -> List[str]:
        return self._chaves_pix.copy()
