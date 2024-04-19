#MENU

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair do Menu
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato = f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Depósito não efetuado, valor esta inválido, por favor digite o valor novamente!")

    elif opcao == "s":
        valor = float(input("Digite o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("A operação falhou! O valor do saque excedeu o saldo, por favor tente novamente!")

        elif excedeu_limite:
            print("A operação falhou! O valor do saque excedeu o limite, por favor tente novamente!")

        elif excedeu_saques:
            print("A operação falhou! Foi excedido a quantidade de saques diárias, por favor tente novamente no dia seguinte!")

        elif valor > 0:
            saldo -= valor
            print(f"Valor restante: {saldo:.2f}")
            extrato = f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Saque não efetuado, valor esta inválido, por favor digite o valor novamente!")

    elif opcao == "e":
        print("\n============================== EXTRATO ==============================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("=======================================================================")

    elif opcao == "q":
        break

    else:
        print("Opção incorreta, por favor selecione novamente")