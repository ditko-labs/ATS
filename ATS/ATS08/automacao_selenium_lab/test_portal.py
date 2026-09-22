import os
import platform

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def navegador():
    driver = webdriver.Chrome()
    caminho_html = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "portal.html")
    )
    driver.get("file://" + caminho_html)
    yield driver
    driver.quit()


def test_preencher_formulario(navegador):
    assert navegador.title == "Portal do Colaborador"

    campo_nome = navegador.find_element(By.ID, "nome_usuario")
    campo_email = navegador.find_element(By.ID, "email")
    botao_enviar = navegador.find_element(By.ID, "btn-enviar")
    mensagem_sucesso = navegador.find_element(By.ID, "msg-sucesso")

    campo_nome.send_keys("Ryan Rodrigues")
    campo_email.send_keys("ryan.rodrigues@example.com")
    botao_enviar.click()

    assert mensagem_sucesso.is_displayed()
    assert mensagem_sucesso.text == "Dados enviados com sucesso!"


def test_acoes_avancadas_mouse(navegador):
    acoes = ActionChains(navegador)

    botao_duplo = navegador.find_element(By.ID, "btn-duplo")
    acoes.double_click(botao_duplo).perform()
    assert botao_duplo.text == "Autorizado!"

    botao_direito = navegador.find_element(By.ID, "btn-direito")
    ActionChains(navegador).context_click(botao_direito).perform()
    assert botao_direito.text == "Menu Aberto!"


def test_acoes_teclado(navegador):
    campo_observacao = navegador.find_element(By.ID, "obs")
    tecla_selecionar_tudo = Keys.COMMAND if platform.system() == "Darwin" else Keys.CONTROL

    acoes = ActionChains(navegador)
    acoes.click(campo_observacao)
    acoes.key_down(tecla_selecionar_tudo).send_keys("a").key_up(tecla_selecionar_tudo)
    acoes.send_keys(Keys.BACKSPACE)
    acoes.perform()

    texto_esperado = "Teste automatizado finalizado."
    campo_observacao.send_keys(texto_esperado)

    assert campo_observacao.get_attribute("value") == texto_esperado
