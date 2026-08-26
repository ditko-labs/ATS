# ATS04 — Fixtures e parametrização com `pytest`

Quarta entrega da disciplina **Automação de Testes de Software**. O objetivo desta etapa é praticar o uso de `fixtures`, escopo de dependências e parametrização em testes com [`pytest`](https://docs.pytest.org/).

## Objetivo

Explorar conceitos fundamentais de testes automatizados em Python, incluindo:

- criação de fixtures para disponibilizar dados e recursos aos testes;
- uso de escopo de sessão para compartilhar estado entre testes;
- parametrização de casos de teste com diferentes entradas;
- manipulação de ambiente e arquivos temporários durante a execução.

## Estrutura

```text
ATS/ATS04/
├── ex01/
│   └── test_log.py
├── ex02/
│   └── projeto/
│       ├── conftest.py
│       └── test_db.py
├── ex03/
│   └── test_user_access.py
├── ex04/
│   └── test_processamento.py
├── requirements.txt
├── assets/
└── README.MD
```

## Exercícios

### 1. Escrita de log

**Arquivo:** [ex01/test_log.py](ex01/test_log.py)

Neste exercício, a fixture `log_file` cria um arquivo temporário para simular a escrita de um registro de log. Após o teste, o arquivo é removido automaticamente, validando a criação e a limpeza do ambiente.

| Cenário | Comportamento esperado |
|---------|------------------------|
| Criação do arquivo | Arquivo `test_log.txt` deve existir |
| Limpeza | Arquivo deve ser removido após o teste |

### 2. Conexão global de banco

**Arquivo:** [ex02/projeto/test_db.py](ex02/projeto/test_db.py)

A fixture `db_connection` possui escopo de sessão e simula uma conexão global ao banco de dados. O teste verifica que o mesmo valor é reutilizado em diferentes casos do mesmo contexto.

| Cenário | Descrição |
|---------|-----------|
| Fixture de sessão | Estado compartilhado entre testes |
| Reuso da conexão | Mesmo valor retornado em múltiplas execuções |

**Arquivo de suporte:** [ex02/projeto/conftest.py](ex02/projeto/conftest.py)

### 3. Controle de acesso por perfil

**Arquivo:** [ex03/test_user_access.py](ex03/test_user_access.py)

Neste exercício, a fixture usa `@pytest.fixture(params=[...])` para gerar múltiplos perfis de usuário. Cada caso representa um cenário diferente de acesso:

- `admin` → permitido
- `editor` → permitido
- `guest` → negado

| Perfil | Resultado esperado |
|--------|--------------------|
| `admin` | Acesso permitido |
| `editor` | Acesso permitido |
| `guest` | Acesso negado |

### 4. Ambiente e processamento de dados

**Arquivo:** [ex04/test_processamento.py](ex04/test_processamento.py)

O exercício configura uma variável de ambiente `APP_ENV=testing` por meio de uma fixture e valida a manipulação de uma lista de itens durante o processamento. A ideia é verificar o comportamento do sistema em um ambiente controlado de testes.

| Recurso | Aplicação |
|---------|-----------|
| `os.environ` | Definição do ambiente de teste |
| `yield` | Fornecimento e limpeza do contexto |
| Lista de dados | Inclusão de um novo item e validação do tamanho |

## Requisitos

```bash
cd ATS/ATS04
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
pytest ex01/test_log.py
pytest ex02/projeto/test_db.py
pytest ex03/test_user_access.py
pytest ex04/test_processamento.py
```

Também é possível executar com saída detalhada:

```bash
pytest -v
```

## Resultado esperado

A suíte deve executar com sucesso e validar os cenários de:

- criação e limpeza de arquivos;
- fixtures com escopo de sessão;
- parametrização de usuários;
- configuração de ambiente e processamento.

## Autor

**Ryan Rodrigues Cordeiro**