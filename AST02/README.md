# AST02 — Testes unitários com `unittest`

Segunda entrega da disciplina **Automação de Testes de Software**. O objetivo é praticar testes unitários em Python usando o módulo padrão [`unittest`](https://docs.python.org/3/library/unittest.html).

## Objetivo

Implementar funções e classes simples e validá-las com testes automatizados, cobrindo:

- asserts básicos (`assertTrue`, `assertFalse`, `assertEqual`);
- regras de negócio com múltiplos cenários;
- tratamento de exceções com `assertRaises`;
- manipulação de coleções com `assertIn` e `assertNotIn`.

## Estrutura

```text
AST02/
└── unit_tests/
    ├── docs/
    │   └── Exercício ATS02.pdf      # Enunciado da atividade
    ├── src/                         # Código sob teste
    │   ├── verificador_idade.py
    │   ├── calculadora_desconto.py
    │   ├── cadastro_usuarios.py
    │   └── carrinho_compras.py
    └── tests/                       # Suíte de testes
        ├── test_verificador_idade.py
        ├── test_calculadora_desconto.py
        ├── test_cadastro_usuarios.py
        └── test_carrinho_compras.py
```

## Exercícios

### 1. Verificador de idade

**Arquivo:** [unit_tests/src/verificador_idade.py](unit_tests/src/verificador_idade.py)

Função `pode_dirigir(idade)` retorna `True` se idade ≥ 18.

| Cenário | Entrada | Resultado esperado |
|---------|---------|-------------------|
| Positivo | 20 | `True` |
| Negativo | 16 | `False` |

### 2. Calculadora de descontos

**Arquivo:** [unit_tests/src/calculadora_desconto.py](unit_tests/src/calculadora_desconto.py)

Função `calcular_desconto(valor, percentual)` aplica desconto com limite máximo de 50%.

| Cenário | Descrição |
|---------|-----------|
| Desconto comum | Ex.: 10% sobre R$ 100 |
| Limite de segurança | Percentual > 50% limitado a 50% |
| Valor inválido | Valor ≤ 0 levanta `ValueError` |

### 3. Cadastro de usuários

**Arquivo:** [unit_tests/src/cadastro_usuarios.py](unit_tests/src/cadastro_usuarios.py)

Função `cadastrar_senha(senha)` exige no mínimo 8 caracteres.

| Cenário | Descrição |
|---------|-----------|
| Sucesso | Senha válida retorna `True` |
| Exceção | Senha curta levanta `ValueError` |
| Mensagem | Erro com texto `"Senha muito curta"` |

### 4. Carrinho de compras

**Arquivo:** [unit_tests/src/carrinho_compras.py](unit_tests/src/carrinho_compras.py)

Classe `CarrinhoDeCompras` com `adicionar_item`, `remover_item` e `listar_itens`.

| Cenário | Assert utilizado |
|---------|------------------|
| Adicionar item | `assertIn` |
| Remover item | `assertNotIn` |
| Item inexistente | `assertRaises(ValueError)` |

## Como executar os testes

Na pasta `unit_tests`:

```bash
cd AST02/unit_tests
python3 -m unittest discover -s tests -p "test_*.py" -v
```

Saída esperada: **11 testes** executados com sucesso.

## Resultado dos testes

| Módulo | Testes |
|--------|--------|
| `test_verificador_idade` | 2 |
| `test_calculadora_desconto` | 3 |
| `test_cadastro_usuarios` | 3 |
| `test_carrinho_compras` | 3 |
| **Total** | **11** |

## Autor

**Ryan Rodrigues Cordeiro**
