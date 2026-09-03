from math import ceil


def calcular_valor_estacionamento(tempo_em_minutos):
    if tempo_em_minutos <= 0:
        raise ValueError("Tempo deve ser um valor maior que 0")

    hora_adicional = tempo_em_minutos - 60
    valor_total = (ceil(hora_adicional / 60) * 5) + 10

    if valor_total <= 50:
        valor_final = valor_total
    else:
        valor_final = 50

    return valor_final
