#1 - Alimentar IP's de Acesso Utilizando CSV FEITO
#2 - Identificar o Modelo do Roteador Utilizando o Tittle FEITO
#3 - Chamar o Arquivo Correspondente ao Modelo FEITO
#4 - Marcar IP' como Visitado, e escrever se foi possivel acessar ou não
#5 - Pegar Proximo Ip na Planilha e Reiniciar o Processo FEITO

from wr849_script import *
from time import sleep
from funcoes import *
from c60_script_funcoes import c60_completo_quebrado_em_funcoes
import os
from definicoes_iniciais import *

def main():

    # Inicialização do Browser
    browser.maximize_window()

    #Leitura do CSV com os IP's de Acesso
    lista_ip = ler_csv(arquivo_csv)
    i = cont_ip(lista_ip)
    print(f"Total de IP's Identificados no Arquivo: {i}")

    j = 0
    while j <= i-1:

        ip = trata_ip(lista_ip[j])
        print(f'Acessando: {ip}')

        browser.get(ip)
        sleep(3)

        titulo = browser.title      #Captura titulo da Pagina (Modelo do Roteador)
        titulo = trata_titulo(titulo)       #Trata String do Titulo

        if titulo == 'archerc60':
            c60_completo_quebrado_em_funcoes(browser)
        elif titulo == 'tlwr849n':
            wr849_completo(browser, senha, dns_primario, dns_secundario, ntp_primario, ntp_secundario)
        else:
            print('Modelo Não Compativel')

        j += 1
        os.system('cls')

    print('LISTA FINALIZADA')




if __name__ == '__main__':
    main()