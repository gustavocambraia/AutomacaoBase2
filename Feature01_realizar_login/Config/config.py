import ExcelUtils

class DadosTest:
    #Web Drivers pastas
    CHROMEDRIVER_PATH = "/tools/selenium/chromedriver"
    GECKODRIVER_PATH = "/tools/selenium/geckodriver"

    #Data Driven Excel pasta
    PATH = "/Users/Lorenzo/Documents/Aulas Faculdade/ProjetoUC/Feature01_realizar_login/Login1.xlsx"

    #URL da pagina de login
    URL = "https://mantis.saojudas.base2.com.br/login_page.php"

    #Listas Data Driven
    def alimentar_list(path, pagina):
        lista = []
        rows = ExcelUtils.get_quantidade_linha(path, pagina)
        columns = ExcelUtils.get_quantidade_coluna(path, pagina)

        for r in range(2, rows+1):
            listatemp = []
            for c in range(1, columns+1):
                dado = ExcelUtils.ler_dados(path, pagina, r, c)
                listatemp.append(dado)

            tupla = tuple(listatemp)
            lista.append(tupla)
        return lista

    LISTA_VALIDOS = alimentar_list(PATH ,"LoginsValidos")
    LISTA_INVALIDOS = alimentar_list(PATH ,"LoginsInvalidos")

    MSG_ERRO_ESPERADO = "Sua conta pode estar desativada ou bloqueada ou o nome de usuário e a senha que você digitou não estão corretos."

