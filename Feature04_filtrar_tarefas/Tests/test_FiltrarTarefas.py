from selenium.webdriver.common.by import By
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Config.config import DadosTest
from datetime import datetime
import pytest
from time import sleep

class Test_Filtrar_Tarefas(BaseTest):

    @pytest.mark.parametrize("atribuido", DadosTest.LISTA_ATRIBUIDO)
    @pytest.mark.parametrize("usuario, senha", DadosTest.LISTA_LOGIN)
    def test_filtrar_tarefa_atribuido(self, usuario, senha, atribuido):
        self.loginPage = LoginPage(self.driver)
        myViewPage = self.loginPage.logar(usuario, senha)
        viewAllPage = myViewPage.ir_para_ver_tarefas()
        tabelasStatus = viewAllPage.filtrar_atribuido(atribuido)
        for td in tabelasStatus:
            assert atribuido in td.text
        if len(tabelasStatus) < 1:
            assert 0 == len(tabelasStatus)
        viewAllPage.deslogar()
        assert viewAllPage.driver.current_url == DadosTest.URL

    @pytest.mark.parametrize("gravidade", DadosTest.LISTA_GRAVIDADE)
    @pytest.mark.parametrize("usuario, senha", DadosTest.LISTA_LOGIN)
    def test_filtrar_tarefa_gravidade(self, usuario, senha, gravidade):
        self.loginPage = LoginPage(self.driver)
        myViewPage = self.loginPage.logar(usuario, senha)
        viewAllPage = myViewPage.ir_para_ver_tarefas()
        tabelasStatus = viewAllPage.filtrar_gravidade(gravidade)
        for td in tabelasStatus:
            assert gravidade in td.text
        if len(tabelasStatus) < 1:
            assert 0 == len(tabelasStatus)
        viewAllPage.deslogar()
        assert viewAllPage.driver.current_url == DadosTest.URL

    @pytest.mark.parametrize("estado", DadosTest.LISTA_ESTADO)
    @pytest.mark.parametrize("usuario, senha", DadosTest.LISTA_LOGIN)
    def test_filtrar_tarefa_estado(self, usuario, senha, estado):
        self.loginPage = LoginPage(self.driver)
        myViewPage = self.loginPage.logar(usuario, senha)
        viewAllPage = myViewPage.ir_para_ver_tarefas()
        tabelasStatus = viewAllPage.filtrar_estado(estado)
        for td in tabelasStatus:
            assert estado in td.text
        if len(tabelasStatus) < 1:
            assert 0 == len(tabelasStatus)
        viewAllPage.deslogar()
        assert viewAllPage.driver.current_url == DadosTest.URL

    @pytest.mark.parametrize("data_inicio, data_fim", DadosTest.LISTA_DATAS)
    @pytest.mark.parametrize("usuario, senha", DadosTest.LISTA_LOGIN)
    def test_filtrar_tarefa_estado(self, usuario, senha, data_inicio, data_fim):
        self.loginPage = LoginPage(self.driver)
        myViewPage = self.loginPage.logar(usuario, senha)
        viewAllPage = myViewPage.ir_para_ver_tarefas()
        data_inicio_parseada = data_inicio.split('/')
        data_fim_parseada = data_fim.split('/')
        tabelasStatus = viewAllPage.filtrar_data(data_inicio_parseada, data_fim_parseada)
        data_inicio_dt = f'{data_inicio_parseada[0]}-{data_inicio_parseada[1]}-{data_inicio_parseada[2]}'
        data_inicio_dt = datetime.strptime(data_inicio_dt, '%Y-%m-%d').date()
        data_fim_dt = f'{data_fim_parseada[0]}-{data_fim_parseada[1]}-{data_fim_parseada[2]}'
        data_fim_dt = datetime.strptime(data_fim_dt, '%Y-%m-%d').date()
        for td in tabelasStatus:
            data_tarefa = datetime.strptime(td.text, '%Y-%m-%d').date()
            assert data_tarefa >= data_inicio_dt and data_tarefa <= data_fim_dt
        if len(tabelasStatus) < 1:
            assert 0 == len(tabelasStatus)
        viewAllPage.deslogar()
        assert viewAllPage.driver.current_url == DadosTest.URL

    @pytest.mark.parametrize("monitor, filtroNome", DadosTest.LISTA_SAVE_FILTER)
    @pytest.mark.parametrize("usuario, senha", DadosTest.LISTA_LOGIN)
    def test_criar_filtro(self, usuario, senha, monitor, filtroNome):
        self.loginPage = LoginPage(self.driver)
        myViewPage = self.loginPage.logar(usuario, senha)
        viewAllPage = myViewPage.ir_para_ver_tarefas()
        opcoes = viewAllPage.criar_filtro(monitor, filtroNome)
        for opc in opcoes:
            if opc == filtroNome:
                assert filtroNome == opc
        viewAllPage.deslogar()
        assert viewAllPage.driver.current_url == DadosTest.URL    


