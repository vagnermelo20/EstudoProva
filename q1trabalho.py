def ler():
    total = int(input(" total? \n"))
    if 0 > total < 100:
        return f'{total} é um número não permitido'
    else:
        lista = []
        compradas = int(input(" compradas? \n"))
        for i in range(compradas):
            numero = int(input("Escreva numero\n"))
            if numero not in lista:
                lista.append(numero)
        resposta = total - len(lista)

    print (resposta)