'''2) Escreva uma função chamada maxnum que retorne o maior
número de um conjunto de números. Utilize
empacotamento para fazer a função.'''

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


def titulo():
    print(f"{color()}-" * len(tit))
    print(f"{color()}{tit}{limpa()}")
    print(f"{color()}-" * len(tit))


#Função do maior número
def maxnum(*num):
    max = num[0]

    for rep in num:
        if rep > max:
            max = rep

    txt = f"O {color()}maior{limpa()} valor de {color()}{num}{limpa()} é o {color()}{max}{limpa()}"
    print(f"{color()}-" * len(txt))
    print(f"           {txt}")
    print(f"{color()}-" * len(txt))

# Chamar função titulo
tit = '     MAIOR NÚMERO     '
titulo()

# Chamada da Função
maxnum(1, 2, 5, 4, 9, 6)
