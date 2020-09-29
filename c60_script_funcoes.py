from c60_funcoes import *
from funcoes import tentativas_login


def c60_completo_quebrado_em_funcoes(titulo):
    try:
        tentativas_login(titulo)
        sleep(1)
        realizado_login = c60_confirma_login()
        if realizado_login:
            try:
                c60_botao_avancado()
                try:
                    sleep(3)
                    c60_botao_rede()
                    sleep(1.5)
                    c60_botao_DHCP()
                    sleep(3)
                    c60_DHCP()
                except:
                    print('Não Foi Possivel configurar o DHCP')
                try:
                    c60_wireless()
                except:
                    print('Não foi possivel configurar WIFI')
                try:
                    c60_scroll_sidebarr()
                    sleep(0.5)
                    c60_botao_sis_tools()
                    sleep(1)
                    c60_botao_ntp()
                    c60_ntp()
                    c60_logoff()
                except:
                    print('Não foi possivel Atualizar o NTP')
                    c60_logoff()
            except:
                print('Botão Avançado não localizado')
    except Exception as ex:
        print('Não foi possivel fazer login')
        print(ex)