print("==========🛒 SuperMarket 🛒==========")
print()
print("====== Produtos disponíveis =====")
print()
print("1 - Maça 🍎\n2 - Banana 🍌\n3 - Morango 🍓\n4 - Goiaba 🍈")

nome = input("Digite nome do produto: ")

qtd = int(input("Digite a quantidade do produto: "))


if qtd <= 0:
    produto = 'esgotado'


elif qtd <= 5:
    produto = 'Crítico'

elif qtd <= 20:
    produto = 'Baixo'

else:
    qtd >= 21
    produto = 'Estoque normal'
    
print("====== RELAÓRIO DE PRODUTOS =====")
print()
print(f"Produto: {nome}\nDisponível: {qtd}\nEstoque: {produto}")
print()
print("=================================")
