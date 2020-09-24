from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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

    #Login Inicial no Roteador

    entradas = browser.find_elements_by_tag_name('input')       #Localiza todos os inputs da pagina, e armazena na lista 'entradas'.
    campo_senha = entradas[20]      #O Campo da senha, corresponde ao item 20 da lista
    campo_senha.send_keys(senha)       #Digita a senha
    browser.find_element_by_id('login-btn').click()     #Clica no Botão de login
    print('!--Login Efetuado com Sucesso--!')

    btn_avancado = WebDriverWait(browser, 8).until(EC.presence_of_element_located((By.ID, 'internet_status')))   #Espera Status da Internet Carregar
    btn_avancado = browser.find_element_by_link_text('Avançado').click()        #Acessa aba Avançado
    print('Avançado')
    sleep(3)

    #btn_rede = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'conn_status_internet')))
    btn_rede = browser.find_element_by_link_text('Rede').click()  #Clica no Botão "Rede"
    print('Rede')

    servidor_dhcp = WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Servidor DHCP')))
    servidor_dhcp = browser.find_element_by_link_text('Servidor DHCP').click()     #Clica no Botão "Servidor DHCP"
    print('Servidor DHCP')

    sleep(0.5)

    dns1 = browser.find_element_by_xpath('//*[@id="dns1"]')     #Localiza Campo DNS Primario
    dns1.send_keys(Keys.CONTROL + "a")      #Seleciona o Conteudo do Campo
    dns1.send_keys(Keys.DELETE)     #Apaga o Conteudo Existente
    dns1.send_keys(dns_primario)     #Inseri Novo DNS Primario
    print(f'DNS Primario Atualizado para: {dns_primario}')

    dns2 = browser.find_element_by_xpath('//*[@id="dns2"]')     #Localiza Campo DNS Secundario
    dns2.send_keys(Keys.CONTROL + "a")      #Seleciona o Conteudo do Campo
    dns2.send_keys(Keys.DELETE)     #Apaga o Conteudo Existente
    dns2.send_keys(dns_secundario)       #Inseri Novo DNS Secundario
    print(f'DNS Secundario Atualizado para: {dns_secundario}')

    salvar_dns = browser.find_element_by_xpath('//*[@id="lan-ipv4-setting"]/div[8]/div/div/div/div[1]/button')      #Localiza Botão de Salvar DNS
    #salvar_dns.click()     #Clica no Botão de Salvar o DNS
    sleep(0.3)
    print('DNS Atualizado com Sucesso')

    '''
    #------------------
    
    wireless = browser.find_element_by_link_text('Wireless')        #Localiza Botão Wireless
    wireless.click()        #Clica no Botão Wireless
    print(wireless.text)
    sleep(2)


    txbf = browser.find_element_by_link_text('TxBF,MU-MIMO')
    txbf.click()
    print(txbf.text)
    sleep(0.5)

    checkbox_all = browser.find_elements_by_xpath('//*[@id="txbf_set"]/div[1]/div[2]/div[1]/ul/li/div/label')
    checked = checkbox_all.__getattribute__('class')
    print(checked)

    sleep(30)

    salvar_txbf = browser.find_element_by_xpath('//*[@id="txbf_set"]/div[2]/div/div/div/div[1]/button/span[2]')
    salvar_txbf.click()
    print('')

    #------------------
    '''

    wireless = browser.find_element_by_link_text('Wireless')  # Localiza Botão Wireless
    wireless.click()  # Clica no Botão Wireless
    print('Wireless')
    sleep(2)

    sis_tools = browser.find_element_by_link_text('Ferramentas de Sistema').click()       #Localiza o "Ferramentas do Sistema" e Clica
    print('Ferramentas do Sistema')
    sleep(0.5)

    ntp = browser.find_element_by_xpath('//*[@id="menu-advanced-system-tools-li"]/div/ul/li[1]/a/span[2]').click()      #Localiza o "Ajuste de Horario" e Clica
    print('Ajuste de Horario')
    sleep(1)

    ntp_server_1 = browser.find_element_by_id('time_set_ntp1')      #Localiza Campo NTP1
    ntp_server_1.send_keys(Keys.CONTROL + "a")      #Seleciona o Conteudo do Campo
    ntp_server_1.send_keys(Keys.DELETE)     #Apaga o Conteudo Existente
    ntp_server_1.send_keys(ntp_primario)      #Digita o Servidor NTP1 Atualizado
    print(f'NTP Primario Atualizado para: {ntp_primario}')

    ntp_server_2 = browser.find_element_by_id('time_set_ntp2')      #Localiza Campo NTP2
    ntp_server_2.send_keys(Keys.CONTROL + "a")      #Seleciona o Conteudo do Campo
    ntp_server_2.send_keys(Keys.DELETE)     #Apaga o Conteudo Existente
    ntp_server_2.send_keys(ntp_secundario)      #Digita o Servidor NTP2 Atualizado
    print(f'NTP Secundario Atualizado para: {ntp_secundario}')

    save_ntp = browser.find_element_by_xpath('//*[@id="time_setting"]/div[6]/div/div/div/div[1]/button/span[2]')        #Localiza o Botão de Salvar NTP
    save_ntp.click()        #Clica no Botão de Salvar
    sleep(3)
    print('NTP Atualizado com Sucesso')
    sleep(0.5)
    print('Configurações Finalizadas')

    logoff = browser.find_element_by_id('top-control-logout').click()       #Localiza Botão de Logoff
    confirmacao_logoff = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div[4]/div/div/div[2]/div/div[2]/button')      #Confirma Logoff
    confirmacao_logoff.click()      #Clica na Confirmação
    print('Logoff Realizado com Sucesso')


except Exception:
    print('Não Foi Possivel Realizar as Alterações')
