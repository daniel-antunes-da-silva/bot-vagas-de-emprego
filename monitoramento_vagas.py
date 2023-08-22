# Bot para pesquisar vagas de emprego no site indeed
import threading
from funcoes import iniciar_driver
from selenium.webdriver.common.by import By
import os
from time import sleep


def fechar_popup():
    contador = 0
    while True:
        try:
            sleep(0.5)
            botao_fechar_popup = driver.find_element(By.XPATH, '//button[@aria-label="fechar"]')
        except:
            pass
        else:
            botao_fechar_popup.click()
            sleep(0.2)
            break


cargo = str(input('Qual cargo quer procurar? '))
local = str(input('Para qual local? País, cidade, estado... '))
print('Encontrando vagas...')

driver = iniciar_driver()

# Navegar até o site
driver.get('https://br.indeed.com/')

try:
    sleep(1.5)
    driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
    sleep(1.5)
except:
    print('Talvez não exista a opção de aceitar cookies ou não foi possível encontrar. '
          'Isso não interromperá o funcionamento da automação.')


# Buscando cargo
# Encontrar o campo de cargo e digitar
campo_cargo = driver.find_element(By.XPATH, '//input[@id="text-input-what"]')
sleep(1)
campo_cargo.click()
sleep(1)
campo_cargo.send_keys(cargo)
sleep(1)
# Encontrar o campo de local e digitar
campo_local = driver.find_element(By.XPATH, '//input[@id="text-input-where"]')
sleep(1)
campo_local.click()
sleep(1)
campo_local.send_keys(local)
sleep(1)
# Encontrar o botão pesquisar (Achar vagas)
botao_pesquisar = driver.find_element(By.XPATH, '//button[@class="yosegi-InlineWhatWhere-primaryButton"]')
sleep(1)
botao_pesquisar.click()
sleep(3)

# Verificando se o popup vai aparecer na tela através de THREAD
thread_fechar_popup = threading.Thread(target=fechar_popup, daemon=True)
thread_fechar_popup.start()

# Começando o processo de extrair as infos
while True:
    sleep(1.5)
    # Descendo a página até o final.
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    sleep(1.5)
    # Encontrar os titulos
    titulos = driver.find_elements(By.XPATH, '//a//span[@title]')
    sleep(1)
    # Encontrar os links
    links = driver.find_elements(By.XPATH, '//a[@class="jcs-JobTitle css-jspxzf eu4oa1w0"]')
    sleep(1)
    # Guardar infos em arquivo txt (ou poderia ser .csv)
    for titulo, link in zip(titulos, links):
        with open('vagas.txt', 'a', encoding='UTF-8', newline='') as arquivo:
            link_extraido = link.get_attribute('href')
            arquivo.write(f'{titulo.text}{os.linesep}{link_extraido}{os.linesep}{os.linesep}')
    sleep(2)
    try:
        botao_avancar = driver.find_element(By.XPATH, '//a[@data-testid="pagination-page-next"]')
        if botao_avancar:
            botao_avancar.click()
            sleep(3)
            botao_avancar = None
        else:
            break
    except:
        print('Busca finalizada!')
        break

driver.close()
