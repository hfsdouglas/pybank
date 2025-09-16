LIMITE_SAQUES = 3

menu = True
largura = 60
qtd_saques = 0
saldo = 0
extrato = []

def retorno(mensagem="Ops... Não foi possível realizar a operação!"):
    print("\n")
    print("*" * largura)
    print(mensagem)
    print("*" * largura)
    print("\n")

def pergunta_extrato():
    valor = str(input("Deseja imprimir o extrato? (S/N) ")).upper()
    
    match valor:
        case "N":
            return 
        case _:
            imprimir_extrato()
    
def saque():
    global saldo
    global qtd_saques
    global extrato 

    valor = float(input("Qual o valor desejado para saque? "))

    if qtd_saques <= LIMITE_SAQUES and saldo > 0 and saldo >= valor:
        saldo -= valor
        qtd_saques += 1

        extrato.append(["Saque", f"{valor:.2f}", f"{saldo:.2f}"])

        retorno(mensagem="Seu saque foi realizado com sucesso!")

        pergunta_extrato()
    else:
        retorno()

def deposito():
    global saldo
    global qtd_saques
    global extrato

    valor = float(input('Qual valor deseja depositar? '))

    saldo += valor
    extrato.append(["Depósito", f"{valor:.2f}", f"{saldo:.2f}"])

    retorno("Seu depósito foi realizado com sucesso!")

    pergunta_extrato()


def imprimir_extrato():
    titulo = "Extrato"

    print("\n")
    print(titulo.center(largura, "="))

    colunas = ["Operação", "Valor", "Saldo"]

    # calcula largura para cada coluna automaticamente
    largura_coluna = largura // len(colunas) - 1

    # monta cabeçalho
    cabecalho = "|".join(f"{c:^{largura_coluna}}" for c in colunas)

    print(f"|{cabecalho}|")
    print("-" * largura)
    
    for linha in extrato:
        linha_formatada = "|".join(f"{c:^{largura_coluna}}" for c in linha)
        print(f"|{linha_formatada}|")

    print("=" * largura)
    print("\n")

def sair():
    global menu

    retorno(mensagem="Agradecemos a sua visita!")

    menu = False

while menu: 
    titulo = "Olá, seja bem-vindo ao PyBank!"
    
    print(titulo.center(largura, "="))
    print("[1] Saque\n[2] Depósito\n[3] Imprimir Extrato\n[4] Sair")
    print("=" * largura)

    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            saque()
        case 2:
            deposito()
        case 3:
            imprimir_extrato()
        case _:
            sair()