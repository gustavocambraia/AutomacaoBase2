from Pages.AccountPage import AccountPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class MyViewPage(BasePage):
    USUARIO_MYVIEW =(By.CSS_SELECTOR, '#navbar-container > div.navbar-buttons.navbar-header.navbar-collapse.collapse > ul > li.grey > a > span')
    VER_TAREFAS = (By.CSS_SELECTOR, '#sidebar > ul > li:nth-child(2) > a')

    DROPDOWN = (By.CSS_SELECTOR, '#navbar-container > div.navbar-buttons.navbar-header.navbar-collapse.collapse > ul > li.grey > a')
    CONTA_BTN = (By.CSS_SELECTOR, '#navbar-container > div.navbar-buttons.navbar-header.navbar-collapse.collapse > ul > li.grey.open > ul > li:nth-child(1) > a')

    def __init__(self, driver):
        super().__init__(driver)

    #Retorna usuario logado
    def get_usuario_myview(self):
        if self.elemento_visivel(self.USUARIO_MYVIEW):
            return self.get_texto_elemento(self.USUARIO_MYVIEW)
            
    #Ir para a pagina de conta
    def ir_para_pagina_conta(self):
        if self.elemento_visivel(self.DROPDOWN):
            self.clicar(self.DROPDOWN)
            self.clicar(self.CONTA_BTN)
            WebDriverWait(self.driver, 10).until(EC.url_matches('https://mantis.saojudas.base2.com.br/account_page.php'))
            return AccountPage(self.driver)