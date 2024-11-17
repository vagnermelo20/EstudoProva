def escrever():
    lista = []

    arquivo = open("arquivo.txt", "r", encoding="utf-8")
    linhas = arquivo.readlines()
    for linha in linhas:
        numero = linha.strip()
        numero = int(numero)
        lista.append(numero)
    
    arquivo.close()



    arquivo = open("arquivo.txt", "a", encoding="utf-8")
    escrever = int(input("Coloca um numero\n "))    
    if lista == []:
            arquivo.write(f"{escrever}\n")
    else:
        if escrever > max(lista):
            arquivo.write(f"{escrever}\n")
    arquivo.close()
def ler():
    lista = []
    arquivo = open("arquivo.txt", "r", encoding="utf-8")
    linhas = arquivo.readlines()
    for linha in linhas:
        linha = linha.strip()
        lista.append(linha)
    return lista

i = 0
while i == 0:
    pergunta = int(input("Bota 1, 2 ou 3\n"))

    if pergunta ==1:
        print("Escreva")
        escrever()
    
    elif pergunta == 2:
        print(ler())
    
    elif pergunta == 3:
        i += 1