menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while (True):
    op = input(menu)
    if op == "d":
        deposito = float(input("Insira o valor do depósito: "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif op == "s":
        if (numero_saques <= LIMITE_SAQUES):
            saque = float(input("Insira o valor do saque: "))
            if(saque > saldo):
                print("Saldo insuficiente.")
            elif (saque > limite):
                print("Limite de saque excedido!")
            elif (saque > 0):
                saldo -= saque
                extrato += f"Saque: R${saque:.2f}\n"
                numero_saques += 1
        else:
            print("Número de saques excedido!")
        
    
    elif op == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    
    elif op == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")