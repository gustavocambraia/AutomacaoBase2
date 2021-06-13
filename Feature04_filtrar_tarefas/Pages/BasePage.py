from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Classe parente de todas as Pages 
# contem utilidades e metodos genéricos

class BasePage():

    def __init__(self, driver):
        self.driver = driver

    #Metodo genérico de click
    def clicar(self, locator):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        ).click()

    #Metodo genérico envio de texto para o elemento
    def enviar_teclas(self, locator, texto):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(texto)
    
    #Metodo genérico retornando texto do elemento
    def get_texto_elemento(self, locator):
        elemento = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )
        return elemento.text

    #Metodo genérico retornando texto do elemento
    def get_elemento(self, locator):
        elemento = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )
        return elemento

    def get_elementos(self, locator):
        elementos = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_all_elements_located(locator)
        )
        return elementos

    #Metodo retorna visibilidade do elemento
    def elemento_visivel(self, locator):
        elemento = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )
        return bool(elemento)

    #Metodo que retorna se o elemento esta exibido
    def elemento_displayed(self, locator):
        elemento = self.driver.find_element(*locator)
        return elemento.is_displayed()

    #Metodo retorna atributo style do elemento
    def get_style_elemento(self, locator):
        elemento = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )
        return elemento.get_attribute('style')

    #Verificar URL
    def verificar_url(self, urlpart):
        resp = WebDriverWait(self.driver, 5).until(EC.url_contains(urlpart))
        return bool(resp)

    JS_DROP_FILE = """
        var target = arguments[0],
            offsetX = arguments[1],
            offsetY = arguments[2],
            document = target.ownerDocument || document,
            window = document.defaultView || window;

        var input = document.createElement('INPUT');
        input.type = 'file';
        input.onchange = function () {
        var rect = target.getBoundingClientRect(),
            x = rect.left + (offsetX || (rect.width >> 1)),
            y = rect.top + (offsetY || (rect.height >> 1)),
            dataTransfer = { files: this.files };

        ['dragenter', 'dragover', 'drop'].forEach(function (name) {
            var evt = document.createEvent('MouseEvent');
            evt.initMouseEvent(name, !0, !0, window, 0, 0, 0, x, y, !1, !1, !1, !1, 0, null);
            evt.dataTransfer = dataTransfer;
            target.dispatchEvent(evt);
        });

        setTimeout(function () { document.body.removeChild(input); }, 25);
        };
        document.body.appendChild(input);
        return input;
    """

    # Metodo genérico de envio de arquivo
    def enviar_arquivo(self, drop_target, path):
        driver = drop_target.parent
        file_input = driver.execute_script(self.JS_DROP_FILE, drop_target, 0, 0)
        file_input.send_keys(path)

    # Metodo genérico de retorno do elemento alert
    def get_alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        return alert
    
         