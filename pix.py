from conta import Conta
class Pix(Conta):
    chaves_pix = []

    def __init__(self):
        self.chave_pix = None

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
            return self.chaves_pix

        if opcao in [1, 2, 3, 4]:
            print(f'Chave cadastrada com sucesso: {self.chave_pix}')
            self.chaves_pix.append(self.chave_pix)

    def get_chave_pix(self):
        return self.chave_pix
