import pytest
from selenium import webdriver
from Config.config import DadosTest

#Iniciar webdriver
@pytest.fixture(params=["chrome"], scope='class')
def iniciar_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=DadosTest.CHROMEDRIVER_PATH)
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=DadosTest.GECKODRIVER_PATH)
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    yield web_driver
    web_driver.close()