import pytest
from selenium import webdriver
from Config.config import DadosTest

#Iniciar webdriver
@pytest.fixture(params=["chrome", "firefox"], scope='class')
def iniciar_driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        prefs = {
            "profile.default_content_settings.popups": 0,
            "download.default_directory": r"C:\Users\Lorenzo\Documents\Aulas Faculdade\ProjetoUC\Feature03_exportar_tarefas\Files\\", ### MUDAR
            "directory_upgrade": True,
            'safebrowsing.enabled': 'false'
        }
        options.add_experimental_option("prefs", prefs)
        web_driver = webdriver.Chrome(executable_path=DadosTest.CHROMEDRIVER_PATH, chrome_options= options)
    if request.param == "firefox":
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.helperApps.alwaysAsk.force", False)
        profile.set_preference("browser.download.manager.showAlertOnComplete", False)
        profile.set_preference("browser.download.dir", r"C:\Users\Lorenzo\Documents\Aulas Faculdade\ProjetoUC\Feature03_exportar_tarefas\Files\\") ### MUDAR
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", 'application/zip,application/octet-stream,application/x-zip-compressed,multipart/x-zip,application/x-rar-compressed, application/octet-stream,application/msword,application/vnd.ms-word.document.macroEnabled.12,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/rtf,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.ms-excel,application/vnd.ms-word.document.macroEnabled.12,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/xls,application/msword,text/csv,application/vnd.ms-excel.sheet.binary.macroEnabled.12,text/plain,text/csv/xls/xlsb,application/csv,application/download,application/vnd.openxmlformats-officedocument.presentationml.presentation,application/octet-stream')
        profile.set_preference("browser.helperApps.neverAsk.openFile", 'application/zip')
        web_driver = webdriver.Firefox(executable_path=DadosTest.GECKODRIVER_PATH, firefox_profile=profile)
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    yield web_driver
    web_driver.close()