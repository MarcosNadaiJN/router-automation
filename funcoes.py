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
    item_lista = item_lista.replace("'", '')
    item_lista = item_lista.replace("'", '')
    return item_lista


#Leitura CSV
def ler_csv (nome_arquivo):
    import csv
    lista = []
    with open(nome_arquivo, newline='') as csv_file:
        for linha in csv.reader(csv_file):
            lista.append(linha[0])
        tamanho_lista = len(lista)
    return lista, tamanho_lista

#Escrita CSV_log
def escrita_csv_log (confirmacao_login, DHCP, NTP, j):
    import csv
    from definicoes_iniciais import lista_ip, tamanho_lista_ip
    with open('LOG_CSV.csv', 'w', newline='') as csv_file:
        campos = ['IP', 'LOGIN', 'DHCP', 'NTP']
        writer = csv.DictWriter(csv_file, fieldnames=campos)

        writer.writeheader()
        writer.writerow({'IP': lista_ip[j], 'LOGIN': confirmacao_login, 'DHCP': DHCP, 'NTP': NTP})


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
    from script_por_roteador import c60_completo_dividido_em_funcoes
    if titulo == 'archerc60':
        confirmacao_login, DHCP, NTP = c60_completo_dividido_em_funcoes(titulo)
    elif titulo == 'tlwr940n':
        print('TL-WR949N')
        #função do 949
    else:
        print('Modelo não localizado na Biblioteca')
    return confirmacao_login, DHCP, NTP


def tentativas_login(titulo):
    from c60_funcoes import c60_confirma_login, c60_login
    from time import sleep
    lista, i = ler_csv('senhas.csv')
    login_bem_sucedido = False
    j = 0
    while login_bem_sucedido == False:
        if titulo == 'archerc60':
            c60_login(trata_lista(lista[j]), j)
        else:
            print('Modelo não localizado')
        j += 1
        sleep(1)
        login_bem_sucedido = c60_confirma_login()
    return login_bem_sucedido
