exibe = True

def saque():
    print("Saque")

def deposito():
    print("Depósito")

def extrato():
    print("Extrato")

def sair():
    print("Sair")

while exibe: 
    print("""
===========Olá, seja bem-vindo ao PyBank!===========

[1] Saque
[2] Depósito
[3] Extrato
[4] Sair

====================================================
    """)

    opcao = int(input("Escolha uma opção: "))

    print("")

    match opcao:
        case 1:
            saque()
        case 2:
            deposito()
        case 3:
            extrato()
        case _:
            sair()
            exibe = False