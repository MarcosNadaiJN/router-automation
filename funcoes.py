#Tratamento de Titulo

def trata_titulo (titulo_original):
    titulo = titulo_original
    titulo = titulo.lower()
    titulo = titulo.strip()
    titulo = titulo.replace(' ', '')
    titulo = titulo.replace('-', '')
    return titulo
