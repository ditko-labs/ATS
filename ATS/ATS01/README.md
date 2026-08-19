# ATS01 — Casos de teste para e-commerce

Primeira entrega da disciplina **Automação de Testes de Software**. O foco é o **projeto de casos de teste** para o cálculo do valor final de uma compra em um e-commerce, usando técnicas de teste caixa-preta.

## Objetivo

Projetar e documentar casos de teste que validem o cálculo do valor final da compra, considerando:

- regras de **frete** (cobrança fixa ou frete grátis);
- aplicação dos cupons **PROMO10** e **PRIMEIRACOMPRA**;
- restrições de elegibilidade e precedência entre desconto e frete.

A abordagem combina:

- **Particionamento por Classes de Equivalência** — reduzir entradas mantendo cobertura lógica;
- **Análise de Valores-Limite** — exercitar fronteiras onde o comportamento muda.

## Cenário de negócio

Sistema de carrinho de compras com as seguintes regras (resumo):

| Regra | Descrição |
|-------|-----------|
| Valor dos produtos | Deve ser maior que zero |
| PROMO10 | 10% de desconto; válido apenas se valor ≥ R$ 100,00 |
| PRIMEIRACOMPRA | R$ 30,00 de desconto fixo |
| Cupons | Apenas um cupom por compra |
| Frete grátis | Valor (já descontado) ≥ R$ 200,00 |
| Frete pago | R$ 25,00 quando não elegível ao frete grátis |

> O desconto do cupom é aplicado **antes** da verificação de frete grátis.

## Classes de equivalência (valor dos produtos)

| Classe | Faixa (R$) | Comportamento esperado |
|--------|------------|------------------------|
| CE1 | V ≤ 0 | Entrada inválida |
| CE2 | 0 < V < 100 | Sem PROMO10; frete R$ 25,00 |
| CE3 | 100 ≤ V < 200 | PROMO10 permitido; frete R$ 25,00 |
| CE4 | V ≥ 200 | Frete grátis; PROMO10 permitido |

## Valores-limite analisados

| Fronteira | Valores testados (R$) | Regra impactada |
|-----------|----------------------|-----------------|
| Mínimo PROMO10 | 99,99 · 100,00 · 100,01 | Aceitação/rejeição do cupom |
| Frete grátis | 199,99 · 200,00 · 200,01 | Cobrança ou isenção de frete |

## Artefatos entregues

| Arquivo | Descrição |
|---------|-----------|
| [Exercicio_ATS01_RYAN-RODRIGUES-CORDEIRO.pdf](Exercicio_ATS01_RYAN-RODRIGUES-CORDEIRO.pdf) | Resolução completa com casos de teste |
| [Exercicio_ATS01_RYAN_RODRIGUES_CORDEIRO.zip](Exercicio_ATS01_RYAN_RODRIGUES_CORDEIRO.zip) | Pacote compactado da entrega |

## Tipo de entrega

Esta atividade é **documental** — não há código automatizado nesta pasta. A avaliação considera a qualidade dos casos de teste, cobertura das regras de negócio e uso correto das técnicas de projeto de testes.

## Autor

**Ryan Rodrigues Cordeiro**
