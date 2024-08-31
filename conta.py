class Conta:

    contas = []
    def __init__(self, titular, numero, tipo_conta, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self.numero = numero
        self.tipo_conta = tipo_conta
        self.chave_pix = None

    def adicionar_saldo(self):
        valor = float(input('Digite o valor a depositar: '))
        self.saldo += valor
        return self.saldo
    

    def fazer_pix(self):
        valor = float(input('Digite o valor da transação: '))
        if valor < self.saldo:
            self.saldo -= valor
            return self.saldo
        else:
            print('O valor solicitado é maior que o saldo em conta')

    def exibir_dados(self):
        chave_pix = self.get_chave_pix() if hasattr(self, 'get_chave_pix') else None
        print(f'Titular: {self.titular:<20} '
              f'Numero: {self.numero:<10} '
              f'Tipo da Conta: {self.tipo_conta:<15} '
              f'Saldo: {self.saldo:<10.2f} '
              f'Chave pix: {chave_pix}')

    def set_chave_pix(self):
        print('Digite a opção de chave que deseja cadastrar')
        print('1 - CPF')
        print('2 - Email')
        print('3 - Celular')
        print('4 - Aleatório')
        opcao = int(input('Digite a opção desejada: '))
        if opcao == 1:
            self.chave_pix = input('Digite o CPF: ')
        elif opcao == 2:
            self.chave_pix = input('Digite o Email: ')
        elif opcao == 3:
            self.chave_pix = input('Digite o Celular: ')
        elif opcao == 4:
            self.chave_pix = input('Digite a chave aleatória: ')
        else:
            print('Opção inválida')
            return

        if opcao in [1, 2, 3, 4]:
            print(f'Chave cadastrada com sucesso: {self.chave_pix}')

    def get_chave_pix(self):
        return self.chave_pix
