from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Config.config import DadosTest
import pytest

class Test_Filtrar_Tarefas(BaseTest):

    # Teste para criação de perfil
    @pytest.mark.parametrize("plataforma, so, versaoSo, descAdc", DadosTest.LISTA_NOVO_PERFIL)
    @pytest.mark.parametrize("usuario, senha", DadosTest.LISTA_LOGIN)
    def test_criar_perfil(
        self, usuario, senha, 
        plataforma, so, versaoSo, descAdc
        ):
        self.loginPage = LoginPage(self.driver)
        myViewPage = self.loginPage.logar(usuario, senha)
        accountPage = myViewPage.ir_para_pagina_conta()
        select = accountPage.criar_perfil(plataforma=plataforma, so=so, versaoSo=versaoSo, descAdc=descAdc or '')
        opcoes = select.options
        perfil = f'{plataforma} {so} {versaoSo}'
        for p in opcoes:
            if p.text == perfil:
                assert perfil == p.text

    # Teste de criação de teste sem preenchimento de campos obrigatórios
    @pytest.mark.parametrize("plataforma, so, versaoSo, descAdc", DadosTest.LISTA_NOVO_PERFIL_INVALIDO)
    @pytest.mark.parametrize("usuario, senha", DadosTest.LISTA_LOGIN)
    def test_criar_perfil_sem_obg(
        self, usuario, senha, 
        plataforma, so, versaoSo, descAdc
        ):
        self.loginPage = LoginPage(self.driver)
        myViewPage = self.loginPage.logar(usuario, senha)
        accountPage = myViewPage.ir_para_pagina_conta()
        accountPage.criar_perfil(plataforma=plataforma or '', so=so or '', versaoSo=versaoSo or '', descAdc=descAdc or '')
        msg = accountPage.verificar_required(accountPage.PLATAFORMA)
        assert msg in 'Preencha este campo.'
        msg = accountPage.verificar_required(accountPage.SO)
        assert msg in 'Preencha este campo.'
        msg = accountPage.verificar_required(accountPage.VERSAO_SO)
        assert msg in 'Preencha este campo.'

    # Teste de edição de perfil de SO
    @pytest.mark.parametrize("plataforma, so, versaoSo, descAdc, novaPlataforma", DadosTest.LISTA_EDITAR_PERFIL)
    @pytest.mark.parametrize("usuario, senha", DadosTest.LISTA_LOGIN)
    def test_editar_perfil(
        self, usuario, senha, 
        plataforma, so, versaoSo, descAdc, novaPlataforma
        ):
        self.loginPage = LoginPage(self.driver)
        myViewPage = self.loginPage.logar(usuario, senha)
        accountPage = myViewPage.ir_para_pagina_conta()
        select = accountPage.criar_perfil(plataforma=plataforma, so=so, versaoSo=versaoSo, descAdc=descAdc or '')
        perfil = f'{plataforma} {so} {versaoSo}'
        opcoes = select.options
        for p in opcoes:
            if p.text == perfil:
                assert perfil == p.text
        profEditPage = accountPage.editar_filtro(perfil)
        profEditPage.editar_plataforma(novaPlataforma)
        select = accountPage.pegar_select()
        perfil = f'{novaPlataforma} {so} {versaoSo}'
        opcoes = select.options
        for p in opcoes:
            if p.text == perfil:
                assert perfil == p.text




    

