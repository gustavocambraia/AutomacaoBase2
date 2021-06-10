from Pages.MyViewPage import MyViewPage
from Pages.BasePage import BasePage
from Config.config import DadosTest
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    USUARIO = (By.ID, 'username')
    SENHA = (By.ID, 'password')
    LOGIN_BTN = (By.CSS_SELECTOR, 'input[type="submit"]')
    MSG_ERRO = (By.CSS_SELECTOR, '#main-container > div > div > div > div > div.alert.alert-danger > p')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DadosTest.URL)

    #Metodo logar
    def logar(self, usuario, senha):
        self.enviar_teclas(self.USUARIO, usuario)
        self.clicar(self.LOGIN_BTN)
        self.enviar_teclas(self.SENHA, senha)
        self.clicar(self.LOGIN_BTN)
        return MyViewPage(self.driver)