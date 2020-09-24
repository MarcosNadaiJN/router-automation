#Tratamento de Titulo

def trata_titulo (titulo_original):
    titulo = titulo_original
    titulo = titulo.lower()
    titulo = titulo.strip()
    titulo = titulo.replace(' ', '')
    titulo = titulo.replace('-', '')
    return titulo



#Tratamento do IP de Acesso

def trata_ip (ip_acesso):
    ip_acesso = str(ip_acesso)
    ip_acesso = ip_acesso.replace("['", '')
    ip_acesso = ip_acesso.replace("']", '')
    ip_acesso = 'http://'+ip_acesso
    return ip_acesso



#Leitura CSV

def ler_csv (nome_arquivo):
    import csv

    with open(nome_arquivo) as csv_file:
        arquivo = csv.reader(csv_file)
        lista = list(arquivo)

    return lista



#Contagem da Lista de IP's

def cont_ip (lista):
    tamanho = len(lista)
    return tamanho



# CRTL A + CRTL DEL

def seleciona_deleta(campo):
    from selenium.webdriver.common.keys import Keys
    campo.send_keys(Keys.CONTROL + "a")
    campo.send_keys(Keys.DELETE)



# Browser

def abre_navegador():
    from selenium import webdriver
    return webdriver.Chrome(executable_path="F:\Drivers\chromedriver.exe")