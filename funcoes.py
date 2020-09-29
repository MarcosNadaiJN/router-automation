#Tratamento de Titulo
def trata_titulo (titulo_original):
    titulo = titulo_original
    titulo = titulo.lower()
    titulo = titulo.strip()
    titulo = titulo.replace(' ', '')
    titulo = titulo.replace('-', '')
    return titulo



#Tratamento do IP de Acesso
def trata_lista (item_lista):
    item_lista = str(item_lista)
    item_lista = item_lista.replace("['", '')
    item_lista = item_lista.replace("']", '')
    return item_lista



#Leitura CSV
def ler_csv (nome_arquivo):
    import csv
    with open(nome_arquivo) as csv_file:
        arquivo = csv.reader(csv_file)
        lista = list(arquivo)
        tamanho = len(lista)
    return lista, tamanho



# CRTL A + CRTL DEL
def seleciona_deleta(campo):
    from selenium.webdriver.common.keys import Keys
    from time import sleep
    campo.send_keys(Keys.CONTROL + "a")
    sleep(0.15)
    campo.send_keys(Keys.DELETE)
    sleep(0.15)



# Browser
def abre_navegador():
    from selenium import webdriver
    return webdriver.Chrome(executable_path="F:\Drivers\chromedriver.exe")


# Indentifica Modelo do Roteador e Roda o Script Correspondente
def identifica_modelo(titulo):
    from c60_script_funcoes import c60_completo_quebrado_em_funcoes
    if titulo == 'archerc60':
        c60_completo_quebrado_em_funcoes(titulo)
    elif titulo == 'tlwr940n':
        print('TL-WR949N')
        #função do 949
    else:
        print('Modelo não localizado na Biblioteca')



# Coleta a lista de senhas contida no arquivo CSV "senhas.csv"
def lista_senhas():
    import csv
    with open('senhas.csv') as csv_file:
        lista_senhas = csv.reader(csv_file)
        lista_senhas = list(lista_senhas)
        tamanho = len(lista_senhas)
        lista_senhas = trata_lista(lista_senhas)
        return lista_senhas, tamanho



def tentativas_login(titulo):
    from c60_funcoes import c60_confirma_login, c60_login
    lista, i = lista_senhas()
    login_bem_sucedido = c60_confirma_login()
    j = 0
    while j <= i or login_bem_sucedido == False:
        if titulo == 'archerc60':
            c60_login(lista[j])
        j += 1
