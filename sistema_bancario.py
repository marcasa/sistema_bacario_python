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

def sacar(valor_saque, saldo ,qtd_saques, hoje):
    hoje = date.today()
    if qtd_saques < 3:
        if valor_saque <=500.00 :
            if valor_saque <= saldo :
                saldo -= valor_saque
                qtd_saques += 1
                print("Saque efetuado com sucesso! Retire seu dinheiro")
                extrato = f"\n SAQUE -------- {hoje.day}/{hoje.month}/{hoje.year} ------ R$ {valor_saque:.2f}"
                return extrato, qtd_saques, saldo
            else:
                print("Saldo insuficiente para o valor desejado")
        else:
            print("Valor do saque deve ser menor que R$ 500.00")
    else:
        print("Quantidade de saques diários ultrapassado")


def depositar(valor_deposito, hoje):
    
    extrato = f"\n DEPÓSITO ----- {hoje.day}/{hoje.month}/{hoje.year} ----- R$ {valor_deposito:.2f}"
    print("Deposito realizado com sucesso")
    return extrato, valor_deposito

def gerar_extrato(saldo, hoje):
    extrato = f"\n SALDO EM {hoje.day}/{hoje.month}/{hoje.year} R$ {saldo}"
    return extrato


while True :
    
    opcao = input(menu)

    if opcao == "1" :
        extrato_return = gerar_extrato(saldo=saldo, hoje=data_hoje)
        print(extrato)
        print(extrato_return)
    elif opcao == "2" :
            
        saque = float(input("Valor a ser sacado: "))
        sacar_return = sacar(valor_saque=saque, saldo=saldo, qtd_saques=qtd_saques, hoje = data_hoje)
        if  sacar_return is not None:
            extrato += sacar_return[0]
            qtd_saques = sacar_return[1]
            saldo = sacar_return[2]
        
    elif opcao == "3" :
        deposito = float(input("Valor do depósito: "))
        deposito_return = depositar(valor_deposito=deposito, hoje=data_hoje )
        extrato += deposito_return[0]
        saldo += deposito_return[1]
        

    elif opcao == "4" :
        print("Saindo...")
        break
    else :
        print("Opção inválida... ")





