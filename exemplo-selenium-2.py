# Exemplo 2: Teste de busca em um site e verificação de resultados

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

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