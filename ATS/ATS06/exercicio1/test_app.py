from app import processar_envio

def test_enviar_mensagem_externa_chamada(mocker):

    mock_enviar_mensagem_externa = mocker.patch('app.enviar_mensagem_externa')

    processar_envio("Ryan", "Oi, tudo bem?")

    mock_enviar_mensagem_externa.assert_called_once_with("Ryan", "Oi, tudo bem?")


def test_processar_envio(mocker):

    mock_enviar_mensagem_externa = mocker.patch('app.enviar_mensagem_externa')
    mock_enviar_mensagem_externa.return_value = "Mensagem enviada para Ryan: Oi, tudo bem?"

    mensagem = processar_envio("Ryan", "Oi, tudo bem?")

    assert mensagem == "Mensagem enviada para Ryan: Oi, tudo bem?"