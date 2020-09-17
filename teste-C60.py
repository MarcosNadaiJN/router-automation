from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# Definições Iniciais
senha = 'insert97'

dns_primario = '177.55.32.237'
dns_secundario = '8.8.8.8'

ntp_primario = 'a.btp.br'
ntp_secundario = 'b.ntp.br'

#Inicialização do Browser

browser = webdriver.Chrome(executable_path="F:\Drivers\chromedriver.exe")
browser.get("https://www.google.com.br")
browser.maximize_window()
sleep(1)
browser.get("http://192.168.0.1")
sleep(2)

'''
def find_by_href(browser, link):
    """
    Encontrar o elemento 'a' com o link 'link'

    Argumentos:
        - browser = instancia do browser [Chrome]
        - link = link que sera procurado em todos as tags a
    """
    elementos = browser.find_elements_by_tag_name('a')

    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento
'''

entradas = browser.find_elements_by_tag_name('input')       #Localiza todos os inputs da pagina, e armazena na lista 'entradas'.
campo_senha = entradas[20]      #O Campo da senha, corresponde ao item 20 da lista
campo_senha.send_keys(senha)       #Digita a senha
browser.find_element_by_id('login-btn').click()     #Clica no Botão de login
print('!--Login Efetuado com Sucesso--!')
sleep(5)

btn_avancado = browser.find_element_by_link_text('Avançado')        #Localiza Aba "Avançado"
btn_avancado.click()        #Acessa aba Avançado
print(btn_avancado.text)
sleep(3)

btn_rede = browser.find_element_by_link_text('Rede')        #Localiza Botão "Rede"
btn_rede.click()        #Clica no Botão "Rede"
print(btn_rede.text)
sleep(1)

servidor_dhcp = browser.find_element_by_link_text('Servidor DHCP')      #Localiza Botão "Servidor DHCP"
servidor_dhcp.click()       #Clica no Botão "Servidor DHCP"
print(servidor_dhcp.text)
sleep(2)

dns1 = browser.find_element_by_xpath('//*[@id="dns1"]')     #Localiza Campo DNS Primario
dns1.send_keys(Keys.CONTROL + "a")      #Seleciona o Conteudo do Campo
dns1.send_keys(Keys.DELETE)     #Apaga o Conteudo Existente
dns1.send_keys('177.55.32.237')     #Inseri Novo DNS Primario
print(f'DNS Primario Atualizado para: {dns_primario}')

dns2 = browser.find_element_by_xpath('//*[@id="dns2"]')     #Localiza Campo DNS Secundario
dns2.send_keys(Keys.CONTROL + "a")      #Seleciona o Conteudo do Campo
dns2.send_keys(Keys.DELETE)     #Apaga o Conteudo Existente
dns2.send_keys('1.1.1.1')       #Inseri Novo DNS Secundario
print(f'DNS Secundario Atualizado para: {dns_secundario}')

salvar_dns = browser.find_element_by_xpath('//*[@id="lan-ipv4-setting"]/div[8]/div/div/div/div[1]/button')      #Localiza Botão de Salvar DNS
#salvar_dns.click()     #Clica no Botão de Salvar o DNS
sleep(0.3)
print('DNS Atualizado com Sucesso')
sleep(5)

wireless = browser.find_element_by_link_text('Wireless')
wireless.click()
print(wireless.text)
sleep(2)

sis_tools = browser.find_element_by_link_text('Ferramentas de Sistema')     #Localiza o "Ferramentas do Sistema"
sis_tools.click()     #Clica no Ferramentas do Sistema
print(sis_tools.text)
sleep(3)

ntp = browser.find_element_by_xpath('//*[@id="menu-advanced-system-tools-li"]/div/ul/li[1]/a/span[2]')      #Localiza o "Ajuste de Horario"
ntp.click()     #Clica no "Ajuste de Horario"
print(ntp.text)
sleep(2)

ntp_server_1 = browser.find_element_by_id('time_set_ntp1')      #Localiza Campo NTP1
ntp_server_1.send_keys(Keys.CONTROL + "a")      #Seleciona o Conteudo do Campo
ntp_server_1.send_keys(Keys.DELETE)     #Apaga o Conteudo Existente
ntp_server_1.send_keys(ntp_primario)      #Digita o Servidor NTP1 Atualizado
print(f'NTP Primario Atualizado para: {ntp_primario}')

ntp_server_1 = browser.find_element_by_id('time_set_ntp2')      #Localiza Campo NTP2
ntp_server_1.send_keys(Keys.CONTROL + "a")      #Seleciona o Conteudo do Campo
ntp_server_1.send_keys(Keys.DELETE)     #Apaga o Conteudo Existente
ntp_server_1.send_keys(ntp_secundario)      #Digita o Servidor NTP2 Atualizado
print(f'NTP Secundario Atualizado para: {ntp_secundario}')

save_ntp = browser.find_element_by_xpath('//*[@id="time_setting"]/div[6]/div/div/div/div[1]/button/span[2]')        #Salva as Alterações do NTP
sleep(3)
print('NTP Atualizado com Sucesso')
sleep(0.5)
print('Configurações Finalizadas')

logoff = browser.find_element_by_id('top-control-logout').click()
confirmacao_logoff = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div[4]/div/div/div[2]/div/div[2]/button')
confirmacao_logoff.click()

print('Logoff Realizado com Sucesso')
