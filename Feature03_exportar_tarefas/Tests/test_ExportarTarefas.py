from Pages.ViewTPage import ViewTPage
from Pages.ViewAllPage import ViewAllPage
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Config.config import DadosTest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import pytest
from time import sleep

class Test_Exportar_Tarefas(BaseTest):

    # Test Exportar tarefas para o Excel
    @pytest.mark.parametrize("resumo, descricao", DadosTest.LISTA_OBRIGATORIO)
    @pytest.mark.parametrize("usuario, senha", DadosTest.LISTA_LOGIN)
    def test_exportar_tarefas_csv(self, usuario, senha, resumo, descricao):
        for root, dirs, files in os.walk(DadosTest.PATH_FILES):
            for file in files:
                file_path = os.path.join(DadosTest.PATH_FILES, file)
                if os.path.exists(file_path) and '.csv' in file:
                    os.remove(file_path)
        self.loginPage = LoginPage(self.driver)
        myViewPage = self.loginPage.logar(usuario, senha)
        BugReportPage = myViewPage.ir_para_criar_tarefa()
        ViewTPage = BugReportPage.criar_tarefa_obrigatoria(resumo, descricao)
        assert "Operação realizada com sucesso." in BugReportPage.driver.page_source
        id = ViewTPage.get_id()
        assert ViewTPage.verificar_url(f'id={id}')
        ViewAllPage = ViewTPage.ir_para_ver_tarefas()
        ViewAllPage.baixar_csv()
        resp = WebDriverWait(ViewAllPage.driver, 10).until(EC.url_changes('https://mantis.saojudas.base2.com.br/csv_export.php'))
        sleep(7)
        assert True == resp

    # Test Exportar tarefas para o CSV
    @pytest.mark.parametrize("resumo, descricao", DadosTest.LISTA_OBRIGATORIO)
    @pytest.mark.parametrize("usuario, senha", DadosTest.LISTA_LOGIN)
    def test_exportar_tarefas_excel(self, usuario, senha, resumo, descricao):
        for root, dirs, files in os.walk(DadosTest.PATH_FILES):
            for file in files:
                file_path = os.path.join(DadosTest.PATH_FILES, file)
                if os.path.exists(file_path) and '.xml' in file:
                    os.remove(file_path)
        self.loginPage = LoginPage(self.driver)
        myViewPage = self.loginPage.logar(usuario, senha)
        BugReportPage = myViewPage.ir_para_criar_tarefa()
        ViewTPage = BugReportPage.criar_tarefa_obrigatoria(resumo, descricao)
        assert "Operação realizada com sucesso." in BugReportPage.driver.page_source
        id = ViewTPage.get_id()
        assert ViewTPage.verificar_url(f'id={id}')
        ViewAllPage = ViewTPage.ir_para_ver_tarefas()
        ViewAllPage.baixar_excel()
        resp = WebDriverWait(ViewAllPage.driver, 10).until(EC.url_changes('https://mantis.saojudas.base2.com.br/excel_xml_export.php'))
        sleep(7)
        assert True == resp
    
