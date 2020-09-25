from c60_funcoes import *

def c60_completo_quebrado_em_funcoes(browser):
    try:
        c60_login()
        sleep(1)
        url_atual = confirma_login()
        if 'index' in url_atual:
            try:
                c60_botao_avancado()
                sleep(3)
                c60_botao_rede()
                sleep(1.5)
                c60_botao_DHCP()
                sleep(3)
                c60_DHCP()
            except:
                print('Botão Avançado não localizado')
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
        print('Não foi possivel fazer login')