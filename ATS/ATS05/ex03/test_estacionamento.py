import pytest
from sistema_estacionamento import calcular_valor_estacionamento


def test_valor_minimo():
    assert calcular_valor_estacionamento(59) == 10


def test_hora_adicional():
    assert calcular_valor_estacionamento(61) == 15


def test_hora_adicional_2():
    assert calcular_valor_estacionamento(150) == 20


def test_hora_adicional_3():
    assert calcular_valor_estacionamento(200) == 25


def test_valor_maximo():
    assert calcular_valor_estacionamento(1440) == 50


def test_tempo_invalido():
    with pytest.raises(ValueError):
        calcular_valor_estacionamento(0)
