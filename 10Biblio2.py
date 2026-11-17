import pandas as pd

# Criando uma mini base de dados

dados = {
    "Produto": ["Camisa", "Calça", "Boné", "Tenis"],
    "Preço": [79.90, 129.90, 39.90, 299.90],
    "Estoque": [15, 5, 20, 8]
}

df = pd.DataFrame(dados)

# Exibindo o Dataframe
print("Tabela de produtos:")
print(df)

# Operações simples
print("\nPreço médio:", df["Preço"].mean())
print("Produto mais caro:", df.loc[df["Preço"].idxmax(), "Produto"])
