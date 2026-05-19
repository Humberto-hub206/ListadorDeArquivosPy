import os

def listarArquivos(extensao):
    for arquivo in os.listdir():
        if arquivo.endswith(extensao):
            print(arquivo)
    if not any(arquivo.endswith(extensao) for arquivo in os.listdir()):
        print(f"Nenhum arquivo com a extensão {extensao} encontrado.")
try:
    caminho = input("Digite o caminho do diretório: ")
    os.chdir(caminho)

    while True:
        print("1 - .txt\n2 - .word\n3 - .pdf\n4 - .excel\n")
        escolha = int(input("Digite qual tipo de arquivo deseja listar: \n"))
        match escolha:
            case 1:
                extensao = ".txt"
                listarArquivos(extensao)
            case 2:
                extensao = ".docx"
                listarArquivos(extensao)
            case 3:
                extensao = ".pdf"
                listarArquivos(extensao)
            case 4:
                extensao = ".xlsx"
                listarArquivos(extensao)
            case _:
                print("Opção inválida, tente novamente.")
except FileNotFoundError:
    print("Diretório não encontrado.")
except ValueError:
    print("Entrada inválida, por favor digite um número.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")