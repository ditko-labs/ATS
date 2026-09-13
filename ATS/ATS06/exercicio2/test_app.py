import pytest
from app import GerenciadorUsuarios, RepositorioUsuariosFake


@pytest.fixture()
def repositorio():
    return RepositorioUsuariosFake()

@pytest.fixture()
def gerenciador(repositorio):
    return GerenciadorUsuarios(repositorio)


def test_adicionar_e_encontrar_usuario(gerenciador):
    gerenciador.registrar_usuario("Ryan")

    usuario = gerenciador.encontrar_usuario("Ryan")

    assert usuario == "Usuário Ryan encontrado"


def test_encontrar_usuario_inexistente(gerenciador):
    usuario = gerenciador.encontrar_usuario("João")

    assert usuario is None