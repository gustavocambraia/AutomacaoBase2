import string
import time

from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
import random


class TokenAPI(BasePage):
    BOTAO_CRIAR_TOKEN = (By.XPATH, '//*[@id="account-create-api-token-form"]/div/div[2]/div[2]/input')
    BOTAO_CONFIRMAR_TOKEN = (By.XPATH, '//*[@id="main-container"]/div[2]/div[2]/div/div/a')
    BOTAO_REVOGAR_TOKEN = (By.XPATH, '//*[@id="revoke-api-token-form"]/fieldset/input[3]')
    CAMPO_TEXTO_TOKEN = (By.XPATH, '//*[@id="token_name"]')


    def criar_token(self):
        letras = string.ascii_letters
        texto_rand = ''.join(random.choice(letras) for i in range(10))
        self.do_send_keys(self.CAMPO_TEXTO_TOKEN, texto_rand)
        self.do_click(self.BOTAO_CRIAR_TOKEN)
        self.do_click(self.BOTAO_CONFIRMAR_TOKEN)
        return texto_rand

    def deletar_token(self):
        self.do_click(self.BOTAO_REVOGAR_TOKEN)
        time.sleep(5)




