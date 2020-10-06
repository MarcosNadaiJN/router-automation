from c60_funcoes import *
from funcoes import tentativas_login


def c60_completo_dividido_em_funcoes(titulo):
    try:
        confirmacao_login = tentativas_login(titulo)
        sleep(1)
        if confirmacao_login:
            try:
                c60_botao_avancado()
                try:
                    sleep(3)
                    c60_botao_rede()
                    sleep(1.5)
                    c60_botao_DHCP()
                    sleep(3)
                    c60_DHCP()
                    DHCP = 1
                except:
                    print('Não Foi Possivel configurar o DHCP')
                    DHCP = 0
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
                    NTP = 1
                    c60_logoff()
                except:
                    print('Não foi possivel Atualizar o NTP')
                    NTP = 0
                    c60_logoff()
            except:
                print('Botão Avançado não localizado')
        else:
            print('Não foi Possivel Fazer Login')
    except Exception as ex:
        print('Não foi possivel fazer login')
        print(ex)
    return confirmacao_login, DHCP, NTP