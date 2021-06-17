from Pages.BasePage import BasePage
from Pages.ViewAllPage import ViewAllPage
from Config.config import DadosTest
from selenium.webdriver.common.by import By

class ViewTPage(BasePage):
    ID = (By.CSS_SELECTOR, '#main-container > div.main-content > div.page-content > div > div:nth-child(1) > div > div.widget-body > div.widget-main.no-padding > div > table > tbody > tr.bug-header-data > td.bug-id')
    VER_TAREFAS = (By.CSS_SELECTOR, '#sidebar > ul > li:nth-child(2) > a')

    def __init__(self, driver):
        super().__init__(driver)

    #Metodo retorno de ID da tarefa
    def get_id(self):
        id = self.get_texto_elemento(self.ID)
        idParseada = ''
        n = 0
        while(True):
            if id[n] != '0':
                idParseada = id[n:]
                break
            n += 1
        return idParseada

    #Ir para a pagina de ver tarefas
    def ir_para_ver_tarefas(self):
        if self.elemento_visivel(self.VER_TAREFAS):
            self.clicar(self.VER_TAREFAS)
            return ViewAllPage(self.driver)