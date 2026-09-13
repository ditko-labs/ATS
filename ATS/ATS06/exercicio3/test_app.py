from unittest.mock import call
from app import executar_processo


def test_executar_processo(mocker):
    mock_processador = mocker.Mock()

    mock_processador.validar_dados.return_value = True
    mock_processador.salvar_dados.return_value = True

    processo = executar_processo(mock_processador, {"nome": "Ryan"})

    roteiro_esperado = [
        call.validar_dados({"nome": "Ryan"}),
        call.salvar_dados({"nome": "Ryan"})
    ]

    mock_processador.assert_has_calls(roteiro_esperado, any_order=False)

    assert processo == "Dados salvos com sucesso"