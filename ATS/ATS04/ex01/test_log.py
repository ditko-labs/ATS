import pytest
import os


@pytest.fixture()
def log_file():
    arquivo = 'test_log.txt'

    yield arquivo

    if os.path.exists(arquivo):
        os.remove(arquivo)


def test_escrita_log(log_file):
    with open(log_file, 'w') as f:
        f.write('Teste de Log')

    assert os.path.exists(log_file)