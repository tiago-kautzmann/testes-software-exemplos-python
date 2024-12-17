# Exemplo 1 - Teste de busca em um site

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializa o WebDriver para o Chrome
driver = webdriver.Chrome()

# Abre o site desejado em que será realizada a busca
driver.get("https://ifpr.edu.br/uniao-da-vitoria/")

# Aguarda 5 segundos para garantir que a página carregue
time.sleep(5)

# Localiza o campo de busca e envia uma consulta
campo_busca = driver.find_element(By.ID, "site-search")
campo_busca.send_keys("Entec")

# Aguarda 2 segundos
time.sleep(2)

# Pressiona a tecla Enter para realizar a busca
campo_busca.send_keys(Keys.RETURN)

# Aguarda 10 segundos para visualizar os resultados
time.sleep(10)

# Fecha o navegador
driver.quit()