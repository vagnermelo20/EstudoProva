#ex lista1[2, 4, 3]; lista2[5, 6, 4]
#resultado [7, 0, 8]. seria: 342 + 465 = 807

l1 = [2, 4, 3]
l2 = [5, 6, 4]
l3 = []
l1 = l1[::-1]
l2 = l2[::-1]
numero1 = int(''.join(str(num) for num in l1))
numero2 = int(''.join(str(num) for num in l2))

numerofinal = str(numero1 + numero2)

for numero in numerofinal:
    numero = int(numero)
    l3.append(numero)

print(l3[::-1])