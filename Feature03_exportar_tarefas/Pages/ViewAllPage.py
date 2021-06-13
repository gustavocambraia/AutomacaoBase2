from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class ViewAllPage(BasePage):

    EXPORTAR_CSV = (By.CSS_SELECTOR, '#bug_action > div > div.widget-body > div.widget-toolbox.padding-8.clearfix > div > div.btn-group.pull-left > a:nth-child(2)')
    EXPORTAR_EXCEL = (By.CSS_SELECTOR, '#bug_action > div > div.widget-body > div.widget-toolbox.padding-8.clearfix > div > div.btn-group.pull-left > a:nth-child(3)')

    def __init__(self, driver):
        super().__init__(driver)
    
    #Baixar CSV
    def baixar_csv(self):
        self.clicar(self.EXPORTAR_CSV)

    #Baixar EXCEL (xml)
    def baixar_excel(self):
        self.clicar(self.EXPORTAR_EXCEL)
