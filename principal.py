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

        acessa_ip_porta(ip)
        sleep(2)

        titulo = trata_titulo(browser.title)    #Captura titulo da Pagina (Modelo do Roteador) e Trata a String

        identifica_modelo(titulo, j)

        j += 1

    print('LISTA FINALIZADA')


if __name__ == '__main__':
    main()