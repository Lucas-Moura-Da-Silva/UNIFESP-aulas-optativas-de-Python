'''3) Escreva uma função que receba dois números e retorne True
se o primeiro número for múltiplo do segundo.'''

#cores
cores = {'limpa':'\033[m',
         1:'\033[1;30m',
         2:'\033[1;31m',
         3:'\033[1;32m',
         4:'\033[1;33m',
         5:'\033[1;34m',
         6:'\033[1;35m',
         7:'\033[1;36m'}

#importação da biblioteca random
from random import randint


#função para cores aleatorias
def color():
    return cores[randint(1, 7)]

#função para limpar
def limpa():
    return cores['limpa']


def multiplo(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False


# Programa principal
num1 = int(input(f"Digite o {color()}primeiro número{limpa()}:"))
num2 = int(input(f"Digite o {color()}segundo número{limpa()}:"))

print(multiplo(num1, num2))

