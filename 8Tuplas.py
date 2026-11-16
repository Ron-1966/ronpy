# Exemplo de mutação em lista
lojaLista = ["camisetas", "Shorts", "Vestido"]
print(f"LojaLista inicial antes da alteraçao: {lojaLista}")
lojaLista[0] = "Camisa"
print(f"LojaLista depois da alteraçao: {lojaLista}")

# Exemplo de imutabilidade em tuplas
lojaTupla = ("Camiseta", "Shorts", "Vestido")
print(f"LojaTupla inicial: {lojaTupla}")
print(lojaTupla[2])

lojaTupla2 = ("Camiseta", "Shorts", "Vestido", "Vestido", "Camiseta")
# Count
print(f"Contagem do item Vestido: {lojaTupla2.count("Vestido")}")

# index
print(f"Posição no index da primeira ocorrência de Vestido: {lojaTupla.index("Vestido")}")
