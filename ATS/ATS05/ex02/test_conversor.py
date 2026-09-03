import pytest
from conversor_temperatura import celsius_para_fahrenheit, fahrenheit_para_celsius


def test_celsius_para_fahrenheit():
    assert celsius_para_fahrenheit(0) == 32


def test_celsius_para_fahrenheit_precisao():
    assert celsius_para_fahrenheit(25.5) == 77.90


def test_celsius_para_fahrenheit_valor_invalido():
    with pytest.raises(TypeError):
        celsius_para_fahrenheit("0")


def test_fahrenheit_para_celsius():
    assert fahrenheit_para_celsius(32) == 0


def test_fahrenheit_para_celsius_valor_precisao():
    assert fahrenheit_para_celsius(77.9) == 25.50


def test_fahrenheit_para_celsius_valor_invalido():
    with pytest.raises(TypeError):
        fahrenheit_para_celsius("32")
