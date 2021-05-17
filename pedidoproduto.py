pedido = dict()
pedidos = list()
tabela_precos = dict()

Tabela_Precos = {1000: ['Caneta Azul Pamper', 2], 1001: ['Estojo Canetinha Colorida', 5], 1002: ['Apagador de Quadro Negro', 7], 1003: [
    'Caderno Sticker', 3], 1004: ['Mouse Pad Air', 25], 1005: ['Estojo Escolar', 10], 1006: ['Caderno 10 Volumes Musical', 8], 1007: ['Cola Bastão', 3], 1008: ["Borracha", 2], 1009: ['Fichário', 20], 1010: ['Grampeador', 10]}


print("Digite o número do pedido: ")


while True:
    pedidos.clear()
    Numero_Pedido = int(input("Digite número do pedido: "))
    Numero_Produtos = int(input("Digite número de Produtos que deseja: "))
    NumeroProdutoA = int(input("Digite número do produto: "))
    QntA = int(input("Digite a quantidade: "))
    NumeroProdutoB = int(input("Digite número do produto: "))
    QntB = int(input("Digite a quantidade: "))
    NumeroProdutoC = int(input("Digite número do produto: "))
    QntC = int(input("Digite a quantidade: "))

    pedido = {Numero_Pedido: [Numero_Produtos, {
        NumeroProdutoA: QntA, NumeroProdutoB: QntB, NumeroProdutoC: QntC}]}

    pedidos.append(pedido.copy())
    while True:
        resp = str(input('Quer Fazer mais pedido? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print("ERROR: RESPONDA (S) OU (N).")
    if resp == 'N':
        break


print(pedidos)
