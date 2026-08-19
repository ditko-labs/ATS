'''Exercício 4: Gerenciador de Carrinho de Compras
Objetivo: Testar listas, inserção, remoção e busca usando assertIn e
assertNotIn.
• Tarefa: Crie uma classe simples CarrinhoDeCompras que possui uma lista
itens vazia ao ser inicializada e três métodos:
• adicionar_item(item): adiciona o nome de um produto na lista.
• remover_item(item): remove o produto se ele estiver presente (se não
estiver, levanta um ValueError com a mensagem "Item não encontrado").
• listar_itens(): retorna a lista atual de itens.
Desafio: Crie uma classe de teste para verificar:
1. Adicionar um item e verificar se ele está presente na lista (assertIn).
2. Remover um item e verificar se ele não está mais na lista (assertNotIn).
3. Tentar remover um item que não está no carrinho e verificar se um
ValueError é disparado.'''


class CarrinhoDeCompras():
    def __init__(self):
        self.lista_itens = []

    def adicionar_item(self, item):
        self.lista_itens.append(item)

    def remover_item(self, item):
        if item in self.lista_itens:
            self.lista_itens.remove(item)
        else:
            raise ValueError('Item não encontrado')

    def listar_itens(self):
        return self.lista_itens