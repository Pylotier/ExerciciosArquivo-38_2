import os

dir: str = ''
arq: str = ''

def main():
    arquivoPermissao: str = '/tmp/exercicios/'
    os.chmod(arquivoPermissao, 0o744)

    lerNumeros()

def lerNumeros():
    global dir
    global arq

    dir = '/tmp/exercicios/'
    arq = 'ex38.txt'
    file: str = ''
    tipo: str = ''
    enc: str = ''
    linha: str = ''
    arquivo: str = ''

    

    if(os.path.exists(dir) and os.path.isdir(dir)):
        tipo = 'r'
        arquivo = dir + arq
        enc = 'utf-8'
        if (os.path.exists(arquivo)):
            with open (arquivo, tipo, encoding=enc) as file:
                for linha in file:
                    linha = linha.strip()
                    if linha.isdigit():
                        if (int(linha) % 5 == 0):
                            dir2 = '/tmp/exercicios/'
                            arq2 = 'ex38_2.txt'
                            arquivo2 = dir2 + arq2
                            with open (arquivo2, tipo, encoding=enc) as file:
                                file.write(str(linha) + "\n") 
                    else:
                        break   
        else:
            print("Arquivo não encontrado")
    else:
        print('Diretorio invalido')
        

if (__name__ == "__main__"):
    main()
