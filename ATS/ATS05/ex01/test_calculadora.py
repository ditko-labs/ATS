import pytest
from calculadora_desconto import calcular_desconto


def test_calcular_desconto_basico():
    assert calcular_desconto(100, 20) == 80


def test_calcular_desconto_invalido():
    with pytest.raises(ValueError):
        calcular_desconto(50, 110)


def test_valor_final_minimo():
    assert calcular_desconto(100, 100) == 0
