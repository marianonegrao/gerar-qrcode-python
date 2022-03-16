from selenium import webdriver
import pyautogui as pag

veiculos = ["Gol G5", "Celta", "Brasilia", "Fusca", "Ford KA"]  # LISTA COM CADA CARRO
driver = webdriver.Chrome('C:/Users/mariano/Desktop/chromedriver.exe')  # ESPECIFICAÇÃO DE ONDE ESTÁ O CHROMEDRIVER

for veiculo in veiculos:    # RODANDO CADA VEICULO NA LISTA VEICULOS...
    driver.get('https://chart.googleapis.com/chart?chs=150x150&cht=qr&chl=' + veiculo)  # ABRINDO O SITE QUE GERA QRCODE E CONCATENANDO URL+VEICULO
    driver.maximize_window()  # MAXIMIZA A PÁGINA ABERTA

    pag.moveTo(x=677, y=409)  # MOVE O MOUSE PARA A POSIÇÃO ESPECIFICADA
    pag.sleep(3)  # "ADORMECE" 3 SEGUNDOS ATÉ A EXECUÇÃO DO PRÓXIMO MOVIMENTO
    pag.rightClick()  # SIMULA O CLICK COM O BOTÃO DIREITO DO MOUSE
    pag.moveTo(x=748, y=453)  # MOVE O MOUSE PARA A POSIÇÃO ESPECIFICADA
    pag.sleep(3)  # "ADORMECE" 3 SEGUNDOS ATÉ A EXECUÇÃO DO PRÓXIMO MOVIMENTO
    pag.leftClick()  # SIMULA O CLICK COM O BOTÃO ESQUERDO DO MOUSE
    pag.sleep(3)  # "ADORMECE" 3 SEGUNDOS ATÉ A EXECUÇÃO DO PRÓXIMO MOVIMENTO
    pag.hotkey('alt', 'space', 'x')  # SIMULA A AÇÃO DE PRESSIONAR AS TECLAS ESPECIFICADAS
    pag.sleep(3)  # "ADORMECE" 3 SEGUNDOS ATÉ A EXECUÇÃO DO PRÓXIMO MOVIMENTO
    pag.write(veiculo)  # ESCREVE O QUE ESTÁ NA LISTA VEICULO NA POSIÇÃO PERCORRIDA ATUALMENTE
    pag.sleep(3)  # "ADORMECE" 3 SEGUNDOS ATÉ A EXECUÇÃO DO PRÓXIMO MOVIMENTO
    pag.hotkey('ENTER')  # SIMULA A AÇÃO DE APERTAR A TECLA ENTER

driver.close()  # Fecha a conexão com o driver
