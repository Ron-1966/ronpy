armario = {"Gaveta1": "Arquivo1", "Gaveta2": "Arquivo2"}
print(armario)
print(armario["Gaveta1"])
print(armario["Gaveta2"])

print("________________________________________________________________________________")

# Métodos
# .get() - pega o valor associado a uma chave.
print(armario.get("Gaveta1"))

# .keys() - retorna as chaves de um dicionário
print(armario.keys())

# .values
print(armario.values())

# .items()
print(armario.items())

# .setdefault(chave, valor)
armario.setdefault("Gaveta3", "Arquivo3")
print(armario)
print(armario.items())
