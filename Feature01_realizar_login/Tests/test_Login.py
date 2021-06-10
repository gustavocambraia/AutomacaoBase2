from selenium.webdriver.common.by import By
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Config.config import DadosTest
import pytest

class Test_Login(BaseTest):

    # Teste para login valido
    @pytest.mark.parametrize("usuario, senha", DadosTest.LISTA_VALIDOS)
    def test_login_usuario_valido(self, usuario, senha):
        self.loginPage = LoginPage(self.driver)
        myViewPage = self.loginPage.logar(usuario, senha)
        usuario_myview = myViewPage.get_usuario_myview()
        assert usuario == usuario_myview

    # Teste para login invalido
    @pytest.mark.parametrize("usuario, senha", DadosTest.LISTA_INVALIDOS)
    def test_login_usuario_invalido(self, usuario, senha):
        self.loginPage = LoginPage(self.driver)
        myViewPage = self.loginPage.logar(usuario, senha)
        elemento_resp = myViewPage.get_texto_elemento(LoginPage.MSG_ERRO)
        assert elemento_resp == DadosTest.MSG_ERRO_ESPERADO

    