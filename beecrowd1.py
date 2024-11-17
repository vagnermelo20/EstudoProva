# numero = int(input("Escreva um numero"))
# numeros = [
#     ("M", 1000),
#     ("CM", 900),
#     ("D", 500),
#     ("CD", 400),
#     ('C', 100),
#     ('XC', 100),
#     ('L', 100),
#     ('XL', 100),
#     ('X', 100),
#     ('IX', 100),
#     ('V', 100),
#     ('IV', 100),
#     ('I', 100),
# ] 

def arabic_to_roman(num):
    roman_numerals = [
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1)
    ]
    
    result = ""
    for roman, value in roman_numerals:
        while num >= value:
            result += roman
            num -= value
    return result

# Entrada do usuário
N = int(input())
if 0 < N < 1000:
    print(arabic_to_roman(N))
