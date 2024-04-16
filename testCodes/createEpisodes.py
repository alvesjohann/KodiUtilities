import os

caminho = input("Pasta: ")
temporada = int(input("Temporada: "))

txtEpisodes = input("Caminho do arquivo .txt com os episódios: ")
if txtEpisodes[:1] == "\"":
    txtEpisodes = txtEpisodes[1:len(txtEpisodes)-1]
txtEpisodes = os.path.abspath(txtEpisodes)


if temporada < 10:
    temporada = '0' + str(temporada)
else:
    temporada = str(temporada)

os.chdir(caminho)
arquivos = os.listdir()
ArquivosAlterados = 0

with open(f'{txtEpisodes}', 'r') as dados:
    lines = dados.readlines()

episodio = 0

for arquivo in arquivos:
    caminhoArquivo = os.path.join(caminho, arquivo)
    if os.path.isdir(caminhoArquivo):
        continue
    else:
        fileName, fileExtension = os.path.splitext(arquivo)

        for line in lines:
            ifLine = line[:-1].lower().replace('\'','').replace('?','').replace(',','').replace(" ","").replace("-","")
            ifFileName = fileName.lower().replace('\'','').replace('?','').replace(',','').replace(" ","").replace("-","")

            if ifLine == ifFileName:
                episodio = int(lines[lines.index(line)-1][:len(lines[lines.index(line)-1])-1])

                if episodio < 10:        
                    os.rename(arquivo, f'S{temporada}E0{episodio} {str(arquivo)}')
                else:
                    os.rename(arquivo, f'S{temporada}E{episodio} {str(arquivo)}')

                ArquivosAlterados += 1

print(f"Foram alterados {ArquivosAlterados} arquivos.")
os.system("pause")