def calcularDesconto(valorBase: object, percentualDeDesconto: object) -> None:
    """Informa-se o valor base e o percentual de desconto"""
    ValorLiquido = (valorBase * (1 - percentualDeDesconto))
    ValorDesconto = valorBase - ValorLiquido

    print(f"Valor base sem desconto : {valorBase}")
    print(f"Percentual de desconto aplicado : {percentualDeDesconto * 100}%")
    print(f"Valor do desconto : {ValorDesconto}")
    print(f"Valor liquido : {ValorLiquido}")


def main():
    calcularDesconto(200.00, 0.20)


main()
