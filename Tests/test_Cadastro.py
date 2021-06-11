from Pages.LoginPage import LoginPage
from Config.config import TestData
from Tests.test_base import BaseTest


class Test_cadastro(BaseTest):
    """
    def test_alterar_senha_invalido(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login_cadastro(TestData.USER_NAME, TestData.PASSWORD)
        homePage.alterar_senha_invalida()
        erro = homePage.verifica_pagina_erro_senha()
        assert TestData.MENSAGEM_ERRO_SENHA == erro


    """
    def test_mudar_nome_real(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login_cadastro(TestData.USER_NAME, TestData.PASSWORD)
        nome_alterado = homePage.alterar_nome_real()
        verifica_nome = homePage.verificar_nome_alterado()
        assert nome_alterado == verifica_nome
        homePage.reverter_nome_real()
"""
    def test_alterar_email(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login_cadastro(TestData.USER_NAME, TestData.PASSWORD)
        email_cadastrado = homePage.cadastrar_email()
        verifica_email = homePage.verificar_email_atualizado()
        assert email_cadastrado == verifica_email
        homePage.reverter_email()

    def test_alterar_senha(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login_cadastro(TestData.USER_NAME, TestData.PASSWORD)
        homePage.alterar_senha()
        homePage = self.loginPage.do_login_homepage(TestData.USER_NAME, "gusmantis1")
        title = homePage.get_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE
        homePage.reverter_senha()
    """





