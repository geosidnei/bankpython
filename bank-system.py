'''
Sistema Bancário/Dio
Data: 25/2/23
Professor: Guilherme Arthur de Carvalho
'''

menu = """
Aperte a letra correspondente:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> ...:  """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3 # constante

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input('Informe o valor do depósito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'

        else:
            print('Operação falhou por valor inválido.')

    elif opcao == "s":
        valor = float(input('Informe o valor do saque: '))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Operação falhou por saldo insuficiente.')
            
        elif excedeu_limite:
            print('Operação falhou por limite ultrapassado.')
            
        elif excedeu_saques:    
            print('Operação falhou por número de saques ultrapassado.')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
            
    elif opcao == "e":
        print()
        print('*'*20, 'Extrato','*'*20)
        print('Não houve movimentações.' if not extrato else extrato)
        print()
        print(f'Saldo: R$ {saldo:.2f}')
        print('*'*49)

    elif opcao == "q":
        break

    else:
        print('''
            Operação inválida.
            Selecione a operação desejada.

            ''')
