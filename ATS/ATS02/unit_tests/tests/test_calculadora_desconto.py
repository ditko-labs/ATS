import unittest
from src.calculadora_desconto import calcular_desconto

class TesteCalculadoraDesconto(unittest.TestCase):

    def test_desconto_comum(self):

        # Dados de entrada e resultado esperado com desconto comum
        valor_produto = 100
        percentual_desconto = 30
        resultado_esperado = 70

        # Variável que armazena o retorno da função de cálculo de desconto
        valor_total = calcular_desconto(valor_produto, percentual_desconto)

        # Verifica se o valor armazenado na variável 'valor_total' é igual ao resultado esperado
        self.assertEqual(valor_total, resultado_esperado)

    def test_limite_desconto(self):

        # Dados de entrada e resultado esperado com desconto limite de 50%
        valor_produto = 100
        percentual_desconto = 55
        resultado_esperado = 50

        # Variável que armazena o retorno da função de cálculo de desconto
        valor_total = calcular_desconto(valor_produto, percentual_desconto)

        # Verifica se o valor da variável 'valor_total' é igual ao resultado esperado
        self.assertEqual(valor_total, resultado_esperado)

    def test_valor_produto(self):

        # Dados de entrada: valor do produto igual a zero
        valor_produto = 0
        percentual__desconto = 10

        # Verifica se a função de cáculto de desconto retorna um ValueError em caso de valor do produto = 0
        with self.assertRaises(ValueError):
            calcular_desconto(valor_produto, percentual__desconto)