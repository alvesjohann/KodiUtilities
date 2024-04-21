import os

#### TÍTULOS DE MENU ####
titleMenuPrincipal = "MANIPULAÇÃO DE ARQUIVOS"
titleAlteracao = "Deseja fazer mais alterarações nesta pasta?"
titleTentarDeNovo = "Tentar de novo?"

#### DEFINIÇÕES DE OPÇÕES #### teste
MenuPrincipal = 'm'
AdicionarPrefixo = 'p'
RemoverPrefixo = 'r'
SubstituirTexto = 's'
OrganizarEpisodios = 'e'
TrocarPasta = 't'
Sair = 'q'
Sim = 'y'
Nao = 'n'

#### DICIONÁRIOS DE OPÇÕES DE MENU ####
optionsMenuPrincipal = {
    'P' : 'Adicionar Prefixo a Arquivos',
    'R' : 'Remover Prefixo de Arquivos',
    'S' : 'Substituir Texto',
    'E' : 'Organizar Episódios',
    'Q' : 'Sair'
}

optionsAlteracao = {
    'Y' : 'Sim',
    'M' : 'Menu Principal',
    'T' : 'Trocar Pasta'
}

optionsTentarDeNovo = {
    'Y' : 'Sim',
    'M' : 'Menu Principal'
}

#### FUNÇÕES ####
def showMenu(MenuToShow, title=""):
    if title != "":
        print(f"{title}\n")
    else:
        print("")
    
    for shortcut, menu in MenuToShow.items():
        print(f"| {shortcut} | {menu}")
    
    opcao = input("\nSelecione uma opção: ").lower()

    return opcao

def opcaoInvalida(resposta="Opção", menuRetorno=""):
    os.system("cls")
    print(f"{resposta} inválido(a).")
    if menuRetorno != "":
        print(f"Redirecionando para {menuRetorno}.")

