import ExcelUtils

class DadosTest:
    #Web Drivers pastas
    CHROMEDRIVER_PATH = "/tools/selenium/chromedriver"
    GECKODRIVER_PATH = "/tools/selenium/geckodriver"

    #Data Driven Excel pasta
    PATH = r"C:\Users\Lorenzo\Documents\Aulas Faculdade\ProjetoUC\Feature05_criar_perfil_so\PerfilSO.xlsx"

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

    LISTA_LOGIN = alimentar_list(PATH ,"Login")
    LISTA_NOVO_PERFIL = alimentar_list(PATH, "NovoPerfilSO")
    LISTA_NOVO_PERFIL_INVALIDO = alimentar_list(PATH, "NovoPerfilSO_Invalido")
    LISTA_EDITAR_PERFIL = alimentar_list(PATH, "EditarPerfilSO")
