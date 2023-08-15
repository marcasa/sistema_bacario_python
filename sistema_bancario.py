from datetime import date


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
===============EXTRATO==============
OPERAÇÃO ----- DATA ----- VALOR 
"""
saldo = 0.00
qtd_saques = 0
LIMITE_SAQUE_DIARIO = 500.00
saque = 0.00
data_hoje = date.today()

while True :
    
    opcao = input(menu)

    if opcao == "1" :
        extrato += f"\n SALDO EM {data_hoje.day}/{data_hoje.month}/{data_hoje.year} R$ {saldo}"
        print(extrato)
    elif opcao == "2" :
        saque = float(input("Valor a ser sacado: "))
        if qtd_saques < 3 and saque <= 500.00 and saque <= saldo :
            saldo -= saque
            qtd_saques += 1 
            print("Saque efetuado com sucesso, retire seu dinheiro")
            print(f"Saldo atual = {saldo}")
            extrato += f"\n SAQUE ----- {data_hoje.day}/{data_hoje.month}/{data_hoje.year} ----- R$ {saque:.2f}"
        else :
            print("Erro ao efetuar o saque...")
            

    elif opcao == "3" :
        deposito = float(input("Valor do depósito: "))
        extrato += f"\n DEPÓSITO ----- {data_hoje.day}/{data_hoje.month}/{data_hoje.year} ----- R$ {deposito:.2f}"
        saldo += deposito

    elif opcao == "4" :
        print("Saindo...")
        break
    else :
        print("Opção inválida... ")
