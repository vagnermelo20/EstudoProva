i = 0
while i == 0:
    frase = input("Escreva uma frase\n")
    palavras = frase.strip().split(" ")
    for i in palavras:
        oi = len(i)
        certo = i.replace(i, str(oi))
    if frase == '0':
        i+=1