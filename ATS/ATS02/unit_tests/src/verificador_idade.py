'''Exercício 1: O Verificador de Idade
Objetivo: Praticar a estrutura básica e assertTrue / assertFalse /
assertEqual.
• Tarefa: Crie uma função pode_dirigir(idade) que retorna True se a idade
for maior ou igual a 18, e False caso contrário.
• Desafio: Escreva uma classe de teste com dois métodos:
1. Um método para testar um caso positivo (ex: 20 anos).
2. Um método para testar um caso negativo (ex: 16 anos).'''


def pode_dirigir(idade):

    if idade >= 18:
        return True
    else:
        return False
    