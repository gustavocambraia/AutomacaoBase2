from Pages.ViewTPage import ViewTPage
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import os.path

class BugReportPage(BasePage):

    BTN_PERFIL_CLOSED = (By.CSS_SELECTOR, '#profile_closed_link > i')
    DIV_OPEN = (By.CSS_SELECTOR, '#profile_open')
    PLATAFORMA = (By.XPATH, '//*[@id="profile_open"]/table/tbody/tr[1]/td/span/input[2]')
    SO = (By.NAME, 'os')
    VERSAO_SO = (By.NAME, 'os_build')
    RESUMO = (By.CSS_SELECTOR, '#summary')
    DESCRICAO = (By.CSS_SELECTOR, '#description')
    PASSOS = (By.NAME, 'steps_to_reproduce')
    INFO_ADC = (By.NAME, 'additional_info')
    TAG = (By.NAME, 'tag_string')
    BTN_CRIAR = (By.CSS_SELECTOR, '#report_bug_form > div > div.widget-body.dz-clickable > div.widget-toolbox.padding-8.clearfix > input')
    TABLE = (By.CSS_SELECTOR, '#profile_closed')

    ARQUIVO_DROP = (By.CLASS_NAME, 'dropzone')

    def __init__(self, driver):
        super().__init__(driver)

    #Metodo para criação de tarefa apenas com campos obrigatórios
    def criar_tarefa_obrigatoria(self, resumo='', descricao=''):
        self.enviar_teclas(self.RESUMO, resumo)
        self.enviar_teclas(self.DESCRICAO, descricao)
        self.clicar(self.BTN_CRIAR)
        return ViewTPage(self.driver)

    #Metodo para a criação de tarefa prenchendo todos os campos de texto
    def criar_tarefa_todos_inputs(
        self, resumo, 
        descricao, plataforma, 
        so, versaoSo, 
        passos, infoAdc, tag):
        self.enviar_teclas(self.RESUMO, resumo)
        self.enviar_teclas(self.DESCRICAO, descricao)
        self.enviar_teclas(self.PASSOS, passos)
        self.enviar_teclas(self.INFO_ADC, infoAdc)
        self.enviar_teclas(self.TAG, tag)
        try:
            if 'none' in self.get_style_elemento(self.DIV_OPEN):
                if self.elemento_visivel(self.BTN_PERFIL_CLOSED):
                    elemento = self.get_elemento(self.BTN_PERFIL_CLOSED)
                    self.driver.execute_script("arguments[0].click();", elemento)
        finally:
            self.enviar_teclas(self.PLATAFORMA, plataforma)
            self.enviar_teclas(self.SO, so)
            self.enviar_teclas(self.VERSAO_SO, versaoSo)
            self.clicar(self.BTN_CRIAR)
        return ViewTPage(self.driver)

    #Metodo para criação de tarefa com arquivo valido
    def criar_tarefa_arquivo_valid(self, resumo, descricao, arquivo):
        self.enviar_teclas(self.RESUMO, resumo)
        self.enviar_teclas(self.DESCRICAO, descricao)
        elemento = self.get_elemento(self.ARQUIVO_DROP)
        self.enviar_arquivo(elemento, arquivo)
        self.clicar(self.BTN_CRIAR)
        return ViewTPage(self.driver)

    #Metodo para criação de tarefa com arquivo invalido
    def criar_tarefa_arquivo_invalid(self, resumo, descricao, arquivo):
        self.enviar_teclas(self.RESUMO, resumo)
        self.enviar_teclas(self.DESCRICAO, descricao)
        elemento = self.get_elemento(self.ARQUIVO_DROP)
        self.enviar_arquivo(elemento, arquivo)
        alert = self.get_alert()
        texto = alert.text
        alert.accept()
        return texto


