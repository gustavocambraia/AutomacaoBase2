from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ViewAllPage(BasePage):

    ANCORA_ATRIBUIDO = (By.CSS_SELECTOR, '#handler_id_filter')
    SELECT_ATRIBUIDO = (By.CSS_SELECTOR, '#handler_id_filter_target > select')
    ANCORA_MONITORADO = (By.CSS_SELECTOR, '#user_monitor_filter')
    SELECT_MONITORADO = (By.CSS_SELECTOR, '#user_monitor_filter_target > select')
    ANCORA_GRAVIDADE = (By.CSS_SELECTOR, '#show_severity_filter')
    SELECT_GRAVIDADE = (By.CSS_SELECTOR, '#show_severity_filter_target > select')
    ANCORA_ESTADO = (By.CSS_SELECTOR, '#show_status_filter')
    SELECT_ESTADO = (By.CSS_SELECTOR, '#show_status_filter_target > select')
    ANCORA_DATAS = (By.CSS_SELECTOR, '#do_filter_by_last_updated_date_filter')
    BTN_DATA = (By.CSS_SELECTOR, '#do_filter_by_last_updated_date_filter_target > table > tbody > tr:nth-child(1) > td > label > span')
    SELECT_DATA_INI_ANO = (By.CSS_SELECTOR, '#do_filter_by_last_updated_date_filter_target > table > tbody > tr:nth-child(2) > td.nowrap > select:nth-child(1)')
    SELECT_DATA_INI_MES = (By.CSS_SELECTOR, '#do_filter_by_last_updated_date_filter_target > table > tbody > tr:nth-child(2) > td.nowrap > select:nth-child(2)')
    SELECT_DATA_INI_DIA = (By.CSS_SELECTOR, '#do_filter_by_last_updated_date_filter_target > table > tbody > tr:nth-child(2) > td.nowrap > select:nth-child(3)')
    SELECT_DATA_FIM_ANO = (By.CSS_SELECTOR, '#do_filter_by_last_updated_date_filter_target > table > tbody > tr:nth-child(3) > td:nth-child(2) > select:nth-child(1)')
    SELECT_DATA_FIM_MES = (By.CSS_SELECTOR, '#do_filter_by_last_updated_date_filter_target > table > tbody > tr:nth-child(3) > td:nth-child(2) > select:nth-child(2)')
    SELECT_DATA_FIM_DIA = (By.CSS_SELECTOR, '#do_filter_by_last_updated_date_filter_target > table > tbody > tr:nth-child(3) > td:nth-child(2) > select:nth-child(3)')
    SELECT_FILTROS_CRIADOS = (By.CSS_SELECTOR, '#filter-queries-form > label > select')
    BTN_REDEFINIR = (By.CSS_SELECTOR, '#filter > div.widget-body > div > div > div > div > a:nth-child(1)')
    BTN_SALVAR = (By.CSS_SELECTOR, '#filter > div.widget-body > div > div > div > div > a:nth-child(2)')
    BTN_FILTRAR = (By.CSS_SELECTOR, '#filters_form_open > div.widget-toolbox.padding-8.clearfix > div > div > input.btn.btn-primary.btn-sm.btn-white.btn-round.no-float')
    BTN_IMPRIMIR = (By.CSS_SELECTOR, '#bug_action > div > div.widget-body > div.widget-toolbox.padding-8.clearfix > div > div.btn-group.pull-left > a:nth-child(1)')
    BTN_SALVAR_FILTRONOME = (By.CSS_SELECTOR, '#save-filter > div.widget-body > div > form.form-inline > input.btn.btn-primary.btn-white.btn-round')
    ESTADO_TD = (By.CLASS_NAME, 'column-status')
    GRAVIDADE_TD = (By.CLASS_NAME, 'column-severity')
    DATA_TD = (By.CLASS_NAME, 'column-last-modified')
    INPUT_CRIAR_FILTRO = (By.CSS_SELECTOR, '#save-filter > div.widget-body > div > form.form-inline > input.input-sm')

    DROPDOWN = (By.CSS_SELECTOR, '#navbar-container > div.navbar-buttons.navbar-header.navbar-collapse.collapse > ul > li.grey > a')
    SAIR = (By.CSS_SELECTOR, '#navbar-container > div.navbar-buttons.navbar-header.navbar-collapse.collapse > ul > li.grey.open > ul > li:nth-child(4) > a')

    def __init__(self, driver):
        super().__init__(driver)

    def filtrar_atribuido(self, valor):
        self.clicar(self.BTN_REDEFINIR)
        self.clicar(self.ANCORA_ATRIBUIDO)
        select = Select(self.get_elemento(self.SELECT_ATRIBUIDO))
        select.select_by_visible_text(valor)
        self.clicar(self.BTN_FILTRAR)
        tabelasStatus = self.get_elementos(self.ESTADO_TD)
        del tabelasStatus[0]
        return tabelasStatus

    def filtrar_estado(self, valor):
        self.clicar(self.BTN_REDEFINIR)
        self.clicar(self.ANCORA_ESTADO)
        select = Select(self.get_elemento(self.SELECT_ESTADO))
        select.select_by_visible_text(valor)
        self.clicar(self.BTN_FILTRAR)
        tabelasStatus = self.get_elementos(self.ESTADO_TD)
        del tabelasStatus[0]
        return tabelasStatus

    def filtrar_gravidade(self, valor):
        self.clicar(self.BTN_REDEFINIR)
        self.clicar(self.ANCORA_GRAVIDADE)
        select = Select(self.get_elemento(self.SELECT_GRAVIDADE))
        select.select_by_visible_text(valor)
        self.clicar(self.BTN_FILTRAR)
        tabelasStatus = self.get_elementos(self.GRAVIDADE_TD)
        del tabelasStatus[0]
        return tabelasStatus

    def filtrar_data(self, data_inicio_parseada, data_fim_parseada):
        self.clicar(self.BTN_REDEFINIR)
        self.clicar(self.ANCORA_DATAS)
        self.clicar(self.BTN_DATA)
        select_ini_ano = Select(self.get_elemento(self.SELECT_DATA_INI_ANO))
        select_ini_mes = Select(self.get_elemento(self.SELECT_DATA_INI_MES))
        select_ini_dia = Select(self.get_elemento(self.SELECT_DATA_INI_DIA))
        select_fim_ano = Select(self.get_elemento(self.SELECT_DATA_FIM_ANO))
        select_fim_mes = Select(self.get_elemento(self.SELECT_DATA_FIM_MES))
        select_fim_dia = Select(self.get_elemento(self.SELECT_DATA_FIM_DIA))
        select_ini_ano.select_by_visible_text(data_inicio_parseada[0])
        select_ini_mes.select_by_value(data_inicio_parseada[1])
        select_ini_dia.select_by_visible_text(data_inicio_parseada[2])
        select_fim_ano.select_by_visible_text(data_fim_parseada[0])
        select_fim_mes.select_by_value(data_fim_parseada[1])
        select_fim_dia.select_by_visible_text(data_fim_parseada[2])
        self.clicar(self.BTN_FILTRAR)
        tabelasStatus = self.get_elementos(self.DATA_TD)
        del tabelasStatus[0]
        return tabelasStatus

    def criar_filtro(self, monitor, filtroNome):
        self.clicar(self.BTN_REDEFINIR)
        self.clicar(self.ANCORA_MONITORADO)
        selectMonitor = Select(self.get_elemento(self.SELECT_MONITORADO))
        selectMonitor.select_by_visible_text(monitor)
        self.clicar(self.BTN_FILTRAR)
        self.clicar(self.BTN_SALVAR)
        WebDriverWait(self.driver, 10).until(EC.url_matches('https://mantis.saojudas.base2.com.br/query_store_page.php'))
        self.enviar_teclas(self.INPUT_CRIAR_FILTRO, filtroNome)
        self.clicar(self.BTN_SALVAR_FILTRONOME)
        selectFiltros = Select(self.get_elemento(self.SELECT_FILTROS_CRIADOS))
        options = selectFiltros.options
        return options

    def deslogar(self):
        self.clicar(self.DROPDOWN)
        self.clicar(self.SAIR)
        WebDriverWait(self.driver, 10).until(EC.url_matches('https://mantis.saojudas.base2.com.br/login_page.php'))