#### LOOP PRINCIPAL ####
while True:
    os.system("cls")
    opcao = showMenu(optionsMenuPrincipal, titleMenuPrincipal)

    if opcao == AdicionarPrefixo:
        firstWhile = 1
        while firstWhile:
            os.system("cls")
            caminho = input("Pasta: ")
            if os.path.isdir(caminho):
                while True:
                    os.system("cls")
                    print(caminho)
                    prefixo = input("Prefixo: ")

                    os.chdir(caminho)
                    arquivos = os.listdir()
                    ArquivosAlterados = 0

                    for arquivo in arquivos:
                        caminhoArquivo = os.path.join(caminho, arquivo)
                        if os.path.isdir(caminhoArquivo):
                            continue
                        if arquivo[:len(prefixo)] == prefixo:
                            continue
                        else:
                            os.rename(arquivo, prefixo + str(arquivo))
                            ArquivosAlterados += 1

                    print(f"Foram alterados {ArquivosAlterados} arquivos.")
                    opcao = showMenu(optionsAlteracao,titleAlteracao)

                    if opcao == Sim:
                        continue
                    elif opcao == MenuPrincipal:
                        firstWhile = 0
                        break
                    elif opcao == TrocarPasta:
                        break
                    else:
                        opcaoInvalida(menuRetorno="Menu Principal")
                        firstWhile = 0
                        os.system("pause")
                        break

            else:
                opcaoInvalida("Caminho")
                opcao = showMenu(optionsTentarDeNovo,titleTentarDeNovo)
                
                if opcao == Sim:
                    continue
                elif opcao == MenuPrincipal:
                    firstWhile = 0
                    break
                else:
                    opcaoInvalida(menuRetorno="Menu Principal")
                    firstWhile = 0
                    os.system("pause")
                    break

    elif opcao == RemoverPrefixo:
        firstWhile = 1
        while firstWhile:
            os.system("cls")
            caminho = input("Pasta: ")
            if os.path.isdir(caminho):
                while True:
                    os.system("cls")
                    print(caminho)
                    prefixo = input("Quantidade de caracteres a remover: ")

                    try: #filtro caso o input deva ser obrigatóriamente um número
                        prefixo = int(int(prefixo)/1)
                    except:
                        opcaoInvalida()
                        opcao = showMenu(optionsTentarDeNovo,titleTentarDeNovo)
                        
                        if opcao == Sim:
                            continue
                        elif opcao == MenuPrincipal:
                            firstWhile = 0
                            break
                        else:
                            opcaoInvalida(menuRetorno="Menu Principal")
                            firstWhile = 0
                            os.system("pause")
                            break

                    os.chdir(caminho)
                    arquivos = os.listdir()
                    ArquivosAlterados = 0

                    for arquivo in arquivos:
                        caminhoArquivo = os.path.join(caminho, arquivo)
                        if os.path.isdir(caminhoArquivo):
                            continue
                        if prefixo > len(arquivo):
                            print(f"O número de caracteres a excluir é maior que {arquivo}. Nada foi alterado.")
                        else:
                            os.rename(arquivo, str(arquivo[prefixo:]))
                            ArquivosAlterados += 1

                    print(f"Foram alterados {ArquivosAlterados} arquivos.")
                    opcao = showMenu(optionsAlteracao,titleAlteracao)

                    if opcao == Sim:
                        continue
                    elif opcao == MenuPrincipal:
                        firstWhile = 0
                        break
                    elif opcao == TrocarPasta:
                        break
                    else:
                        opcaoInvalida(menuRetorno="Menu Principal")
                        firstWhile = 0
                        os.system("pause")
                        break

            else:
                opcaoInvalida("Caminho")
                opcao = showMenu(optionsTentarDeNovo,titleTentarDeNovo)
                
                if opcao == Sim:
                    continue
                elif opcao == MenuPrincipal:
                    firstWhile = 0
                    break
                else:
                    opcaoInvalida(menuRetorno="Menu Principal")
                    firstWhile = 0
                    os.system("pause")
                    break

    elif opcao == SubstituirTexto:
        firstWhile = 1
        while firstWhile:
            os.system("cls")
            caminho = input("Pasta: ")
            if os.path.isdir(caminho):
                while True:
                    os.system("cls")
                    print(caminho)
                    strAntigo = input("Trocar: ")
                    strNovo = input("Por: ")

                    os.chdir(caminho)
                    arquivos = os.listdir()
                    ArquivosAlterados = 0

                    if strAntigo == strNovo:
                        print("Termos de troca são idênticos. Nenhum arquivo foi alterado.")
                        os.system("pause")
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
                        
                    opcao = showMenu(optionsAlteracao,titleAlteracao)

                    if opcao == Sim:
                        continue
                    elif opcao == TrocarPasta:
                        break
                    elif opcao == MenuPrincipal:
                        firstWhile = 0
                        break
                    else:
                        opcaoInvalida(menuRetorno="Menu Principal")
                        firstWhile = 0
                        os.system("pause")
                        break
                    
            else:
                opcaoInvalida("Caminho")
                opcao = showMenu(optionsTentarDeNovo,titleTentarDeNovo)
                
                if opcao == Sim:
                    continue
                elif opcao == MenuPrincipal:
                    break
                else:
                    opcaoInvalida(menuRetorno="Menu Principal")
                    os.system("pause")
                    break

    elif opcao == OrganizarEpisodios:
        firstWhile = 1
        while firstWhile:
            os.system("cls")
            caminho = input("Pasta: ")
            if os.path.isdir(caminho):
                while True:
                    os.system("cls")
                    print(caminho)
                    temporada = input("Temporada: ")

                    try: #filtro caso o input deva ser obrigatóriamente um número
                        temporada = int(int(temporada)/1)
                    except:
                        opcaoInvalida()
                        opcao = showMenu(optionsTentarDeNovo,titleTentarDeNovo)
                        
                        if opcao == Sim:
                            continue
                        elif opcao == MenuPrincipal:
                            firstWhile = 0
                            break
                        else:
                            opcaoInvalida(menuRetorno="Menu Principal")
                            firstWhile = 0
                            os.system("pause")
                            break

                    txtEpisodes = input("Caminho do arquivo .txt com os episódios: ")
                    if txtEpisodes[:1] == "\"":
                        txtEpisodes = txtEpisodes[1:len(txtEpisodes)-1]

                    if os.path.isfile(txtEpisodes): #filtro caso o input deva ser obrigatóriamente um arquivo
                        pass
                    else:
                        opcaoInvalida()
                        opcao = showMenu(optionsTentarDeNovo,titleTentarDeNovo)
                        
                        if opcao == Sim:
                            continue
                        elif opcao == MenuPrincipal:
                            firstWhile = 0
                            break
                        else:
                            opcaoInvalida(menuRetorno="Menu Principal")
                            firstWhile = 0
                            os.system("pause")
                            break

                    desconsiderar = input("Desconsiderar caracteres finais? Digite a quantidade ('0' ou Enter não altera nada): ")

                    try: #filtro caso o input deva ser obrigatóriamente um número
                        if desconsiderar == "":
                            desconsiderar = 0
                        desconsiderar = int(int(desconsiderar)/1)
                    except:
                        opcaoInvalida()
                        opcao = showMenu(optionsTentarDeNovo,titleTentarDeNovo)
                        
                        if opcao == Sim:
                            continue
                        elif opcao == MenuPrincipal:
                            firstWhile = 0
                            break
                        else:
                            opcaoInvalida(menuRetorno="Menu Principal")
                            firstWhile = 0
                            os.system("pause")
                            break
                    
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
                                ifLine = line[:-1].lower().replace('\'','').replace('?','').replace(',','').replace(" ","").replace("-","").replace("!","").replace("&","")
                                if desconsiderar == 0:
                                    ifFileName = fileName.lower().replace('\'','').replace('?','').replace(',','').replace(" ","").replace("-","").replace("!","").replace("&","")
                                else:
                                    ifFileName = fileName[:-desconsiderar].lower().replace('\'','').replace('?','').replace(',','').replace(" ","").replace("-","").replace("!","").replace("&","")

                                if ifLine == ifFileName:
                                    episodio = int(lines[lines.index(line)-1][:len(lines[lines.index(line)-1])-1])

                                    if episodio < 10:        
                                        os.rename(arquivo, f'S{temporada}E0{episodio} {str(arquivo)}')
                                    else:
                                        os.rename(arquivo, f'S{temporada}E{episodio} {str(arquivo)}')

                                    ArquivosAlterados += 1

                    print(f"Foram alterados {ArquivosAlterados} arquivo(s).")
                        
                    opcao = showMenu(optionsAlteracao,titleAlteracao)

                    if opcao == Sim:
                        continue
                    elif opcao == TrocarPasta:
                        break
                    elif opcao == MenuPrincipal:
                        firstWhile = 0
                        break
                    else:
                        opcaoInvalida(menuRetorno="Menu Principal")
                        firstWhile = 0
                        os.system("pause")
                        break
                    
            else:
                opcaoInvalida("Caminho")
                opcao = showMenu(optionsTentarDeNovo,titleTentarDeNovo)
                
                if opcao == Sim:
                    continue
                elif opcao == MenuPrincipal:
                    break
                else:
                    opcaoInvalida(menuRetorno="Menu Principal")
                    os.system("pause")
                    break

    elif opcao == Sair:
        break

    else:
        opcaoInvalida(menuRetorno="Menu Principal")
        os.system("pause")