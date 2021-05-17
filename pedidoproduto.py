pedido = dict()
pedidos = list()


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
    
    pedido = {Numero_Pedido:[Numero_Produtos, {NumeroProdutoA:QntA,NumeroProdutoB:QntB,NumeroProdutoC:QntC}]}
    
    pedidos.append(pedido.copy())
    while True:
        resp = str(input('Quer Fazer mais pedido? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print("ERROR: RESPONDA (S) OU (N).")
    if resp == 'N':
        break



print(pedidos)

