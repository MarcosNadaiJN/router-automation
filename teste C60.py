from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

#Inicialização do Browser

browser = webdriver.Chrome(executable_path="F:\Drivers\chromedriver.exe")
browser.get("http://192.168.0.1")
sleep(2)


entradas = browser.find_elements_by_tag_name('input')#Localiza todos os inputs da pagina, e armazena na lista 'entradas'.

campo_senha = entradas[20]#O Campo da senha, corresponde ao item 20 da lista

campo_senha.send_keys('insert97')#Digita a senha

browser.find_element_by_id('login-btn').click()#Clica no Botão de login
