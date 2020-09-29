import csv
from funcoes import trata_lista
with open('senhas.csv') as csv_file:
    lista_senhas = csv.reader(csv_file)
    lista_senhas = list(lista_senhas)
    print(lista_senhas)
    tamanho = len(lista_senhas)
    lista_senhas = trata_lista(lista_senhas)
    print(lista_senhas)
    lista_senhas = list(lista_senhas)
    print(lista_senhas)
    print(tamanho)