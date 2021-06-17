from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.ViewTPage import ViewTPage
from selenium.webdriver.common.by import By
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Config.config import DadosTest
from time import sleep
import pytest

class Test_Criar_Tarefa(BaseTest):

    # Criar tarefa preenchendo apenas campos requeridos
    @pytest.mark.parametrize("resumo, descricao", DadosTest.LISTA_OBRIGATORIO)
    @pytest.mark.parametrize("usuario, senha", DadosTest.LISTA_LOGIN)
    def test_criar_tarefa_obrigatoria(self, usuario, senha, resumo, descricao):
        self.loginPage = LoginPage(self.driver)
        myViewPage = self.loginPage.logar(usuario, senha)
        bugReportPage = myViewPage.ir_para_criar_tarefa()
        viewTPage = bugReportPage.criar_tarefa_obrigatoria(resumo, descricao)
        assert "Operação realizada com sucesso." in bugReportPage.driver.page_source
        id = viewTPage.get_id()
        assert viewTPage.verificar_url(f'id={id}')

    # Criar tarefa preenchendo campos input
    @pytest.mark.parametrize("resumo, descricao, plataforma, so, versaoSo, passos, infoAdc, tag", DadosTest.LISTA_TODOS)
    @pytest.mark.parametrize("usuario, senha", DadosTest.LISTA_LOGIN)
    def test_criar_tarefa_todos_inputs(
        self, usuario, senha, resumo, 
        descricao, plataforma, so, 
        versaoSo, passos, infoAdc, tag):
        self.loginPage = LoginPage(self.driver)
        myViewPage = self.loginPage.logar(usuario, senha)
        bugReportPage = myViewPage.ir_para_criar_tarefa()
        viewTPage = bugReportPage.criar_tarefa_todos_inputs(resumo, 
        descricao, plataforma, so, 
        versaoSo, passos, infoAdc, tag)
        assert "Operação realizada com sucesso." in bugReportPage.driver.page_source
        id = viewTPage.get_id()
        assert viewTPage.verificar_url(f'id={id}')

    # Criar tarefa sem preencher nenhum campo
    @pytest.mark.parametrize("usuario, senha", DadosTest.LISTA_LOGIN)
    def test_criar_tarefa_preencher_nenhum_campo(self, usuario, senha):
        self.loginPage = LoginPage(self.driver)
        myViewPage = self.loginPage.logar(usuario, senha)
        bugReportPage = myViewPage.ir_para_criar_tarefa()
        bugReportPage.criar_tarefa_obrigatoria()
        msg = bugReportPage.verificar_required(bugReportPage.RESUMO)
        assert msg in 'Preencha este campo.'
        msg = bugReportPage.verificar_required(bugReportPage.DESCRICAO)
        assert msg in 'Preencha este campo.'

    # Anexar arquivo válido
    @pytest.mark.parametrize("resumo, descricao, arquivo", DadosTest.LISTA_ARQUIVO_VALID)
    @pytest.mark.parametrize("usuario, senha", DadosTest.LISTA_LOGIN)
    def test_criar_tarefa_arquivo_valido(self, usuario, senha, resumo, descricao, arquivo):
        self.loginPage = LoginPage(self.driver)
        myViewPage = self.loginPage.logar(usuario, senha)
        bugReportPage = myViewPage.ir_para_criar_tarefa()
        path_arquivo = f'C:\\Users\\Lorenzo\\Documents\\Aulas Faculdade\\ProjetoUC\\Feature02_criar_tarefa\\teste.pdf'
        viewTPage = bugReportPage.criar_tarefa_arquivo_valid(resumo, descricao, path_arquivo)
        WebDriverWait(bugReportPage.driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.alert.alert-success'), "Operação realizada com sucesso"))
        assert "Operação realizada com sucesso." in bugReportPage.driver.page_source
        id = viewTPage.get_id()
        assert viewTPage.verificar_url(f'id={id}')

    # Anexar arquivo excedendo tamanho máximo
    @pytest.mark.parametrize("resumo, descricao, arquivo", DadosTest.LISTA_ARQUIVO_INVALID)
    @pytest.mark.parametrize("usuario, senha", DadosTest.LISTA_LOGIN)
    def test_criar_tarefa_arquivo_invalido(self, usuario, senha, resumo, descricao, arquivo):
        self.loginPage = LoginPage(self.driver)
        myViewPage = self.loginPage.logar(usuario, senha)
        bugReportPage = myViewPage.ir_para_criar_tarefa()
        path_arquivo = f'C:\\Users\\Lorenzo\\Documents\\Aulas Faculdade\\ProjetoUC\\Feature02_criar_tarefa\\{arquivo}'
        alert = bugReportPage.criar_tarefa_arquivo_invalid(resumo, descricao, path_arquivo)
        assert "tamanho máximo de arquivo permitido" in alert

    # Criar tarefas em sequência
    @pytest.mark.parametrize("resumo, descricao", DadosTest.LISTA_OBRIGATORIO)
    @pytest.mark.parametrize("usuario, senha", DadosTest.LISTA_LOGIN)
    def test_criar_tarefa_obrigatoria(self, usuario, senha, resumo, descricao):
        self.loginPage = LoginPage(self.driver)
        myViewPage = self.loginPage.logar(usuario, senha)
        bugReportPage = myViewPage.ir_para_criar_tarefa()
        viewTPage = bugReportPage.criar_tarefa_obrigatoria(resumo, descricao)
        assert "Operação realizada com sucesso." in bugReportPage.driver.page_source
        id = viewTPage.get_id()
        assert viewTPage.verificar_url(f'id={id}')
        bugReportPage = myViewPage.ir_para_criar_tarefa()
        viewTPage = bugReportPage.criar_tarefa_obrigatoria(resumo, descricao)
        assert "Operação realizada com sucesso." in bugReportPage.driver.page_source
        id = viewTPage.get_id()
        assert viewTPage.verificar_url(f'id={id}')