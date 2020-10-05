import os
from funcoes import *
from time import sleep
from definicoes_iniciais import *

def main():

    # Inicialização do Browser
    browser.maximize_window()

    #Leitura do CSV com os IP's de Acesso
    lista_ip, i = ler_csv('testecsv.csv')
    print(f"Total de IP's Identificados no Arquivo: {i}")

    j = 0
    while j <= i-1:

        ip = trata_lista(lista_ip[j])
        print(f'Acessando: {ip}')

        browser.get('http://'+ip)           #Acessa IP contido no CSV
        sleep(2)

        titulo = trata_titulo(browser.title)            #Captura titulo da Pagina (Modelo do Roteador) e Trata a String

        identifica_modelo(titulo)

        j += 1
        os.system('cls')

    print('LISTA FINALIZADA')


if __name__ == '__main__':
    main()