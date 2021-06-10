from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
import os.path

# Classe parente de todas as Pages 
# contem utilidades e metodos genéricos

class BasePage():
    def __init__(self, driver):
        self.driver = driver

    #Metodo genérico de click
    def clicar(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        ).click()

    #Metodo genérico envio de texto para o elemento
    def enviar_teclas(self, locator, texto):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(texto)
    
    #Metodo genérico retornando texto do elemento
    def get_texto_elemento(self, locator):
        elemento = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        return elemento.text

    #Metodo retorna visibilidade do elemento
    def elemento_visivel(self, locator):
        elemento = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        return bool(elemento)