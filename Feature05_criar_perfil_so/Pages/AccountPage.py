from Pages.ProfEditPage import ProfEditPage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.BasePage import BasePage

class AccountPage(BasePage):

    ABA_PERFIS = (By.CSS_SELECTOR, '#main-container > div.main-content > div.page-content > div > ul > li:nth-child(4) > a')
    PLATAFORMA = (By.CSS_SELECTOR, '#platform')
    SO = (By.CSS_SELECTOR, '#os')
    VERSAO_SO = (By.CSS_SELECTOR, '#os-version')
    DESC_ADICIONAL = (By.CSS_SELECTOR, '#description')

    BTN_ADC_PERFIL = (By.CSS_SELECTOR, '#account-profile-form > fieldset > div > div.widget-body > div.widget-toolbox.padding-8.clearfix > input')

    SELECT_PERFILS = (By.XPATH, '//*[@id="select-profile"]')
    SPAN_EDITAR = (By.CSS_SELECTOR, '#account-profile-update-form > div > div.widget-body > div.widget-main.no-padding > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > label > span')
    BTN_SALVAR_PERFIL = (By.CSS_SELECTOR, '#account-profile-update-form > div > div.widget-body > div.widget-toolbox.padding-8.clearfix > input')

    ANCORA_CRIAR_TAREFA = (By.CSS_SELECTOR, '#sidebar > ul > li:nth-child(3) > a')

    def __init__(self, driver):
        super().__init__(driver)

    def pegar_select(self):
        select = Select(self.get_elemento(self.SELECT_PERFILS))
        return select

    def criar_perfil(self, plataforma, so, versaoSo, descAdc):
        self.clicar(self.ABA_PERFIS)
        WebDriverWait(self.driver, 10).until(EC.url_matches('https://mantis.saojudas.base2.com.br/account_prof_menu_page.php'))
        self.enviar_teclas(self.PLATAFORMA, texto=plataforma)
        self.enviar_teclas(self.SO, texto=so)
        self.enviar_teclas(self.VERSAO_SO, texto=versaoSo)
        self.enviar_teclas(self.DESC_ADICIONAL, texto=descAdc)
        self.clicar(self.BTN_ADC_PERFIL)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'body')))
        select = self.pegar_select()
        return select

    def editar_filtro(self, perfil):
        select = self.pegar_select()
        select.select_by_visible_text(perfil)
        self.clicar(self.SPAN_EDITAR)
        self.clicar(self.BTN_SALVAR_PERFIL)
        return ProfEditPage(self.driver)