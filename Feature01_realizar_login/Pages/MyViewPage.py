from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class MyViewPage(BasePage):
    USUARIO_MYVIEW =(By.CSS_SELECTOR, '#navbar-container > div.navbar-buttons.navbar-header.navbar-collapse.collapse > ul > li.grey > a > span')

    def __init__(self, driver):
        super().__init__(driver)

    # Metodo retorna usuario logado
    def get_usuario_myview(self):
        if self.elemento_visivel(self.USUARIO_MYVIEW):
            return self.get_texto_elemento(self.USUARIO_MYVIEW)