import random


# função sem parametro e sem retorno
def bemVindo():
    print("Seja muito bem-vindo")


bemVindo()
bemVindo()
bemVindo()


# funcão sem parâmetro e com retorno
def aleatorio1to100():
    return random.randint(1, 100)


print(f"Retorno de um número aleatório entre 1 e 100 : {aleatorio1to100()}")
print(f"Retorno de um número aleatório entre 1 e 100 : {aleatorio1to100()}")
print(f"Retorno de um número aleatório entre 1 e 100 : {aleatorio1to100()}")


# função com parâmetro e sem retorno
def bemVindoPersonalizado(nome):
    print(f"Seja bem-vindo {nome}")


bemVindoPersonalizado("Ronaldo")
bemVindoPersonalizado("João")
bemVindoPersonalizado("Joana")


# função com parâmetro e com retorno
def soma3Mult10(numero):
    return ((numero + 3) * 10)


numeroBase = 2
print(f"O numero base é {numeroBase}")
print(
    f"Imprime o resultado da função que soma 3 ao numero base e então multiplica por 10 : {soma3Mult10(numeroBase)} ")

soma3Mult10(2)
