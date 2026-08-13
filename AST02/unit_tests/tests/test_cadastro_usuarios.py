import unittest
from src.cadastro_usuarios import cadastrar_senha

class TesteCadastroUsuarios(unittest.TestCase):

    def test_cadastrar_senha_valida(self):

        # Dado de entrada: senha válida
        senha = '123123123'

        # Variável que armazena o retorno da função de cadastro de senha
        senha_valida = cadastrar_senha(senha)

        # Verifica se o valor da variável é True
        self.assertTrue(senha_valida)


    def test_cadastrar_senha_invalida(self):

        # Dado de entrada: senha inválida
        senha = '123'

        # Verifica se a função retorna um ValueError em casos de senha inválida
        with self.assertRaises(ValueError):
            cadastrar_senha(senha)


    def test_capturar_erro(self):

        # Dado de entrada: senha inválida
        senha = '123'

        # Verifica se a função retorna um ValueError em casos de senha muito curta com a mensagem correta
        with self.assertRaises(ValueError) as e:
            cadastrar_senha(senha)
        self.assertEqual(str(e.exception), 'Senha muito curta')