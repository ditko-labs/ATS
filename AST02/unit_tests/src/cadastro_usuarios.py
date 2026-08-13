'''Exercício 3: Sistema de Cadastro de Usuários
Objetivo: Testar validações e exceções com assertRaises.
• Tarefa: Crie uma função cadastrar_senha(senha).
• A senha deve ter pelo menos 8 caracteres.
• Se a senha for menor que isso, a função deve levantar um ValueError com a
mensagem "Senha muito curta".
Desafio: Crie testes para:
1. Teste de Sucesso: Verifique se uma senha válida (ex: 10 caracteres) é
cadastrada sem levantar erros.
2. Teste de Exceção: Use with self.assertRaises(ValueError): para
garantir que tentar cadastrar a senha "123" levanta o erro esperado.
3. Desafio Extra: Capture a exceção gerada e verifique se a mensagem do erro
é exatamente "Senha muito curta".'''


def cadastrar_senha(senha):

    if len(senha) >=8:
        return True
    else:
        raise ValueError('Senha muito curta')