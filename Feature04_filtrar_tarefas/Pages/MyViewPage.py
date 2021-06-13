from Pages.ViewAllPage import ViewAllPage
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class MyViewPage(BasePage):
    USUARIO_MYVIEW =(By.CSS_SELECTOR, '#navbar-container > div.navbar-buttons.navbar-header.navbar-collapse.collapse > ul > li.grey > a > span')
    CRIAR_TAREFA = (By.CSS_SELECTOR, '#sidebar > ul > li:nth-child(3) > a')
    VER_TAREFAS = (By.CSS_SELECTOR, '#sidebar > ul > li:nth-child(2) > a')

    def __init__(self, driver):
        super().__init__(driver)

    #Retorna usuario logado
    def get_usuario_myview(self):
        if self.elemento_visivel(self.USUARIO_MYVIEW):
            return self.get_texto_elemento(self.USUARIO_MYVIEW)
            
    #Ir para a pagina de ver tarefas
    def ir_para_ver_tarefas(self):
        if self.elemento_visivel(self.VER_TAREFAS):
            self.clicar(self.VER_TAREFAS)
            return ViewAllPage(self.driver)