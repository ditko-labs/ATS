# ATS05 — Test-Driven Development com `pytest`

Quinta entrega da disciplina **Automação de Testes de Software**. O objetivo desta etapa é praticar o ciclo de **Test-Driven Development (TDD)**: escrever o teste primeiro, implementar o mínimo para passar e validar as regras de negócio com [`pytest`](https://docs.pytest.org/).

## Objetivo

Desenvolver e validar, orientado por testes:

- aplicação de desconto com percentual limitado e valor final não negativo;
- conversão bidirecional entre Celsius e Fahrenheit, com arredondamento e validação de tipo;
- cálculo de tarifa de estacionamento com valor mínimo, adicional por hora e teto máximo.

## Estrutura

```text
ATS/ATS05/
├── ex01/
│   ├── calculadora_desconto.py
│   └── test_calculadora.py
├── ex02/
│   ├── conversor_temperatura.py
│   └── test_conversor.py
├── ex03/
│   ├── sistema_estacionamento.py
│   └── test_estacionamento.py
├── assets/
│   └── Exercicio_ATS05.pdf
├── requirements.txt
└── README.md
```

## Exercícios

### 1. Calculadora de desconto

**Arquivo:** [ex01/calculadora_desconto.py](ex01/calculadora_desconto.py)

Função `calcular_desconto(valor_original, percentual_desconto)` aplica o percentual sobre o valor original e devolve o valor final.

| Regra | Comportamento |
|-------|---------------|
| Percentual válido | Aceita valores entre `0` e `100` |
| Percentual inválido | Levanta `ValueError` |
| Valor final | Resultado após o desconto; nunca negativo |

| Cenário | Entrada | Resultado esperado |
|---------|---------|-------------------|
| Desconto básico | `100`, `20` | `80` |
| Percentual inválido | `50`, `110` | `ValueError` |
| Desconto total | `100`, `100` | `0` |

### 2. Conversor de temperatura

**Arquivo:** [ex02/conversor_temperatura.py](ex02/conversor_temperatura.py)

Funções `celsius_para_fahrenheit(temperatura_celsius)` e `fahrenheit_para_celsius(temperatura_fahrenheit)`.

| Regra | Comportamento |
|-------|---------------|
| Conversão | Fórmulas `C → F` e `F → C` |
| Precisão | Arredonda o resultado para 2 casas decimais |
| Tipo inválido | Levanta `TypeError` quando o valor não é numérico |

| Cenário | Entrada | Resultado esperado |
|---------|---------|-------------------|
| Ponto de congelamento | `0 °C` | `32 °F` |
| Precisão Celsius | `25.5 °C` | `77.90 °F` |
| Tipo inválido (C → F) | `"0"` | `TypeError` |
| Ponto de congelamento | `32 °F` | `0 °C` |
| Precisão Fahrenheit | `77.9 °F` | `25.50 °C` |
| Tipo inválido (F → C) | `"32"` | `TypeError` |

### 3. Sistema de estacionamento

**Arquivo:** [ex03/sistema_estacionamento.py](ex03/sistema_estacionamento.py)

Função `calcular_valor_estacionamento(tempo_em_minutos)` calcula a tarifa de permanência.

| Regra | Comportamento |
|-------|---------------|
| Valor mínimo | `R$ 10` para permanência curta (até 60 minutos) |
| Hora adicional | `R$ 5` por hora excedente, com arredondamento para cima |
| Valor máximo | Teto de `R$ 50` |
| Tempo inválido | Levanta `ValueError` quando o tempo é menor ou igual a zero |

| Cenário | Tempo (min) | Resultado esperado |
|---------|-------------|-------------------|
| Permanência curta | `59` | `10` |
| 1 hora excedente | `61` | `15` |
| 2 horas excedentes | `150` | `20` |
| 3 horas excedentes | `200` | `25` |
| Teto diário | `1440` | `50` |
| Tempo inválido | `0` | `ValueError` |

## Requisitos

```bash
cd ATS/ATS05
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Dependência principal:

- `pytest`

## Como executar os testes

No diretório raiz do projeto:

```bash
pytest
```

Para executar um exercício específico:

```bash
pytest ex01/test_calculadora.py
pytest ex02/test_conversor.py
pytest ex03/test_estacionamento.py
```

Também é possível executar com saída detalhada:

```bash
pytest -v
```

Saída esperada: **15 testes** executados com sucesso.

## Resultado dos testes

| Módulo | Testes |
|--------|--------|
| `test_calculadora` | 3 |
| `test_conversor` | 6 |
| `test_estacionamento` | 6 |
| **Total** | **15** |

## Autor

**Ryan Rodrigues Cordeiro**
