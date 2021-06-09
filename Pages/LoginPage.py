from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage
from Pages.MinhaVisao import MinhaVisao
from Pages.TokenAPI import TokenAPI


class LoginPage(BasePage):

    """ By locators """
    EMAIL = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login-form"]/fieldset/input[2]')
    PASSWORD_BUTTON = (By.XPATH, '//*[@id="login-form"]/fieldset/input[3]')
    LINK_NOVA_CONTA = (By.LINK_TEXT, 'criar uma nova conta')
    IR_TAREFAS = (By.XPATH, '//*[@id="sidebar"]/ul/li[2]/a/span')
    BOTAO_MENU = (By.XPATH, '//*[@id="navbar-container"]/div[2]/ul/li[2]/a/span')
    BOTAO_MINHA_CONTA = (By.XPATH, '//*[@id="navbar-container"]/div[2]/ul/li[2]/ul/li[1]/a')
    BOTAO_TOKEN_API = (By.XPATH, '//*[@id="main-container"]/div[2]/div[2]/div/ul/li[5]/a')

    """ Construtor da classe """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """ Ações da Página """

    def get_login_page_title(self, title):
        """ Obter título da página """
        return self.get_title()

    def is_signup_link_exist(self):
        """ Verificar link para criar usuário """
        return self.is_visible(self.LINK_NOVA_CONTA)

    def do_login_homepage(self, username, password):
        """ Função para realizar login em homepage """
        self.do_send_keys(self.EMAIL, username)
        self.do_click(self.LOGIN_BUTTON)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.PASSWORD_BUTTON)
        return HomePage(self.driver)

    def do_login_tarefas(self, username, password):
        """ Função para realizar login em tarefas """
        self.do_send_keys(self.EMAIL, username)
        self.do_click(self.LOGIN_BUTTON)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.PASSWORD_BUTTON)
        self.do_click(self.IR_TAREFAS)
        return MinhaVisao(self.driver)

    def do_login_api(self, username, password):
        """ Função para realizar login em token API """
        self.do_send_keys(self.EMAIL, username)
        self.do_click(self.LOGIN_BUTTON)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.PASSWORD_BUTTON)
        self.do_click(self.BOTAO_MENU)
        self.do_click(self.BOTAO_MINHA_CONTA)
        self.do_click(self.BOTAO_TOKEN_API)
        return TokenAPI(self.driver)





