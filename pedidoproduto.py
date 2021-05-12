
print("===== Programa para fazer pedidos =====")
print("Digite os pedidos separados por pedido.")
print('')


pedidonum = int(input("Digite o Número do Pedido: "))
numproduct = int(input("Digite o Produto: "))
qtdpedida = int(input("Digite a quantidade: "))


# def Leitura_pedidos
# N pedido (Int 4 Dig) +  N Produto (Int 3 dig) + Qnt pedida (Inteiro)
# def leitura_pedidos ( PEDIDOS ) - função faz a leitura dos pedidos, organizando no dicionário – pode usar return se quiser

pedido = {1: 'Caneta', 2: 'Lápis', 3: 'Caderno', 4: 'Tesoura', 5: 'Borracha',
          6: 'Corretivo', 7: 'Apontador', 8: 'Cola', 9: 'Mochila', 10: 'Marca-texto'}
print(pedido)

#  pedidos = {1}

n_pedido = int(input("Digite o numero do pedido: "))
quant_prod = int(input("Quantos produtos deste pedido?: "))
i = 0

while i < quant_prod:
    n_produto = int(input("Nº Produto: "))
    quantidade = int(input("Quantidade: "))
    i += 1


# def Imprime_relatório
# def imprime_relatorio (Tab_Precos, PEDIDOS) - essa função deverá imprimir o relatório pedido;


# def Valida_Produto
# def valida_produto(CodigoProduto, Tab_Precos) – função que retorna True ou False se o código digitado no pedido existe ou não na Tabela de Preços;
