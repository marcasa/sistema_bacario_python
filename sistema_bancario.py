menu = """
========SISTEMA BANCÁRIO============
Digite a opção desejada:

1 - Extrato
2 - Saque
3 - Depósito
4 - Sair
====================================

"""
extrato = """
==========EXTRATO===========
"""
saldo = 5000.00
qtd_saques = 0
LIMITE_SAQUE_DIARIO = 500.00

saque = 0.00

while True :
    
    opcao = input(menu)

    if opcao == "1" :
        print(extrato)
    elif opcao == "2" :
        saque = float(input("Valor a ser sacado: "))
        if qtd_saques <= 3 and saque <= 500.00 and saque <= saldo :
            saldo -= saque
            qtd_saques += 1 
            print("Saque efetuado com sucesso, retire seu dinheiro")
            print(f"Saldo atual = {saldo}")
        else :
            print("Erro ao efetuar o saque...")
            

    elif opcao == "3" :
        deposito = input("Valor do depósito: ")
    elif opcao == "4" :
        print("Saindo...")
        break
    else :
        print("Opção inválida... ")
