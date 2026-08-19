import pytest
from core.ecommerce import calcular_preco_final


def test_calcular_preco_final_valido():
    assert calcular_preco_final(100) == 120


def test_calcular_preco_final_invalido():
    with pytest.raises(ValueError):
        calcular_preco_final(0)


def test_calcular_preco_final_cupom_10():
    assert calcular_preco_final(50, cupom="PROMO10") == 65


def test_calcular_preco_final_cupom_20():
    assert calcular_preco_final(150, cupom="PROMO20") == 140


def test_calcular_preco_final_cupom_invalido():
    assert calcular_preco_final(30, cupom="PROMO30") == 50


def test_calcular_preco_final_frete_gratis():
    assert calcular_preco_final(300, frete_gratis=True) == 300


def test_calcular_preco_final_frete_gratis_acima_de_500():
    assert calcular_preco_final(550) == 550


def test_calcular_preco_final_desconto_aproximado():
    assert calcular_preco_final(1999.99, cupom="PROMO10") == pytest.approx(1799.99)
