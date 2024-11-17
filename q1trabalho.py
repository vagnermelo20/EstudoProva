total = int(input(" total? \n"))
compradas = int(input(" compradas? \n"))
lista = []
for i in range(compradas):
    numero = int(input("Escreva numero\n"))
    if numero not in lista:
        lista.append(numero)
resposta = total - len(lista)

print (resposta)