# Automação de Testes de Software (ATS)

Repositório de entregas da disciplina **Automação de Testes de Software**, organizado por atividade prática (ATS). Cada pasta documenta o objetivo da entrega, os artefatos produzidos e, quando aplicável, como executar os testes automatizados.

## Sobre a disciplina

A matéria aborda fundamentos e prática de testes de software, com foco em:

- técnicas de teste caixa-preta (classes de equivalência, valores-limite);
- escrita de casos de teste e documentação de cenários;
- testes unitários em Python com `unittest` e `pytest`;
- validação de regras de negócio, exceções e cobertura de código.

Este repositório reúne as entregas ao longo do semestre, mantendo histórico claro do que foi desenvolvido em cada atividade.

## Estrutura do repositório

```text
.
├── README.md          # Visão geral da disciplina (este arquivo)
└── ATS/
    ├── ATS01/         # Projeto de casos de teste (documentação)
    ├── ATS02/         # Testes unitários com unittest
    ├── ATS03/         # Testes automatizados com pytest e cobertura
    ├── ATS04/         # Fixtures e parametrização com pytest
    ├── ATS05/         # Test-Driven Development com pytest
    └── ATS0N/         # Próximas entregas seguem o mesmo padrão
```

| Atividade | Tema principal | Tecnologias | Documentação |
|-----------|----------------|-------------|--------------|
| [ATS01](ATS/ATS01/README.md) | Casos de teste para e-commerce | Documentação / PDF | Entrega documental |
| [ATS02](ATS/ATS02/README.md) | Testes unitários em Python | `unittest` | 4 exercícios práticos |
| [ATS03](ATS/ATS03/README.md) | Pytest e cobertura de código | `pytest`, `pytest-cov` | Operações + e-commerce |
| [ATS04](ATS/ATS04/README.MD) | Fixtures e parametrização | `pytest` | 4 exercícios práticos |
| [ATS05](ATS/ATS05/README.md) | Test-Driven Development | `pytest` | Desconto, temperatura e estacionamento |

## Como navegar

1. Abra a pasta da atividade desejada (`ATS/ATS01`, `ATS/ATS02`, `ATS/ATS03`, ...).
2. Leia o `README.md` local — cada ATS tem objetivo, estrutura e instruções próprias.
3. Para atividades com código, siga a seção **Como executar os testes** do README correspondente.

## Padrão para novas entregas (ATS04+)

Ao adicionar uma nova atividade, crie uma pasta `ATS/ATS0N/` com:

- `README.md` descrevendo objetivo, estrutura, como rodar testes e autor;
- código-fonte e testes organizados em subpastas claras (`src/`, `tests/`, `docs/`, etc.);
- dependências em `requirements.txt`, quando houver projeto Python;
- artefatos de apoio (PDFs, prints de cobertura) em `docs/` ou `assets/`.

Atualize também a tabela deste README com a nova linha da atividade.

## Requisitos gerais

- Python 3.10+ (recomendado)
- `pip` ou ambiente virtual (`venv`)

Para projetos Python com dependências:

```bash
cd ATS/ATS0N
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Autor

**Ryan Rodrigues Cordeiro**
