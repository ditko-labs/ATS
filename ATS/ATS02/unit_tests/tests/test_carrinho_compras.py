import unittest
from src.carrinho_compras import CarrinhoDeCompras

class TesteCarrinhoDeCompras(unittest.TestCase):

    def test_adicionar_item(self):

        # Dado de entrada: produto que será colocado no carrinho
        item = 'tênis'

        # Objeto que representa o carrinho de compras e função que adiciona um item ao carrinho
        carrinho = CarrinhoDeCompras()
        carrinho.adicionar_item(item)

        # Verifica se o item foi adicionado ao carrinho
        self.assertIn(item, carrinho.lista_itens)


    def test_remover_item(self):

        # Dado de entrada: produto que será colocado e posteriormente removido do carrinho
        item = 'boné'

        # Objeto que representa o carrinho de compras e função que adiciona um item ao carrinho
        carrinho = CarrinhoDeCompras()
        carrinho.adicionar_item(item)

        # Função que remove um item do carrinho
        carrinho.remover_item(item)

        # Verifica se o item foi removido do carrinho
        self.assertNotIn(item, carrinho.lista_itens)


    def test_remover_item_inexistente(self):

        # Dado de entrada: produto que não está no carrinho
        item = 'blusa'

        # Objeto que representa o carrinho de compras
        carrinho = CarrinhoDeCompras()

        # Verifica de a função de remover item retorna um ValueError no caso do produto não estar no carrinho
        with self.assertRaises(ValueError):
            carrinho.remover_item(item)