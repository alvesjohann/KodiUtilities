import os

caminho = input("Pasta: ")
prefixo = input("Prefixo: ")

os.chdir(caminho)
arquivos = os.listdir()
ArquivosAlterados = 0

for arquivo in arquivos:
    ArquivosAlterados
    caminhoArquivo = os.path.join(caminho, arquivo)
    if os.path.isdir(caminhoArquivo):
        continue
    if arquivo[:len(prefixo)] == prefixo:
        continue
    else:
        os.rename(arquivo, prefixo + str(arquivo))
        ArquivosAlterados += 1

print(f"Foram alterados {ArquivosAlterados} arquivos.")
os.system("pause")