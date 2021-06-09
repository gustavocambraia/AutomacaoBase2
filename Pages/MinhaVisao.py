import string

from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
import random


class MinhaVisao(BasePage):
    VER_TAREFAS = (By.XPATH, '//*[@id="sidebar"]/ul/li[2]/a/span')  # Menu lateral "Ver Tarefas" no dashboard
    SELECIONAR_TAREFA = (By.XPATH, '//*[@id="buglist"]/tbody/tr[1]/td[4]/a')  # hiperlink com o n da tarefa no dashboard
    HEADER_DETALHES_TAREFA = (By.XPATH, r'/html/body/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/h4/text()')
    VER_DETALHES = (By.XPATH, '//*[@id="main-container"]/div[2]/div[2]/div/div[1]/div/div[1]/h4')
    BOTAO_ATUALIZAR = (By.XPATH, '//*[@id="main-container"]/div[2]/div[2]/div/div[1]/div/div[2]/'
                                 'div[2]/div/table/tfoot/tr/td/div/div[1]/form/fieldset/input[3]')
    BOTAO_ATUALIZAR_ENVIAR = (By.XPATH, '//*[@id="update_bug_form"]/div/div[3]/input')
    BOTAO_APAGAR = (By.XPATH, '//*[@id="main-container"]/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/'
                              'div/table/tfoot/tr/td/div/div[9]/form/fieldset/input[4]')
    BOTAO_APAGAR_CONFIRMAR = (By.XPATH, '//*[@id="action-group-div"]/form/div/div[2]/div[2]/input')
    CAMPO_DESCRICAO = (By.ID, "description")  # campo preenchível na parte de atualização
    CAMPO_NUMERO_TAREFA = (By.XPATH, '//*[@id="main-container"]/div[2]/div[2]/div/div[1]/div/div[2]/div[2]'
                                     '/div/table/tbody/tr[2]/td[1]')  # célula dos detalhes da tarefa
    DETALHE_DESCRICAO = (By.XPATH, '//*[@id="main-container"]/div[2]/div[2]/div/div[1]/div/div[2]/'
                                   'div[2]/div/table/tbody/tr[11]/td')  # célula dos detalhes da tarefa
    CAMPO_PESQUISAR_TAREFA = (By.XPATH, '//*[@id="nav-search"]/form/span/input')  # botão sup direito
    APPLICATION_ERROR = (By.XPATH, '//*[@id="main-container"]/div[2]/div[2]/div/div/div[2]/p[1]')

    def __init__(self, driver):
        super().__init__(driver)

    def visualizar_tarefas(self):
        """ Clica no botão "Ver Tarefas" na dashboard """
        self.do_click(self.VER_TAREFAS)
        return MinhaVisao(self.driver)

    def get_minhavisao_title(self, title):
        return self.get_title(title)

    def get_header_minhavisao(self):
        if self.is_visible(self.HEADER_DETALHES_TAREFA):
            return self.get_element_text(self.HEADER_DETALHES_TAREFA)

    def ver_detalhes(self):
        return self.is_visible(self.VER_DETALHES)

    def selecionar_tarefa(self):
        self.do_click(MinhaVisao.VER_TAREFAS)
        self.do_click(MinhaVisao.SELECIONAR_TAREFA)

    def numero_tarefa(self):
        return self.get_element_text(self.CAMPO_NUMERO_TAREFA)

    def confirmar_numero_tarefa(self):
        return self.get_text(self.SELECIONAR_TAREFA)

    def atualizar_tarefa(self):
        """ Clica no Botão Atualizar """
        self.do_click(MinhaVisao.BOTAO_ATUALIZAR)

    def realizar_atualizacao(self):
        """ Cria um novo texto randômico no campo "Descrição" da Tarefa """
        self.do_click(MinhaVisao.CAMPO_DESCRICAO)
        self.clear_text(self.CAMPO_DESCRICAO)
        letras = string.ascii_letters
        texto_rand = ''.join(random.choice(letras) for i in range(20))
        self.do_send_keys(self.CAMPO_DESCRICAO, texto_rand)
        self.do_click(self.BOTAO_ATUALIZAR_ENVIAR)
        return texto_rand

    def verifica_descricao(self):
        """ Grava em uma variável o texto em "Descrição" da tarefa """
        element = self.get_text(self.DETALHE_DESCRICAO)
        return element

    def deletar_tarefa(self):
        """ Aperta os botões para deletar tarefa """
        self.do_click(self.BOTAO_APAGAR)
        self.do_click(self.BOTAO_APAGAR_CONFIRMAR)

    def pesquisar_tarefa(self, num_tarefa):
        """ Digita no campo "Tarefa #" o numero da tarefa que deseja ser pesquisada """
        self.do_click(self.CAMPO_PESQUISAR_TAREFA)
        self.do_send_keys(self.CAMPO_PESQUISAR_TAREFA, num_tarefa)

    def pesquisar_tarefa_invalida(self):
        letras = string.ascii_letters
        texto_rand = ''.join(random.choice(letras) for i in range(5))
        self.do_click(self.CAMPO_PESQUISAR_TAREFA)
        self.do_send_keys(self.CAMPO_PESQUISAR_TAREFA, texto_rand)

    def verifica_tarefa_aberta(self, num_teste):
        """ Verifica se o número da tarefa selecionada pelo dashboard é o mesmo que o da tarefa aberta """
        num_tarefa = self.get_text(self.CAMPO_NUMERO_TAREFA)
        if num_tarefa == num_teste:
            return True
        else:
            return False

    def verifica_erro_pesquisa(self):
        erro = self.get_element_text(self.APPLICATION_ERROR)
        if erro == "APPLICATION ERROR #203":
            return True
