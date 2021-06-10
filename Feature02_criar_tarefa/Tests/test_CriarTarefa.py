from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.ViewTPage import ViewTPage
from selenium.webdriver.common.by import By
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Config.config import DadosTest
import pytest

class Test_Login(BaseTest):

    @pytest.mark.parametrize("resumo, descricao", DadosTest.LISTA_OBRIGATORIO)
    @pytest.mark.parametrize("usuario, senha", DadosTest.LISTA_LOGIN)
    def test_criar_tarefa_obrigatoria(self, usuario, senha, resumo, descricao):
        self.loginPage = LoginPage(self.driver)
        myViewPage = self.loginPage.logar(usuario, senha)
        BugReportPage = myViewPage.ir_para_criar_tarefa()
        ViewTPage = BugReportPage.criar_tarefa_obrigatoria(resumo, descricao)
        assert "Operação realizada com sucesso." in BugReportPage.driver.page_source
        id = ViewTPage.get_id()
        assert ViewTPage.verificar_url(f'id={id}')

    @pytest.mark.parametrize("resumo, descricao, plataforma, so, versaoSo, passos, infoAdc, tag", DadosTest.LISTA_TODOS)
    @pytest.mark.parametrize("usuario, senha", DadosTest.LISTA_LOGIN)
    def test_criar_tarefa_todos_inputs(
        self, usuario, senha, resumo, 
        descricao, plataforma, so, 
        versaoSo, passos, infoAdc, tag):
        self.loginPage = LoginPage(self.driver)
        myViewPage = self.loginPage.logar(usuario, senha)
        BugReportPage = myViewPage.ir_para_criar_tarefa()
        ViewTPage = BugReportPage.criar_tarefa_todos_inputs(resumo, 
        descricao, plataforma, so, 
        versaoSo, passos, infoAdc, tag)
        assert "Operação realizada com sucesso." in BugReportPage.driver.page_source
        id = ViewTPage.get_id()
        assert ViewTPage.verificar_url(f'id={id}')

    @pytest.mark.parametrize("resumo, descricao, arquivo", DadosTest.LISTA_ARQUIVO_VALID)
    @pytest.mark.parametrize("usuario, senha", DadosTest.LISTA_LOGIN)
    def test_criar_tarefa_arquivo_valido(self, usuario, senha, resumo, descricao, arquivo):
        self.loginPage = LoginPage(self.driver)
        myViewPage = self.loginPage.logar(usuario, senha)
        BugReportPage = myViewPage.ir_para_criar_tarefa()
        path_arquivo = f'C:\\Users\\Lorenzo\\Documents\\Aulas Faculdade\\ProjetoUC\\Feature02_criar_tarefa\\teste.pdf'
        ViewTPage = BugReportPage.criar_tarefa_arquivo_valid(resumo, descricao, path_arquivo)
        WebDriverWait(BugReportPage.driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.alert.alert-success'), "Operação realizada com sucesso"))
        assert "Operação realizada com sucesso." in BugReportPage.driver.page_source
        id = ViewTPage.get_id()
        assert ViewTPage.verificar_url(f'id={id}')

    @pytest.mark.parametrize("resumo, descricao, arquivo", DadosTest.LISTA_ARQUIVO_INVALID)
    @pytest.mark.parametrize("usuario, senha", DadosTest.LISTA_LOGIN)
    def test_criar_tarefa_arquivo_invalido(self, usuario, senha, resumo, descricao, arquivo):
        self.loginPage = LoginPage(self.driver)
        myViewPage = self.loginPage.logar(usuario, senha)
        BugReportPage = myViewPage.ir_para_criar_tarefa()
        path_arquivo = f'C:\\Users\\Lorenzo\\Documents\\Aulas Faculdade\\ProjetoUC\\Feature02_criar_tarefa\\{arquivo}'
        alert = BugReportPage.criar_tarefa_arquivo_invalid(resumo, descricao, path_arquivo)
        assert "tamanho máximo de arquivo permitido" in alert

    @pytest.mark.parametrize("resumo, descricao", DadosTest.LISTA_OBRIGATORIO)
    @pytest.mark.parametrize("usuario, senha", DadosTest.LISTA_LOGIN)
    def test_criar_tarefa_obrigatoria(self, usuario, senha, resumo, descricao):
        self.loginPage = LoginPage(self.driver)
        myViewPage = self.loginPage.logar(usuario, senha)
        BugReportPage = myViewPage.ir_para_criar_tarefa()
        ViewTPage = BugReportPage.criar_tarefa_obrigatoria(resumo, descricao)
        assert "Operação realizada com sucesso." in BugReportPage.driver.page_source
        id = ViewTPage.get_id()
        assert ViewTPage.verificar_url(f'id={id}')
        BugReportPage = myViewPage.ir_para_criar_tarefa()
        ViewTPage = BugReportPage.criar_tarefa_obrigatoria(resumo, descricao)
        assert "Operação realizada com sucesso." in BugReportPage.driver.page_source
        id = ViewTPage.get_id()
        assert ViewTPage.verificar_url(f'id={id}')