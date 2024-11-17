comp = int(input("Comp: \n"))

for i in range (comp):
    notas = []
    nome = input("Nome\n")
    dif = float(input("Dif\n"))
    for a in range(7):
        nota = float(input("NOta\n"))
        notas.append(nota)
    soma = sum(notas) - max(notas) - min(notas)
    resultado = soma * dif
    print(f"{nome} {resultado}\n")
    