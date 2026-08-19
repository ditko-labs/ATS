import pytest
from core.operacoes import somar, subtrair, multiplicar, dividir, raiz_quadrada, calcular_media

def test_somar():
    assert somar(5, 2) == 7

def test_subtrair():
    assert subtrair(5, 2) == 3

def test_multiplicar():
    assert multiplicar(5, 2) == 10

def test_dividir_sucesso():
    assert dividir(5, 2) == 2.5

def test_dividir_falha():
    with pytest.raises(ValueError):
        dividir(5, 0)

def test_raiz_quadrada():
    assert raiz_quadrada(9) == 3

def test_raiz_quadrada_numero_negativo():
    with pytest.raises(ValueError):
        raiz_quadrada(-9)

def test_calcular_media_exata():
    assert calcular_media([1, 2, 3]) == 2

def test_calcular_media_aproximada():
    assert calcular_media([0.1, 0.2]) == pytest.approx(0.15)

def test_calcular_media_lista_vazia():
    resultado = calcular_media([])
    assert resultado is False
