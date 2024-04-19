menu = """
    ################# Menu ##################

    [d] - depósito
    [s] - saque
    [e] - extrato
    [q] - sair

Digite a opção desejada: """


saldo              = 0
limite_por_saque   = 500
transacoes         = []
numero_saques      = 0
LIMITE_SAQUE       = 3
VALOR_SAQUE_MAXIMO = 500

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = input("Depósito: ")
        deposito = int(deposito)
        saldo += deposito
        transacoes.append(f'Depósito: R$ {deposito}')

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUE:
            saque = input("Saque: ")
            saque = int(saque)

            if (saldo >= saque) and (saque <= limite_por_saque):
                saldo -= saque
                transacoes.append(f'Saque: R$ {saque}')
                numero_saques += 1
            else:
                if saldo < saque:
                    print("Você não tem saldo suficiente, deposite primeiro antes de sacar!")
                else:
                    print(f"O valor do saque excede o limite máximo de saque por transação (R$ {limite_por_saque}).")
        else:
            print("Você atingiu a quantidade limite de saques diários!")
    
    elif opcao == "e":
        for transacao in transacoes:
            print(transacao)
        print("Saldo atual: R$", saldo)

    elif opcao == "q":
        break

    else:
        print("Opção inválida, por favor selecione novamente a opção desejada !")
