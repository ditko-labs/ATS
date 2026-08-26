import pytest
import os


@pytest.fixture()
def enviroment():
    os.environ["APP_ENV"] = "testing"

    yield

    del os.environ["APP_ENV"]

@pytest.fixture()
def banco_falso(enviroment):
    return ["item1", "item2"]


def test_processamento_de_dados(banco_falso):
    banco_falso.append("item3")
    
    assert os.environ["APP_ENV"] == "testing"
    assert len(banco_falso) == 3