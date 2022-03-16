from selenium import webdriver
from selenium.webdriver.common.by import By

veiculos = ["Fusca", "Gol", "Palio", "Celta", "Ford KA"]  # LISTA COM CADA CARRO
driver = webdriver.Chrome()  # ESPECIFICAÇÃO DE ONDE ESTÁ O CHROMEDRIVER (no caso está na mesma pasta que o código)

for veiculo in veiculos:    # RODANDO CADA VEICULO NA LISTA VEICULOS...
    # ABRINDO O SITE QUE GERA QRCODE E CONCATENANDO URL+VEICULO
    driver.get('https://chart.googleapis.com/chart?chs=150x150&cht=qr&chl=' + veiculo)
    driver.maximize_window()  # MAXIMIZA A PÁGINA ABERTA

    qrcode = driver.find_element(By.XPATH, '//*[@src]')  # ENCONTRA O ELEMENTO ATRAVÉS DO XPATH
    qrcode.screenshot(f'{veiculo}.png')  # TIRA UM PRINT APENAS DO ELEMENTO ESPECIFICADO

driver.close()  # Fecha a conexão com o driver
