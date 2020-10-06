from funcoes import abre_navegador, ler_csv

senha, tamanho = ler_csv('senhas.csv')
lista_ip, tamanho_lista_ip = ler_csv('testecsv.csv')

dns_primario = '177.55.32.237'
dns_secundario = '8.8.8.8'

ntp_primario = 'a.btp.br'
ntp_secundario = 'b.ntp.br'

arquivo_csv = 'testecsv.csv'


#Abre Browser
browser = abre_navegador()