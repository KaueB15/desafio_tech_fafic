from unidecode import unidecode

def salvarArquivo(arquivo):
    f = open(f'resposta.txt', 'a')
    f.write(arquivo)
    f.close()
    
def salvarResposta(resposta):
    arquivo = unidecode(resposta)
    salvarArquivo(arquivo)