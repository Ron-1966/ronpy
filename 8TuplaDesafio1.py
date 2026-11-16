# Exercício
# Cada produto é representado por uma tupla com a seguinte configuração:
# (Nome, QuantidadeEmEstoque)
# Desafio:
# 1) Mostre os produtos com menos de 5 unidades em estoque
# 2) Mostre a quantidade de produtos zerados e qual a quantidade total de itens no estoque
# 3) Quantidade total de itens no estoque

estoque = (("Mouse Lg Tech", 10),
           ("Mic Hyper X", 5),
           ("Acer Nitro 5", 3),
           ("WebCam HD", 0))

quantidadeProdutosComMenos5 = 0
quantidadeProdutosZerados = 0
quantidadeTotalDeProdutos = 0
print(f"------------Produtos com menos de 5 unidade disponíveis em estoque------------- ")
for produto in estoque:
    if produto[1] < 5:
        quantidadeProdutosComMenos5 += 1
        print(f"Produto : {produto[0]}, com {produto[1]} unidades em estoque.")

    if produto[1] == 0:
        quantidadeProdutosZerados += 1

    quantidadeTotalDeProdutos += 1

print(f"-------------------------------------------------------------------------------")

print(f"Quantidade de produtos com menos de cinco unidades : {quantidadeProdutosComMenos5}")

print(f"-------------------------------------------------------------------------------")

print(f"Quantidades de Produtos Zerados : {quantidadeProdutosZerados}")

print(f"-------------------------------------------------------------------------------")

print(f"Quantidades total de produtos : {quantidadeTotalDeProdutos}")

print(f"-------------------------------------------------------------------------------")
