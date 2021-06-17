import ExcelUtils

class DadosTest:
    #Web Drivers pastas
    CHROMEDRIVER_PATH = r"C:\Program Files\JetBrains\PyCharm Community Edition 2020.1.2\bin\chromedriver.exe"
    GECKODRIVER_PATH = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\geckodriver"

    #Data Driven Excel pasta
    PATH = r"C:\Users\gusta\Desktop\AutomacaoBase2-master\AutomacaoBase2-master\Feature04_filtrar_tarefas\FiltrarTarefas.xlsx"

    #URL da pagina de login
    URL = "https://mantis.saojudas.base2.com.br/login_page.php"

    #Listas Data Driven
    def alimentar_list(path, pagina):
        lista = []
        rows = ExcelUtils.get_quantidade_linha(path, pagina)
        columns = ExcelUtils.get_quantidade_coluna(path, pagina)

        for r in range(2, rows+1):
            listatemp = []
            if columns > 1:
                for c in range(1, columns+1):
                    dado = ExcelUtils.ler_dados(path, pagina, r, c)
                    listatemp.append(dado)

                tupla = tuple(listatemp)
                lista.append(tupla)
            else:
                for c in range(1, columns+1):
                    dado = ExcelUtils.ler_dados(path, pagina, r, c)
                    lista.append(dado)
        return lista

    LISTA_LOGIN = alimentar_list(PATH, "Login")
    LISTA_ATRIBUIDO = alimentar_list(PATH, "FiltrarAtribuido")
    LISTA_GRAVIDADE = alimentar_list(PATH, "FiltrarGravidade")
    LISTA_ESTADO = alimentar_list(PATH, "FiltrarEstado")
    LISTA_DATAS = alimentar_list(PATH, "FiltrarDatas")
    LISTA_SAVE_FILTER = alimentar_list(PATH, "SalvarFiltro")


