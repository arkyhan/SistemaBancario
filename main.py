import os
import time
from conta_corrente import Conta_corrente
from conta_poupanca import Conta_poupanca

contas = []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("Pressione Enter para continuar...")

def menu():
    executando = True
    while executando:
        limpar_tela()
        print('1 - Criar contas')
        print('2 - Exibir contas')
        print('3 - Cadastrar chave pix')
        print('4 - Exibir contas com chave pix')
        print('5 - Fazer PIX')
        print('6 - Sair')
        try:
            opcao = int(input('Digite a opção desejada: '))
            if opcao == 1:
                criar_contas()
            elif opcao == 2:
                exibir_contas()
            elif opcao == 3:
                cadastrar_chave_pix()
            elif opcao == 4:
                exibir_contas_com_pix()
            elif opcao == 5:
                fazer_pix()
            elif opcao == 6:
                executando = False
            else:
                print('Opção inválida. Por favor, escolha uma opção válida.')
        except ValueError:
            print('Erro: Por favor, digite um número válido.')
        pausar()

def criar_contas():
    tipo = input('Digite o tipo de conta (Corrente/Poupança): ').lower()
    titular = input('Digite o nome do titular: ')
    try:
        numero = int(input('Digite o número da conta: '))
        saldo = float(input('Digite o saldo inicial: '))
        
        if tipo == 'corrente':
            conta = Conta_corrente(titular, numero, saldo)
        elif tipo == 'poupança':
            conta = Conta_poupanca(titular, numero, saldo)
        else:
            print('Tipo de conta inválido.')
            return
        
        contas.append(conta)
        print('Conta criada com sucesso!')
    except ValueError:
        print('Erro: Por favor, digite valores numéricos válidos para o número da conta e saldo.')

def cadastrar_chave_pix():
    if not contas:
        print('Não há contas cadastradas.')
        return
    
    try:
        numero = int(input('Digite o número da conta: '))
        for conta in contas:
            if conta.numero == numero:
                conta.set_chave_pix()
                return
        print('Conta não encontrada.')
    except ValueError:
        print('Erro: Por favor, digite um número de conta válido.')

def exibir_contas():
    limpar_tela()
    for conta in contas:
        conta.exibir_dados()
        print('-' * 30)
    pausar()

def exibir_contas_com_pix():
    limpar_tela()
    for conta in contas:
        if conta.chave_pix:
            conta.exibir_dados()
            print('-' * 30)
    pausar()

def fazer_pix():
    if len(contas) < 2:
        print('É necessário ter pelo menos duas contas cadastradas para fazer um PIX.')
        return

    try:
        numero_origem = int(input('Digite o número da conta de origem: '))
        chave_pix_destino = input('Digite a chave PIX da conta de destino: ')
        valor = float(input('Digite o valor do PIX: '))

        conta_origem = None
        conta_destino = None

        for conta in contas:
            if conta.numero == numero_origem:
                conta_origem = conta
            elif conta.chave_pix == chave_pix_destino:
                conta_destino = conta

        if not conta_origem or not conta_destino:
            print('Conta de origem ou destino não encontrada.')
            return

        if isinstance(conta_origem, Conta_poupanca):
            valor_total = conta_origem.calcular_valor_pix(valor)
        else:
            valor_total = valor

        if conta_origem.saldo < valor_total:
            print('Saldo insuficiente na conta de origem.')
            return

        conta_origem.saldo -= valor_total
        conta_destino.saldo += valor

        print(f'PIX realizado com sucesso!')
        print(f'Valor transferido: R${valor:.2f}')
        if isinstance(conta_origem, Conta_poupanca):
            print(f'Juros aplicados: R${valor_total - valor:.2f}')
        print(f'Novo saldo da conta de origem: R${conta_origem.saldo:.2f}')
        print(f'Novo saldo da conta de destino: R${conta_destino.saldo:.2f}')

    except ValueError:
        print('Erro: Por favor, digite valores numéricos válidos.')

def main():
    try:
        menu()
    except KeyboardInterrupt:
        print('\nPrograma encerrado pelo usuário.')
    except Exception as e:
        print(f'Ocorreu um erro inesperado: {e}')

if __name__ == "__main__":
    main()
