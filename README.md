# EstudoProva



# Tipos de Exeções
É só usar o try and Except


exept ValueError
"Quando o valor passado é inadequado"

except NameError
"não consegue achar o nome de uma váriavel"

except ZeroDivisionError
"não pode dividir por zero"

except FileNotFoundError
"Não achou o arquivo"


# Manipulação de arquivo

usa assim:

arquivo = open("arquivo.txt", "algo", encoding="utf-8")
Esse algo pode ser r para ler
a para adicionar
w para criar outro arquivo e adicionar

linhas = arquivo.readlines()
for linha in linhas:
ai faz uma lógica

# funcao

lembrar de usar return