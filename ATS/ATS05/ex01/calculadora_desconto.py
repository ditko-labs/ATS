def calcular_desconto(valor_original, percentual_desconto):
    if percentual_desconto < 0 or percentual_desconto > 100:
        raise ValueError("Percentual de desconto deve ser um valor de 0 à 100")

    valor_desconto = valor_original * percentual_desconto / 100

    if valor_desconto > valor_original:
        valor_final = 0
    else:
        valor_final = valor_original - valor_desconto

    return valor_final
