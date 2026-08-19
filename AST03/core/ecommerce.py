def calcular_preco_final(preco_base, cupom=None, frete_gratis=False):

    if preco_base <= 0:
        raise ValueError

    if cupom == "PROMO10":
        desconto = preco_base * 0.10
    elif cupom == "PROMO20":
        desconto = preco_base * 0.20
    else:
        desconto = 0

    valor_produto = preco_base - desconto

    if frete_gratis == True or valor_produto > 500:
        frete = 0
    else:
        frete = 20

    valor_final = valor_produto + frete
    return valor_final
