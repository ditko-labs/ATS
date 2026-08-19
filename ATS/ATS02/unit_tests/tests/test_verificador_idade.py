import unittest
from src.verificador_idade import pode_dirigir

class TesteVerificadorIdade(unittest.TestCase):

    def test_pode_dirigir_positivo(self):

        # Dado de entrada: maior de idade
        idade = 19

        # Variável que recebe o retorno da função de verificação de idade
        habilitado = pode_dirigir(idade)

        # Verifica se o valor da variável 'habilitado' é True
        self.assertTrue(habilitado)


    def test_pode_dirigir_negativo(self):

        # Dado de entrada: menor de idade
        idade = 16

        # Variável que recebe o retorno da função de verificação de idade
        habilitado = pode_dirigir(idade)

        # Verifica se o valor da variável 'habilitado' é False
        self.assertFalse(habilitado)