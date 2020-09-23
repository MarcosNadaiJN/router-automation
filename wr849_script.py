from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def wr849_completo(browser, senha, dns_primario, dns_secundario, ntp_primario, ntp_secundario):
    #browser = webdriver.Chrome(executable_path="F:\Drivers\chromedriver.exe")   #Remover depois
    #browser.maximize_window()   #Remover depois

    sis_tools = browser.find_element_by_xpath('//*[@id="menu_tools"]')
    sis_tools.click()

    horario = browser.find_element_by_id('menu_time')
    sis_tools.click()

    ntp_server_1 = browser.find_element_by_id('ntpA')  # Localiza Campo NTP1
    ntp_server_1.send_keys(Keys.CONTROL + "a")  # Seleciona o Conteudo do Campo
    ntp_server_1.send_keys(Keys.DELETE)  # Apaga o Conteudo Existente
    ntp_server_1.send_keys(ntp_primario)  # Digita o Servidor NTP1 Atualizado
    print(f'NTP Primario Atualizado para: {ntp_primario}')

    ntp_server_2 = browser.find_element_by_id('ntpB')  # Localiza Campo NTP1
    ntp_server_2.send_keys(Keys.CONTROL + "a")  # Seleciona o Conteudo do Campo
    ntp_server_2.send_keys(Keys.DELETE)  # Apaga o Conteudo Existente
    ntp_server_2.send_keys(ntp_primario)  # Digita o Servidor NTP1 Atualizado
    print(f'NTP Primario Atualizado para: {ntp_secundario}')

    salvar_ntp = browser.find_element_by_xpath('//*[@id="saveBtn"]').click()
