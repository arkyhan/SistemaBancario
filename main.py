import os
from typing import List, Union
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca
from pix import Pix

contas: List[Union[ContaCorrente, ContaPoupanca]] = []
pix_manager = Pix()

def limpar_tela() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar() -> None:
    input("Pressione Enter para continuar...")

def menu() -> None:
    opcoes = {
        1: criar_contas,
        2: exibir_contas,
        3: cadastrar_chave_pix,
        4: exibir_contas_com_pix,
        5: fazer_pix,
        6: lambda: print("Programa encerrado.")
    }
    
    while True:
        limpar_tela()
        print('\n'.join(f'{k} - {v.__name__.replace("_", " ").capitalize()}' for k, v in opcoes.items()))
        try:
            opcao = int(input('Digite a opção desejada: '))
            if opcao in opcoes:
                if opcao == 6:
                    opcoes[opcao]()
                    break
                opcoes[opcao]()
            else:
                print('Opção inválida. Por favor, escolha uma opção válida.')
        except ValueError:
            print('Erro: Por favor, digite um número válido.')
        pausar()

def criar_contas() -> None:
    tipo = input('Digite o tipo de conta (Corrente/Poupança): ').lower()
    titular = input('Digite o nome do titular: ')
    try:
        numero = int(input('Digite o número da conta: '))
        saldo = float(input('Digite o saldo inicial: '))
        
        conta_classes = {'corrente': ContaCorrente, 'poupança': ContaPoupanca}
        if tipo in conta_classes:
            conta = conta_classes[tipo](titular, numero, saldo)
            contas.append(conta)
            print('Conta criada com sucesso!')
        else:
            print('Tipo de conta inválido.')
    except ValueError:
        print('Erro: Por favor, digite valores numéricos válidos para o número da conta e saldo.')

def cadastrar_chave_pix() -> None:
    if not contas:
        print('Não há contas cadastradas.')
        return
    
    try:
        numero = int(input('Digite o número da conta: '))
        conta = next((c for c in contas if c.numero == numero), None)
        if conta is None:
            print('Conta não encontrada.')
            return

        opcoes_chave = {1: 'CPF', 2: 'Email', 3: 'Celular', 4: 'Aleatoria'}
        print('\n'.join(f'{k} - {v}' for k, v in opcoes_chave.items()))
        opcao = int(input('Digite a opção desejada: '))
        
        if opcao not in opcoes_chave:
            print('Opção inválida')
            return

        tipo_chave = opcoes_chave[opcao]
        valor = input(f'Digite o {tipo_chave}: ') if opcao != 4 else None
        chave = pix_manager.cadastrar_chave(tipo_chave, valor)
        conta.set_chave_pix(chave)
    except ValueError:
        print('Erro: Por favor, digite valores válidos.')

def exibir_contas() -> None:
    limpar_tela()
    if not contas:
        print('Não há contas cadastradas.')
    else:
        for conta in contas:
            conta.exibir_dados()
            print('-' * 30)

def exibir_contas_com_pix() -> None:
    limpar_tela()
    contas_com_pix = [conta for conta in contas if conta.chave_pix]
    if not contas_com_pix:
        print('Não há contas com chave PIX cadastrada.')
    else:
        for conta in contas_com_pix:
            conta.exibir_dados()
            print('-' * 30)

def fazer_pix() -> None:
    if len(contas) < 2:
        print('É necessário ter pelo menos duas contas cadastradas para fazer um PIX.')
        return

    try:
        numero_origem = int(input('Digite o número da conta de origem: '))
        chave_pix_destino = input('Digite a chave PIX da conta de destino: ')
        valor = float(input('Digite o valor do PIX: '))

        conta_origem = next((c for c in contas if c.numero == numero_origem), None)
        conta_destino = next((c for c in contas if c.chave_pix == chave_pix_destino), None)

        if not conta_origem or not conta_destino:
            print('Conta de origem ou destino não encontrada.')
            return

        if conta_origem == conta_destino:
            print('Não é possível fazer um PIX para a própria conta.')
            return

        if conta_origem.saldo < valor:
            print('Saldo insuficiente na conta de origem.')
            return

        conta_origem.fazer_pix(valor)
        conta_destino.adicionar_saldo(valor)

        print(f'PIX realizado com sucesso!')
        print(f'Valor transferido: R${valor:.2f}')
        print(f'Novo saldo da conta de origem: R${conta_origem.saldo:.2f}')
        print(f'Novo saldo da conta de destino: R${conta_destino.saldo:.2f}')

    except ValueError:
        print('Erro: Por favor, digite valores numéricos válidos.')

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print('\nPrograma encerrado pelo usuário.')
    except Exception as e:
        print(f'Ocorreu um erro inesperado: {e}')