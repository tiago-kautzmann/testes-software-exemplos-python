# Exemplo 3 - Teste de login em um site

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

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