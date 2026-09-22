# ATS08 — Automação e Validação de Interface com Selenium e Pytest

Oitava entrega da disciplina **Automação de Testes de Software**. O objetivo desta etapa é aplicar o ecossistema Selenium em uma suíte ponta a ponta (E2E) sobre uma página HTML local, com locators e assertions no Pytest.

## Objetivo

Automatizar e validar o **Portal do Colaborador**:

- título da página e envio de um formulário simples;
- ações avançadas de mouse (duplo clique e clique direito);
- ações avançadas de teclado (selecionar tudo, apagar e redigitar).

## Estrutura

```text
ATS/ATS08/
├── assets/
│   └── Exercício ATS08.pdf
├── automacao_selenium_lab/
│   ├── portal.html
│   ├── test_portal.py
│   └── requirements.txt
└── README.md
```

## Página alvo

**Arquivo:** [automacao_selenium_lab/portal.html](automacao_selenium_lab/portal.html)

Página local com formulário de colaborador, mensagem de sucesso, botões de ação avançada e um campo de observações.

## Suíte de testes

**Arquivo:** [automacao_selenium_lab/test_portal.py](automacao_selenium_lab/test_portal.py)

A fixture `navegador` inicia o ChromeDriver, abre `portal.html` pelo caminho absoluto e fecha o navegador ao final de cada teste.

| Cenário | Função | O que valida |
|---------|--------|--------------|
| Título e formulário | `test_preencher_formulario` | Título `Portal do Colaborador`, preenchimento dos campos e mensagem `Dados enviados com sucesso!` |
| Mouse | `test_acoes_avancadas_mouse` | Duplo clique em `Autorizado!` e clique direito em `Menu Aberto!` |
| Teclado | `test_acoes_teclado` | Seleção e exclusão do texto padrão, depois o valor `Teste automatizado finalizado.` |

## Requisitos

```bash
cd ATS/ATS08/automacao_selenium_lab
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Dependências:

- `pytest`
- `selenium`

O Chrome precisa estar instalado. O Selenium Manager baixa o ChromeDriver automaticamente.

## Como executar os testes

No diretório do laboratório:

```bash
pytest test_portal.py -v
```

Saída esperada: **3 testes** executados com sucesso.

## Autor

**Ryan Rodrigues Cordeiro**
