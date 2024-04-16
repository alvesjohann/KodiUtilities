import os

caminho = input("Pasta: ")
prefixo = int(input("Quantidade de caracteres a remover: "))

os.chdir(caminho)
arquivos = os.listdir()
ArquivosAlterados = 0

for arquivo in arquivos:
    caminhoArquivo = os.path.join(caminho, arquivo)
    if os.path.isdir(caminhoArquivo):
        continue
    else:
        os.rename(arquivo, str(arquivo[prefixo:]))
        ArquivosAlterados += 1

print(f"Foram alterados {ArquivosAlterados} arquivos.")
os.system("pause")