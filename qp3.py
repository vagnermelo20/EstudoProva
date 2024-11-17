def escrever(arquivo_nome = "arquivo.txt"):
    arquivo = open(arquivo_nome, "w", encoding="utf-8")
    for i in range(6):
        escrever = input("Escreva o nome e sobrenome\n")
        arquivo.write(f"{escrever}\n")
    arquivo.close()

def mudar(arquivo_nome = "arquivo.txt"):
    arquivo = open(arquivo_nome, "r+", encoding="utf-8")
    linhas = arquivo.readlines()
    for linha in linhas:
        print (linha)
        pergunta = input("Voce quer alterar a linha: \n")
        if pergunta == "Sim":
            nova_linha = input("Coloque o novo nome e sobrenome: \n")
            linha = nova_linha
            print(linha)
            print("Nome alterado\n")
        else:
            print("Nome mantido\n")
    arquivo.writelines(linha) 
mudar()