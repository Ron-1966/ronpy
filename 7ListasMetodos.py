listaFrutas = ["Banana", "Maçã", "Uva"]
print(f"listaFrutas - valor inicial: {listaFrutas}")
# Métodos
# @append
listaFrutas.append("Kiwi")
print(f"listaFrutas - após append : {listaFrutas}")

# Insert(posição, elemento)
listaFrutas.insert(1, "Melancia")
print(f"listaFrutas - após insert : {listaFrutas}")

# remove(elemento
listaFrutas.remove("Banana")
print(f"listaFrutas - após remove : {listaFrutas}")

# sort
listaNumeros = [2, 5, 6, 2, 2, 4, 1]
print(f"listaNumeros inicial: {listaNumeros}")
listaNumeros.sort()
print(f"listaNumeros após sort: {listaNumeros}")
