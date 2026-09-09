import pytest

from app import GerenciadorUsuarios, RepositorioUsuariosFake


@pytest.fixture
def repositorio_fake():
	return RepositorioUsuariosFake()


@pytest.fixture
def gerenciador_usuarios(repositorio_fake):
	return GerenciadorUsuarios(repositorio_fake)


def test_registrar_e_encontrar_usuario(gerenciador_usuarios):
	gerenciador_usuarios.registrar_usuario("Ryan")

	assert gerenciador_usuarios.encontrar_usuario("Ryan") == "Ryan"


def test_buscar_usuario_inexistente_retorna_none(gerenciador_usuarios):
	assert gerenciador_usuarios.encontrar_usuario("Inexistente") is None