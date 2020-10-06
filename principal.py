import os
from funcoes import *
from time import sleep
from definicoes_iniciais import *

def main():

    # Inicialização do Browser
    browser.maximize_window()

    #Leitura do CSV com os IP's de Acesso
    print(f"Total de IP's Identificados no Arquivo: {tamanho_lista_ip}")

    j = 0
    while j <= tamanho_lista_ip-1:

        ip = trata_lista(lista_ip[j])
        print(f'Acessando: {ip}')

        browser.get('http://'+ip)           #Acessa IP contido no CSV
        sleep(2)

        titulo = trata_titulo(browser.title)            #Captura titulo da Pagina (Modelo do Roteador) e Trata a String

        confimacao_login, DHCP, NTP = identifica_modelo(titulo)     #Configura Roteador e Retorna Flags para Cada Funcionalidade
        '''
            Necessario estudar uma forma,
            Em que não é preciso passar todos estes valores como argumentos dentro das funções.
            Porem o LOG do CSV está funcional.
        '''
        escrita_csv_log(confimacao_login, DHCP, NTP, j)     #Escreve em um CSV o LOG de quais operações foram realizadas

        j += 1
        os.system('cls')

    print('LISTA FINALIZADA')


if __name__ == '__main__':
    main()