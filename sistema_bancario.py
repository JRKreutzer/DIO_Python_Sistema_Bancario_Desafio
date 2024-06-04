# Variável que imprime o menu principal
menu = '''
{0:=^30}
=={1:^26}==
{0:=^30}

Selecione uma opção:

1. Depositar - Adicione fundos à sua conta.
2. Sacar - Retire fundos da sua conta.
3. Extrato - Verifique seu saldo atual.
0. Sair - Encerre o programa.

Digite a opção escolhida: '''.format('', 'Menu Bancário')

# Variável que imprime o cabeçalho do extrato
menu_extrato = '''
{0:=^30}
=={1:^26}==
{0:=^30}
'''.format('', 'Extrato')


# Variável para armazenar o saldo da conta
saldo = 0
# Limite por saque é de R$ 500,00
limite = 500
# Variável para armazenar o extrato da conta
extrato = ''
# Contador para o número de saques realizados no dia
numero_saques = 0
# Regra de negócio determina que o limite de saques diários seja de 3
LIMITE_SAQUES = 3

# Loop principal do programa
while True:

    # Solicita ao usuário que selecione uma opção do menu
    opcao = input(menu)

    # Opção 1: Depositar fundos na conta
    if opcao == '1':
        # Solicita ao usuário o valor a ser depositado
        valor = float(input('Digite o valor a ser depositado: '))

        # Verifica se o valor do depósito é válido
        if valor <= 0:
            print('Depósito não pode ser igual ou inferior a R$00,00, Tente novamente.')
        else:
            saldo += valor
            extrato += f'\nDepósito de R${saldo:.2f} realizado com sucesso.\n'
            print(f'\nDepósito de R${saldo:.2f} realizado com sucesso.\n')
        
    # Opção 2: Sacar fundos da conta
    elif opcao == '2':
        
        # Verifica se há saldo disponível para saque
        if saldo <= 0:
            print('\nOpção indisponível no momento, verifique seu saldo atual.\n')
        else:
            # Solicita ao usuário o valor a ser sacado
            valor = float(input('Digite o valor que deseja sacar: '))

            # Verifica se o valor do saque é válido
            if valor <= 0:
                print('\nFalha ao realizar o saque, valores iguais ou menores que zero não são aceitos.\n')
            # Verifica se o valor do saque é maior que o valor em conta
            elif valor > saldo:
                print('\nFalha ao realizar o saque, verifique o seu saldo atual.\n')
            # Verifica se o valor do saque é maior que o limite da conta
            elif valor > limite:
                print('\nFalha ao realizar o saque, valor ultrapassou o limite.\n')
            # Verifica se o limite de saques não foi ultrapassado
            elif numero_saques > 2:
                print('\nFalha ao realizar o saque, numeros de saques diários ultrapassado.\n')
            else:
                saldo -= valor
                numero_saques += 1
                extrato += f'\nSaque número {numero_saques} no valor de R${valor:.2f} realizado com sucesso.\n'
                print(f'\nSaque número {numero_saques} no valor de R${valor:.2f} realizado com sucesso.\n')

    # Opção 3: Ver extrato e saldo atual
    elif opcao == '3':
        print(menu_extrato)
        print('Não houve nenhum movimento na conta até o momento.\n') if not extrato else print(extrato + f'\nSaldo atual = R${saldo:.2f}\n')
    
    # Opção 0: Encerrar o programa
    elif opcao == '0':
        
        confirma = input('\nTem certeza que deseja sair? Digite [s] para sair ou qualquer outra tecla para voltar ao menu: ')
        # Confirmação de saída do programa
        if confirma == 's':
            break
        elif confirma == 'n':
            continue
    
    # Se a opção digitada pelo usuário for inválida, solicita que o usuário escolha novamente
    else:
        opcao = input('\nOperação inválida!' + menu)