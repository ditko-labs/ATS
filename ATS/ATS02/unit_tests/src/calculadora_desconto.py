'''Exercício 2: Calculadora de Descontos
Objetivo: Praticar lógica de negócio e múltiplos métodos de teste.
• Tarefa: Crie uma função calcular_desconto(valor, percentual) que
retorna o valor final do produto com desconto aplicado.
• Regra de negócio: Se o percentual informado for maior que 50%, a função
deve limitar o desconto a 50%.
Desafio: Crie testes para:
1. Um desconto comum (ex: 10% de R$ 100).
2. O limite de segurança (ex: tentar aplicar 70% de desconto e verificar se o
valor final reflete apenas 50%).
3. Um valor de produto igual a zero.'''


def calcular_desconto(valor, percentual):

    if valor > 0:
        if percentual <= 50:
            desconto = valor * percentual/100
        else:
            desconto = valor * 0.5

        valor_final = valor - desconto
        return valor_final
    
    else:
        raise ValueError('Valor inválido.')