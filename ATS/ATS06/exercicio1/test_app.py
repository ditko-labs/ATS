from app import processar_envio

def test_processar_envio_chama_dependencia_externa(mocker):
    mock_get = mocker.patch("app.enviar_mensagem_externa")
    mock_get.return_value = "Mensagem enviada com sucesso"

    resultado = processar_envio("Ryan", "Olá, tudo bem por ai?")

    mock_get.assert_called_once_with("Ryan", "Olá, tudo bem por ai?")
    assert resultado == "Mensagem enviada com sucesso"