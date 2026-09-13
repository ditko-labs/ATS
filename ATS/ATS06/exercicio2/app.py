from abc import ABC, abstractmethod
from typing import Optional


class IRepositorioUsuarios(ABC):

    @abstractmethod
    def adicionar_usuario(nome: str):
        pass

    @abstractmethod
    def buscar_usuario(nome: str) -> Optional[str]:
        pass


class RepositorioUsuariosFake(IRepositorioUsuarios):
    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self, nome):
        self.usuarios.append(nome)
        return f'Usuário {nome} adicionado com sucesso'


    def buscar_usuario(self, nome):
        if nome in self.usuarios:
            return f'Usuário {nome} encontrado'
        else:
            return None


class GerenciadorUsuarios():
    def __init__(self, repositorio: IRepositorioUsuarios):
        self.repositorio = repositorio

    def registrar_usuario(self, nome: str):
        return self.repositorio.adicionar_usuario(nome)

    def encontrar_usuario(self, nome: str):
        return self.repositorio.buscar_usuario(nome)