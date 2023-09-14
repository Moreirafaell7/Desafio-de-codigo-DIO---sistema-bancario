menu = '''
Olá, selecione uma opção:

(1) Depósito
(2) Saque
(3) Extrato
(0) Sair

==>'''

# Variáveis
saldo_conta = 1000
limite = 500
qtd_saques = 0
limite_saques = 3
extrato = ''

while True:
    opcao = input(menu)

    # Depósito
    if opcao == "1":
      vlr = float(input("Valor do depósito: "))
      if vlr > 0:
        saldo_conta += vlr
        extrato += f'Depósito: R$ {vlr:.2f}\n'
      else:
        print("Valor incorreto. Tente novamente")
      print(saldo_conta)

    # Saque
    elif opcao == "2":
        vlr = float(input("Valor do saque: "))
        if vlr <= saldo_conta and qtd_saques < limite_saques and vlr <= limite:
            print('Saque realizado')
            saldo_conta -= vlr
            qtd_saques += 1
            extrato += f'Saque: R$ {vlr:.2f}\n'
        elif vlr > saldo_conta:
            print('Saldo insuficiente')
        elif qtd_saques >= limite_saques:
            print('Limite de saques atingido')
        elif vlr > limite:
            print('Valor maior que o limite de saque')

    # Extrato
    elif opcao == "3":
        print("Extrato:")
        print(extrato)

    # Sair
    elif opcao == "0":
        print("Obrigado. Operação encerrada")
        break

    # Opção inválida
    else:
        print("Opção inválida. Tente novamente")