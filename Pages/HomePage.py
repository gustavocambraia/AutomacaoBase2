from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Pages.MinhaVisao import MinhaVisao


class HomePage(BasePage):

    HEADER = (By.XPATH, '//*[@id="navbar-container"]/div[1]/a/span')
    ACCOUNT_NAME = (By.CSS_SELECTOR, "user-info")
    SETTINGS_ICON = (By.XPATH, '//*[@id="navbar-container"]/div[2]/ul/li[2]/ul/li[1]/a')

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