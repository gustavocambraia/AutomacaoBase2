import time

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Pages.MinhaVisao import MinhaVisao


class Test_minhavisao(BaseTest):

    """
    Nesta classe são realizados os seguintes testes de acordo com o BDD:
            - Visualizar tarefas criadas (test_visualizar_tarefas);
            - Atualizar uma tarefa criada (test_atualizar_tarefa);
            - Apagar uma tarefa criada (test_apagar_tarefa);
            - Pesquisar tarefa com código válido (test_pesquisar_tarefa_valida);
            - Pesquisar tarefa com código inválido (test_pesquisa_invalida)
    """

    """
    def test_pesquisar_tarefa_valida(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login_tarefas(TestData.USER_NAME, TestData.PASSWORD)
        num_tarefa = homePage.confirmar_numero_tarefa()
        homePage.pesquisar_tarefa(num_tarefa)
        # homePage.do_enter(MinhaVisao.CAMPO_PESQUISAR_TAREFA)
        teste = homePage.verifica_tarefa_aberta()
        # titulo = homePage.get_title(TestData.TITULO_VER_TAREFAS)
        assert num_tarefa == teste

    def test_visualizar_tarefas(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login_tarefas(TestData.USER_NAME, TestData.PASSWORD)
        homePage.do_click(MinhaVisao.VER_TAREFAS)
        assert homePage.ver_detalhes()

    def test_atualizar_tarefa(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login_tarefas(TestData.USER_NAME, TestData.PASSWORD)
        homePage.selecionar_tarefa()
        homePage.atualizar_tarefa()
        texto_descricao = homePage.realizar_atualizacao()
        verificar_texto = homePage.verifica_descricao()
        assert verificar_texto == texto_descricao

    def test_apagar_tarefa(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login_tarefas(TestData.USER_NAME, TestData.PASSWORD)
        homePage.selecionar_tarefa()
        numero_tarefa = homePage.numero_tarefa()
        homePage.deletar_tarefa()
        confirmar_numero = homePage.confirmar_numero_tarefa()
        assert numero_tarefa != confirmar_numero

    def test_pesquisa_invalida(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login_tarefas(TestData.USER_NAME, TestData.PASSWORD)
        homePage.pesquisar_tarefa_invalida()
        homePage.do_enter(MinhaVisao.CAMPO_PESQUISAR_TAREFA)
        homePage.verifica_erro_pesquisa()
        assert homePage
"""