from unidecode import unidecode

def salvarArquivo(arquivo):
    f = open(f'resposta.txt', 'a')
    f.write(arquivo)
    f.close()
    
def salvarProdutos(resposta):
    arquivo = unidecode(resposta)
    salvarArquivo(arquivo)   
         
def lerArquivo(login):
    f = open(f'produtos_{login}.txt', 'r')
    print(40*'=')
    for linha in f.readlines():
        print(linha, end='')
    f.close()