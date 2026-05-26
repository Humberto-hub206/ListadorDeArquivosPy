import os

def listarTodosArquivos(caminho):
    if not os.listdir(caminho):
        print("Não tem arquivos no diretório.")
        return

    for item in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, item)
        
        if os.path.isdir(caminho_completo):
            print(f"[PASTA] {item}")
        else:
            print(f"[ARQUIVO] {item}")

def listarArquivoPorExtensao(caminho, extensao):
    arquivos_encontrados = [arq for arq in os.listdir(caminho) if arq.endswith(extensao)]
    
    if not arquivos_encontrados:
        print("Não tem arquivos com essa extensão neste diretório.")
        return
        
    for arquivo in arquivos_encontrados:
        print(arquivo)

try:
    caminho = input("Digite o caminho para o diretório: ")
    
    if not os.path.exists(caminho):
        raise FileNotFoundError
        
    print("\n1- Listar todos os arquivos\n2- Listar arquivos por extensão")
    escolha = int(input("O que você deseja listar neste diretório? "))
    
    match escolha:
        case 1:
            listarTodosArquivos(caminho)
        case 2:
            extensao = input("Digite a extensão que deseja procurar (ex: .txt): ")
            listarArquivoPorExtensao(caminho, extensao)
        case _:
            print("Digite uma das opções. tente novamente.")
            
except FileNotFoundError:
    print("Diretório não encontrado!")
except PermissionError:
    print("Você não tem permissão para acessar essa pasta!")
except ValueError:
    print("Input inválido para a variável, tente novamente.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
