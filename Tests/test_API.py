from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Pages.MinhaVisao import MinhaVisao


class Test_API(BaseTest):

    def test_criar_api(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login_api(TestData.USER_NAME, TestData.PASSWORD)
        texto_token = homePage.criar_token()
        assert texto_token

    def test_deletar_token(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login_api(TestData.USER_NAME, TestData.PASSWORD)
        homePage.deletar_token()
        titulo = homePage.get_title(TestData.TITULO_TOKEN_API)
        assert titulo == TestData.TITULO_TOKEN_API




