from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.BasePage import BasePage

class ProfEditPage(BasePage):
    PLATAFORMA = (By.NAME, 'platform')
    BTN_SALVAR = (By.CSS_SELECTOR, '#main-container > div.main-content > div.page-content > div > div > form > div > div.widget-body > div.widget-toolbox.padding-8.clearfix > input')

    def __init__(self, driver):
        super().__init__(driver)

    # Metodo de edição de plataforma do perfil
    def editar_plataforma(self, novaPlataforma):
        input = self.get_elemento(self.PLATAFORMA)
        input.clear()
        self.enviar_teclas(self.PLATAFORMA, novaPlataforma)
        self.clicar(self.BTN_SALVAR)
        WebDriverWait(self.driver, 10).until(EC.url_matches('https://mantis.saojudas.base2.com.br/account_prof_menu_page.php'))