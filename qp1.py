#w escreve, mas apaga o que existe na lista
#r lê
#a escreve mas não apaga

#.strip() exclui o que está nos parentes
#.split() cria listas separando as partes
arquivo = open("arquivo.txt", "w", encoding="utf-8")
arquivo.write("200.135.80.9\n192.268.1.1\n8.35.67.74\n257.32.4.5\n85.345.1.2\n1.2.3.4\n9.8.234.5\n192.168.0.256")

arquivo = open("arquivo.txt", "r", encoding="utf-8")
linhas = arquivo.readlines()

for linha in linhas:
    numeros = linha.strip().split(".")

    numeros0 = int(numeros[0])
    numeros1 = int(numeros[1])
    numeros2 = int(numeros[2])
    numeros3 = int(numeros[3])

    if numeros0 > 255 or numeros1 > 255 or numeros2 > 255 or numeros3 > 255:
        print(f"{numeros} não é um ip")
    
    else:
        (print(f"{numeros} é um ip"))