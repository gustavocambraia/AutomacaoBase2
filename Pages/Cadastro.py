import string
import random
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class Cadastro(BasePage):

    BOTAO_MENU = (By.XPATH, '//*[@id="navbar-container"]/div[2]/ul/li[2]/a/span')
    BOTAO_MINHA_CONTA = (By.XPATH, '//*[@id="navbar-container"]/div[2]/ul/li[2]/ul/li[1]/a')
    BOTAO_PROSSEGUIR_CADASTRO = (By.XPATH, '//*[@id="main-container"]/div[2]/div[2]/div/div/div/div[2]/div/a')
    CAMPO_PREENCHER_EMAIL = (By.ID, 'email-field')
    CAMPO_NOME_VERDADEIRO = (By.ID, 'realname')
    BOTAO_ATUALIZAR_USUARIO = (By.XPATH, '//*[@id="account-update-form"]/div[1]/div[2]/div[2]/input')
    BOTAO_SENHA_ATUAL = (By.ID, 'password-current')
    BOTAO_NOVA_SENHA = (By.ID, 'password')
    BOTAO_CONFIRMAR_SENHA = (By.ID, 'password-confirm')
    MENSAGEM_ERRO_SENHA = (By.XPATH, '//*[@id="main-container"]/div[2]/div[2]/div/div/div[2]/p[1]')

    def cadastrar_email(self):
        """ Cadastra um novo e-mail com texto random e retorna uma string no formato random@teste.gmail.com """
        letras = string.ascii_letters
        texto = ''.join(random.choice(letras) for i in range(10))
        self.do_click(self.CAMPO_PREENCHER_EMAIL)
        self.clear_text(self.CAMPO_PREENCHER_EMAIL)
        self.do_send_keys(self.CAMPO_PREENCHER_EMAIL, texto+"@teste.gmail.com")
        email = self.get_value(self.CAMPO_PREENCHER_EMAIL)
        self.do_click(self.BOTAO_ATUALIZAR_USUARIO)
        self.do_click(self.BOTAO_PROSSEGUIR_CADASTRO)
        return email

    def verificar_email_atualizado(self):
        """ Armazena como string o e-mail na tela """
        self.do_click(self.BOTAO_MENU)
        self.do_click(self.BOTAO_MINHA_CONTA)
        e_mail_tela = self.get_value(self.CAMPO_PREENCHER_EMAIL)
        return e_mail_tela

    def reverter_email(self):
        """ Reverte ao e-mail original após a realização do teste """
        self.do_click(self.CAMPO_PREENCHER_EMAIL)
        self.clear_text(self.CAMPO_PREENCHER_EMAIL)
        self.do_send_keys(self.CAMPO_PREENCHER_EMAIL, "gustavogiraldes.2113@aluno.saojudas.com")
        self.do_click(self.BOTAO_ATUALIZAR_USUARIO)
        self.do_click(self.BOTAO_PROSSEGUIR_CADASTRO)

    def criar_nome_random(self):
        """ Função genérica para criar nome e sobrenome com random """
        nomes = string.ascii_letters
        primeiro_nome = ''.join(random.choice(nomes) for i in range(10))
        sobrenome = ''.join(random.choice(nomes) for i in range(10))
        nome_real = primeiro_nome + " " + sobrenome
        return nome_real

    def alterar_nome_real(self):
        """ Função para alterar o nome real no cadastro """
        self.do_click(self.CAMPO_NOME_VERDADEIRO)
        self.clear_text(self.CAMPO_NOME_VERDADEIRO)
        nome = self.criar_nome_random()
        self.do_send_keys(self.CAMPO_NOME_VERDADEIRO, nome)
        self.do_click(self.BOTAO_ATUALIZAR_USUARIO)
        self.do_click(self.BOTAO_PROSSEGUIR_CADASTRO)
        return nome

    def verificar_nome_alterado(self):
        """ Armazena como string o nome na tela """
        self.do_click(self.BOTAO_MENU)
        self.do_click(self.BOTAO_MINHA_CONTA)
        nome_tela = self.get_value(self.CAMPO_NOME_VERDADEIRO)
        return nome_tela

    def reverter_nome_real(self):
        """ Reverte ao e-mail original após a realização do teste """
        self.do_click(self.CAMPO_NOME_VERDADEIRO)
        self.clear_text(self.CAMPO_NOME_VERDADEIRO)
        self.do_send_keys(self.CAMPO_NOME_VERDADEIRO, "Gustavo Cambraia Giraldes")
        self.do_click(self.BOTAO_ATUALIZAR_USUARIO)
        self.do_click(self.BOTAO_PROSSEGUIR_CADASTRO)

    def alterar_senha(self):
        """ Insere a senha atual e atualiza para a senha nova """
        self.do_click(self.BOTAO_SENHA_ATUAL)
        self.do_send_keys(self.BOTAO_SENHA_ATUAL, "gusmantis")
        self.do_click(self.BOTAO_NOVA_SENHA)
        self.do_send_keys(self.BOTAO_NOVA_SENHA, "gusmantis1")
        self.do_click(self.BOTAO_CONFIRMAR_SENHA)
        self.do_send_keys(self.BOTAO_CONFIRMAR_SENHA, "gusmantis1")
        self.do_click(self.BOTAO_ATUALIZAR_USUARIO)
        self.do_click(self.BOTAO_PROSSEGUIR_CADASTRO)

    def alterar_senha(self):
        """ Insere a senha atual e atualiza para a senha nova """
        self.do_click(self.BOTAO_SENHA_ATUAL)
        self.do_send_keys(self.BOTAO_SENHA_ATUAL, "gusmantis")
        self.do_click(self.BOTAO_NOVA_SENHA)
        self.do_send_keys(self.BOTAO_NOVA_SENHA, "gusmantis1")
        self.do_click(self.BOTAO_CONFIRMAR_SENHA)
        self.do_send_keys(self.BOTAO_CONFIRMAR_SENHA, "gusmantis1")
        self.do_click(self.BOTAO_ATUALIZAR_USUARIO)
        self.do_click(self.BOTAO_PROSSEGUIR_CADASTRO)

    def alterar_senha_invalido(self):
        """ Insere senhas novas iguais, porém não preenche o campo de senha atual """
        self.do_click(self.BOTAO_NOVA_SENHA)
        self.do_send_keys(self.BOTAO_NOVA_SENHA, "gusmantis1")
        self.do_click(self.BOTAO_CONFIRMAR_SENHA)
        self.do_send_keys(self.BOTAO_CONFIRMAR_SENHA, "gusmantis1")
        self.do_click(self.BOTAO_ATUALIZAR_USUARIO)
        self.do_click(self.BOTAO_PROSSEGUIR_CADASTRO)

    def verifica_pagina_erro_senha(self):
        texto = self.get_element_text(self.MENSAGEM_ERRO_SENHA)
        return texto
