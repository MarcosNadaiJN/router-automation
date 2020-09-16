from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

#Inicialização do Browser

browser = webdriver.Chrome(executable_path="F:\Drivers\chromedriver.exe")
browser.get("http://192.168.0.1")
sleep(2)

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



entradas = browser.find_elements_by_tag_name('input')#Localiza todos os inputs da pagina, e armazena na lista 'entradas'.

campo_senha = entradas[20]#O Campo da senha, corresponde ao item 20 da lista

campo_senha.send_keys('insert97')#Digita a senha

browser.find_element_by_id('login-btn').click()#Clica no Botão de login

sleep(5)

btn_avancado = find_by_href(browser, 'pages/frame/advanced.html')
btn_avancado.click()
print(btn_avancado.text)
sleep(3)


btn_rede = find_by_href(browser, 'pages/userrpm/internet.html')
btn_rede.click()
print(btn_rede.text)
sleep(1)

servidor_dhcp = find_by_href(browser, 'pages/userrpm/dhcpServer.html')
servidor_dhcp.click()
print(servidor_dhcp.text)