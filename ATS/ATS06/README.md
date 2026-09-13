# ATS06 - Dublê de Testes

Este repositório reúne exercícios práticos em Python sobre o uso de `dublês de teste` para isolar dependências e verificar comportamentos durante testes automatizados, que fazem parte da disciplina de **Automação de Testes de Software**.

## Objetivos

- Substituir uma função externa por um `mock`.
- Usar um `fake` para simular um repositório de usuários.
- Verificar a sequência de chamadas de um processo com `Mock`.

## Estrutura

```text
ATS06
├── assets/
├── exercicio1/
│   ├── app.py
│   └── test_app.py
├── exercicio2/
│   ├── app.py
│   └── test_app.py
├── exercicio3/
│   ├── app.py
│   └── test_app.py
├── README.md
└── requirements.txt
```

## Exercícios

### Exercício 1: mock de função externa

`processar_envio` depende de `enviar_mensagem_externa`. Os testes substituem essa função com `mocker.patch` para verificar:

- se a dependência foi chamada com destinatário e texto corretos;
- se o retorno da dependência é repassado pelo processo.

### Exercício 2: fake de repositório

`GerenciadorUsuarios` recebe um repositório por injeção de dependência. `RepositorioUsuariosFake` simula o armazenamento em memória e permite testar:

- o cadastro e a busca de um usuário;
- o comportamento quando o usuário não existe.

### Exercício 3: mock de objeto e ordem das chamadas

`executar_processo` recebe um processador e coordena validação e salvamento. O teste usa `Mock` para verificar que:

1. os dados são validados;
2. os dados são salvos após a validação;
3. o processo retorna a mensagem esperada.

## Como executar

1. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv .venv
```

2. Ative o ambiente virtual:

- No Windows:

```bash
.venv\Scripts\activate
```

- No Linux/macOS:

```bash
source .venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute os testes:

```bash
pytest exercicio1/test_app.py -v
```

```bash
pytest exercicio2/test_app.py -v
```

```bash
pytest exercicio3/test_app.py -v
```

## Autor

**Ryan Rodrigues Cordeiro**