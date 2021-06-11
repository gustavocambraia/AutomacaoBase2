from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Pages.MinhaVisao import MinhaVisao


class Test_API(BaseTest):

    """
    Nesta classe são realizados os seguintes testes de acordo com o BDD:
            - Gerar uma chave de acesso para minha API (test_criar_api);
            - Revogar o acesso de uma API (test_deletar_token)
    """

    def test_criar_api(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login_api(TestData.USER_NAME, TestData.PASSWORD)
        homePage.criar_token()
        titulo = homePage.get_title(TestData.TITULO_TOKEN_API)
        assert titulo == TestData.TITULO_TOKEN_API

    def test_deletar_token(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login_api(TestData.USER_NAME, TestData.PASSWORD)
        homePage.deletar_token()
        titulo = homePage.get_title(TestData.TITULO_TOKEN_API)
        assert titulo == TestData.TITULO_TOKEN_API
