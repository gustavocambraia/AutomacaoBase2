import webbrowser

from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Config.config import TestData

"""
Essa classe é o 'pai' de todas as páginas
Ela contém todos os métodos genéricos e funções para todas as páginas
"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def do_enter(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).send_keys(Keys.ENTER)

    def clear_text(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def get_text(self, by_locator):
        texto = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text
        return texto

    def get_value(self, by_locator):
        attribute = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).\
            get_attribute("value")
        return attribute
