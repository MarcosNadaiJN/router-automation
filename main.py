#1 - Alimentar IP's de Acesso Utilizando CSV
#2 - Identificar o Modelo do Roteador Utilizando o Tittle
#3 - Chamar o Arquivo Correspondente ao Modelo
#4 - Marcar IP' como Visitado, e escrever se foi possivel acessar ou não
#5 - Pegar Proximo Ip na Planilha e Reiniciar o Processo

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from funcoes import trata_titulo
import os

# Definições Iniciais
senha = 'insert97'

dns_primario = '177.55.32.237'
dns_secundario = '8.8.8.8'

ntp_primario = 'a.btp.br'
ntp_secundario = 'b.ntp.br'

#Inicialização do Browser

browser = webdriver.Chrome(executable_path="F:\Drivers\chromedriver.exe")
browser.maximize_window()

try:
    browser.get("http://192.168.0.1")
    sleep(2)

    tlt = browser.title
    tlt = trata_titulo(tlt)
    print(tlt)

    if tlt == 'archerc60':
        os.system('python Auto-TPLink-C60.py')
    else:
        print('Modelo Não Compativel')

except Exception:
    print('Erro')