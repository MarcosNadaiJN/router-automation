#from c60_script import *
#from selenium import webdriver
#from selenium.common.exceptions import TimeoutException
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from definicoes_iniciais import *


def c60_login(browser):
    entradas = browser.find_elements_by_tag_name('input')  # Localiza todos os inputs da pagina, e armazena na lista 'entradas'.
    campo_senha = entradas[20]  # O Campo da senha, corresponde ao item 20 da lista
    campo_senha.send_keys(senha)  # Digita a senha
    browser.find_element_by_id('login-btn').click()  # Clica no Botão de login
    print('!--Login Efetuado com Sucesso--!')

def c60_botao_avancado(browser):
    btn_avancado = WebDriverWait(browser, 8).until(EC.presence_of_element_located((By.ID, 'internet_status')))  #Espera Status da Internet Carregar
    btn_avancado = browser.find_element_by_link_text('Avançado').click()  # Acessa aba Avançado
    print('Avançado')

def c60_botao_rede(browser):
    sleep(3)
    btn_rede = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'internet_ipv4_mac_address')))
    btn_rede = browser.find_element_by_link_text('Rede').click()  # Clica no Botão "Rede"
    print('Rede')

def c60_botao_DHCP(browser):
    sleep(0.8)
    servidor_dhcp = WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Servidor DHCP')))
    servidor_dhcp = browser.find_element_by_link_text('Servidor DHCP').click()  # Clica no Botão "Servidor DHCP"
    print('Servidor DHCP')

def c60_DHCP(browser):
    from funcoes import seleciona_deleta
    sleep(0.5)
    dns1 = browser.find_element_by_xpath('//*[@id="dns1"]')     #Localiza Campo DNS Primario
    seleciona_deleta(dns1)      #Limpa o Campo
    dns1.send_keys(dns_primario)        #Inseri Novo DNS Primario
    print(f'DNS Primario Atualizado para: {dns_primario}')

    dns2 = browser.find_element_by_xpath('//*[@id="dns2"]')     #Localiza Campo DNS Secundario
    seleciona_deleta(dns2)      #Limpa Campo
    dns2.send_keys(Keys.DELETE)     #Inseri Novo DNS Secundario
    print(f'DNS Secundario Atualizado para: {dns_secundario}')

    salvar_dns = browser.find_element_by_xpath('//*[@id="lan-ipv4-setting"]/div[8]/div/div/div/div[1]/button')  # Localiza Botão de Salvar DNS
    # salvar_dns.click()     #Clica no Botão de Salvar o DNS
    sleep(0.3)
    print('DNS Atualizado com Sucesso')

def c60_wireless(browser):
    wireless = browser.find_element_by_link_text('Wireless')  # Localiza Botão Wireless
    wireless.click()  # Clica no Botão Wireless
    print('Wireless')

def c60_botao_sis_tools(browser):
    sis_tools = browser.find_element_by_link_text('Ferramentas de Sistema').click()  # Localiza o "Ferramentas do Sistema" e Clica
    print('Ferramentas do Sistema')

def c60_botao_ntp(browser):
    ntp = WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-advanced-system-tools-li"]/div/ul/li[1]/a/span[2]')))
    ntp = browser.find_element_by_xpath('//*[@id="menu-advanced-system-tools-li"]/div/ul/li[1]/a/span[2]').click  # Localiza o "Ajuste de Horario" e Clica
    print('Ajuste de Horario')

def c60_ntp(browser):
    from funcoes import seleciona_deleta
    ntp_server_1 = browser.find_element_by_id('time_set_ntp1')      #Localiza Campo NTP1
    seleciona_deleta(ntp_server_1)      #Limpa Campo NTP 1
    ntp_server_1.send_keys(ntp_primario)      #Digita o Servidor NTP1 Atualizado
    print(f'NTP Primario Atualizado para: {ntp_primario}')

    ntp_server_2 = browser.find_element_by_id('time_set_ntp2')      #Localiza Campo NTP2
    seleciona_deleta(ntp_server_2)
    ntp_server_2.send_keys(ntp_secundario)      #Digita o Servidor NTP2 Atualizado
    print(f'NTP Secundario Atualizado para: {ntp_secundario}')

    save_ntp = browser.find_element_by_xpath('//*[@id="time_setting"]/div[6]/div/div/div/div[1]/button/span[2]')        #Localiza o Botão de Salvar NTP
    save_ntp.click()        #Clica no Botão de Salvar
    sleep(3)
    print('NTP Atualizado com Sucesso')
    print('Configurações Finalizadas')

def c60_logoff(browser):
    logoff = browser.find_element_by_id('top-control-logout').click()  # Localiza Botão de Logoff
    confirmacao_logoff = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div[4]/div/div/div[2]/div/div[2]/button')  # Confirma Logoff
    confirmacao_logoff.click()  # Clica na Confirmação
    print('Logoff Realizado com Sucesso')
