def escrever():
    arquivo = open("arquivo.txt", "w", encoding="utf-8")

    for i in range (0, 10):
        palavra = input("Escreva\n")
        arquivo.write(f"{palavra} \n")
    arquivo.close

def ler():
    star_wars = 0
    star_trek = 0
    nulos = 0
    mais_votado = star_wars
    menos_votado = star_wars
    arquivo = open("arquivo.txt", "r", encoding="utf-8")
    linhas = arquivo.readlines()
    for linha in linhas:

        if linha == 1:
            star_wars +=1
        
        elif linha == 2:
            star_trek +=1
        
        else:
            nulos +=1
    
    if star_trek > star_wars:
        star_trek = mais_votado

    if star_trek < star_wars:
        star_trek = menos_votado
    print(star_trek)
    print(star_trek)
    if star_trek == star_wars:
        print(f'O filme Star Wars e Star Trek estão empatados com {star_wars}')
    else:
        print(f"O filme mais votado foi {mais_votado} com {mais_votado()}")
    
    print(f"Teve {nulos} votos nulos")
i = 0
while i == 0:
    lerr = int(input("Digite 1 para votar, 2 pra ver, 3 pra sair\n"))
    if lerr == 1:
        escrever()
    elif lerr ==2:
        ler()
    
    elif lerr == 3:
        i+= 1