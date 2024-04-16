import os

#DEFINIÇÕES
MenuPrincipal = 'm'
AdicionarPrefixo = 'p'
SubstituirTexto = 's'
TrocarPasta = 't'
Sair = 'q'
Sim = 'y'
Nao = 'n'

#FUNÇÕES
def opcaoInvalida(resposta="Opção"):
    os.system("cls")
    print(f"{resposta} inválido(a).")


#MAIN LOOP
while True:
    os.system("cls")
    print("Utilitários para Manipulação de Arquivos:\n\n| P | Adicionar Prefixo a Arquivos \n| S | Substituir Texto \n| Q | Sair")
    opcao = input("\nSelecione uma opção: ").lower()

    if opcao == AdicionarPrefixo:
        firstWhile = 1
        while firstWhile:
            os.system("cls")
            caminho = input("Pasta: ")
            if os.path.isdir(caminho):
                while True:
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
                    print("\nDeseja fazer mais alterarações de prefixo nesta pasta?\n\n| Y | Sim\n| M | Menu Principal(M)\n| T | Trocar Pasta")
                    opcao = input("\nSelecione uma opção: ").lower()

                    if opcao == Sim:
                        os.system("cls")
                        continue
                    elif opcao == MenuPrincipal:
                        firstWhile = 0
                        break
                    elif opcao == TrocarPasta:
                        break
                    else:
                        opcaoInvalida()
                        print("Redirecionando para Menu Principal.")
                        firstWhile = 0
                        os.system("pause")
                        break

            else:
                opcaoInvalida("Caminho")
                print("Tentar de novo?\n\n| Y | Sim\n| M | Menu Principal: ")
                opcao = input("\nSelecione uma opção: ").lower()
                
                if opcao == Sim:
                    continue
                elif opcao == MenuPrincipal:
                    firstWhile = 0
                    break
                else:
                    opcaoInvalida()
                    print("Redirecionando para Menu Principal.")
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
                        
                    print("\nDeseja fazer mais alterarações de prefixo nesta pasta?\n\n| Y | Sim\n| M | Menu Principal\n| T | Trocar Pasta")
                    opcao = input("\nSelecione uma opção: ").lower()

                    if opcao == Sim:
                        continue
                    elif opcao == TrocarPasta:
                        break
                    elif opcao == MenuPrincipal:
                        firstWhile = 0
                        break
                    else:
                        opcaoInvalida()
                        print("Redirecionando para Menu Principal.")
                        firstWhile = 0
                        os.system("pause")
                        break
            else:
                opcaoInvalida("Caminho")
                print("\nTentar de novo?\n\n| Y | Sim\n| M | Menu Principal")
                opcao = input("\nSelecione uma opção: ").lower()
                
                if opcao == Sim:
                    continue
                elif opcao == MenuPrincipal:
                    break
                else:
                    opcaoInvalida()
                    print("Redirecionando para Menu Principal.")
                    os.system("pause")
                    break


    elif opcao == Sair:
        break

    else:
        opcaoInvalida()
        os.system("pause")