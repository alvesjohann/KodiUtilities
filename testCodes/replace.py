import os

caminho = input("Pasta: ")
strAntigo = input("Trocar: ")
strNovo = input("Por: ")

os.chdir(caminho)
arquivos = os.listdir()
ArquivosAlterados = 0

if strAntigo == strNovo:
    print("Termos de troca são idênticos. Nenhum arquivo foi alterado.")
else:
    for arquivo in arquivos:
        caminhoArquivo = os.path.join(caminho, arquivo)
        if os.path.isdir(caminhoArquivo):
            continue
        if strAntigo in str(arquivo):
            os.rename(arquivo, str(arquivo).replace(strAntigo,strNovo))
            ArquivosAlterados += 1
        else:
            print(f"Não há o termo \"{strAntigo}\" no arquivo \"{arquivo}\"")

    print(f"Foram alterados {ArquivosAlterados} arquivo(s).")

os.system("pause")