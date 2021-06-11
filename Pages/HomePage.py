from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Pages.MinhaVisao import MinhaVisao


class HomePage(BasePage):

    HEADER = (By.XPATH, '//*[@id="navbar-container"]/div[1]/a/span')
    ACCOUNT_NAME = (By.CSS_SELECTOR, "user-info")
    SETTINGS_ICON = (By.XPATH, '//*[@id="navbar-container"]/div[2]/ul/li[2]/ul/li[1]/a')

    BOTAO_MENU = (By.XPATH, '//*[@id="navbar-container"]/div[2]/ul/li[2]/a/span')
    BOTAO_MINHA_CONTA = (By.XPATH, '//*[@id="navbar-container"]/div[2]/ul/li[2]/ul/li[1]/a')
    BOTAO_PROSSEGUIR_CADASTRO = (By.XPATH, '//*[@id="main-container"]/div[2]/div[2]/div/div/div/div[2]/div/a')
    BOTAO_ATUALIZAR_USUARIO = (By.XPATH, '//*[@id="account-update-form"]/div[1]/div[2]/div[2]/input')
    BOTAO_SENHA_ATUAL = (By.ID, 'password-current')
    BOTAO_NOVA_SENHA = (By.ID, 'password')
    BOTAO_CONFIRMAR_SENHA = (By.ID, 'password-confirm')

    def __init__(self, driver):
        super().__init__(driver)

    def get_home_page_title(self, title):
        return self.get_title(title)

    def is_settings_icon_exist(self):
        return self.is_visible(self.SETTINGS_ICON)

    def get_header_value(self):
        if self.is_visible(self.HEADER):
            return self.get_element_text(self.HEADER)

    def get_account_name_value(self):
        if self.is_visible(self.ACCOUNT_NAME):
            return self.get_element_text(self.ACCOUNT_NAME)

    def clicar_tarefas(self):
        return MinhaVisao(self)

    def reverter_senha(self):
        self.do_click(self.BOTAO_MENU)
        self.do_click(self.BOTAO_MINHA_CONTA)
        self.do_click(self.BOTAO_SENHA_ATUAL)
        self.do_send_keys(self.BOTAO_SENHA_ATUAL, "gusmantis1")
        self.do_click(self.BOTAO_NOVA_SENHA)
        self.do_send_keys(self.BOTAO_NOVA_SENHA, "gusmantis")
        self.do_click(self.BOTAO_CONFIRMAR_SENHA)
        self.do_send_keys(self.BOTAO_CONFIRMAR_SENHA, "gusmantis")
        self.do_click(self.BOTAO_ATUALIZAR_USUARIO)
        self.do_click(self.BOTAO_PROSSEGUIR_CADASTRO)
