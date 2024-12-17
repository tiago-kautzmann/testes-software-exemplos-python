from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_site_search():
    print("Iniciando o teste...")

    # Inicializa o WebDriver para o Chrome
    driver = webdriver.Chrome()

    try:
        # Abre o site em que será realizada a busca
        driver.get("https://ifpr.edu.br/uniao-da-vitoria/")

        # Aguarda 5 segundos para garantir que a página carregue
        time.sleep(5)

        # Localiza o campo de pesquisa e envia uma consulta
        campo_pesquisa = driver.find_element(By.ID, "site-search")
        campo_pesquisa.send_keys("Entec")

        # Aguarda 2 segundos
        time.sleep(2)

        # Pressiona a tecla Enter para realizar a busca
        campo_pesquisa.send_keys(Keys.RETURN)

        # Aguarda os resultados carregarem
        time.sleep(10)

        # Verifica se um link específico está presente nos resultados
        link_esperado = "https://ifpr.edu.br/uniao-da-vitoria/inscricoes-abertas-para-as-oficinas-e-palestras-do-7o-entec/"
        resultados = driver.find_elements(By.CSS_SELECTOR, "a")

        # Procura pelo link nos resultados
        link_encontrado = any(link_esperado in resultado.get_attribute("href") for resultado in resultados if resultado.get_attribute("href"))

        # Exibe o resultado da verificação
        if link_encontrado:
            print(f"O link '{link_esperado}' foi encontrado nos resultados.")
        else:
            print(f"O link '{link_esperado}' não foi encontrado nos resultados.")

    except Exception as e:
        print(f"Erro durante a execução: {e}")

    finally:
        # Fecha o navegador
        driver.quit()
        print("Teste finalizado.")

def test_site_login():

    print("Iniciando o teste...")

    # Inicializa o WebDriver para o Chrome
    driver = webdriver.Chrome()

    try:
        # Abre o site
        driver.get("https://suap.ifpr.edu.br/")  # Site de exemplo com login de teste

        # Aguarda 5 segundos para a página carregar
        time.sleep(5)

        # Localiza o campo de nome de usuário e insere o valor
        campo_usuario = driver.find_element(By.ID, "id_username")
        campo_usuario.send_keys("COLOQUE AQUI O USUÁRIO")

        # Localiza o campo de senha e insere o valor
        campo_senha = driver.find_element(By.ID, "id_password")
        campo_senha.send_keys("COLOQUE AQUI A SENHA")

        # Pressiona Enter ou clica no botão de login
        campo_senha.send_keys(Keys.RETURN)

        # Aguarda 5 segundos para o login ser processado
        time.sleep(5)

        # Verifica se o login foi bem-sucedido buscando um elemento da página principal
        try:
            driver.find_element(By.CLASS_NAME, "user-profile")
            print("Login bem-sucedido!")
        except:
            print("Falha no login. Verifique as credenciais.")

    except Exception as e:
        print("Ocorreu um erro:", e)

    finally:
        # Fecha o navegador
        driver.quit()
        print("Teste finalizado.")