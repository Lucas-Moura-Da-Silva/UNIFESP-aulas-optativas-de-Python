'''6) Crie uma função na qual calcula o valor do cos a partir da série
de Taylor (50 primeiros termos) e seno a partir da seguinte
identidade. Obs: Fazer a serie utilizando for e utilizar a função
fatorial desenvolvida no exercício 1.'''

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


#importação do numpy
import numpy as np


#Função fatorial
def fatorial(num):
    fat = 1
    for rep in range(num*2, 0, -1):
        fat *= rep
    return fat


#função do expoentes
def exp(num):
    exp = num * 2
    return exp


# Função para calcular o seno
def calc():
    if rep % 2 == 0:
        res = (angle_rad ** exp(rep)) / fatorial(rep)
    else:
        res = -(angle_rad ** exp(rep)) / fatorial(rep)

    return res


# Função para achar o cosseno
def sen(cos):
    sen = np.math.sqrt(1 - (cos ** 2))

    if 360 > angle_graus > 180:
        sen *= (-1)

    sen = float(f"{sen:.4f}")

    return sen


#Função para imprimir
def imprimir():
    print()
    print(f"{color()}-={limpa()}" * len(tit))

    # imprimindo o cos(x)
    print(f"O cosseno de {color()}{angle_graus}°{limpa()} ou {color()}{angle_rad:.4f}rad{limpa()} é"
          f" {color()}{cos}{limpa()}.")

    # imprimindo o sen(x)
    print(f"O seno de {color()}{angle_graus}°{limpa()} ou {color()}{angle_rad:.4f}rad{limpa()} é"
          f" {color()}{sen}{limpa()}.")

    print(f"{color()}-={limpa()}" * len(tit))


# Função do título
def titulo():
    print(' '*11, f"{color()}-{limpa()}" * len(tit))
    print(' '*11, f"{color()}{tit}{limpa()}")
    print(' '*11, f"{color()}-{limpa()}" * len(tit))
    print()


#Programa principal
# Programa principal
tit = '|     COSSENO E SENO     |'
titulo()


#input da questão
angle_graus = float(input(f"Qual ângulo em grau você quer saber o {color()}cosseno{limpa()} e o "
                          f"{color()}seno{limpa()}? "))



#Converção de graus para radianos
angle_rad = np.math.radians(angle_graus)


#calculo para a sequência de Taylor em cos(x)
cos = 0

for rep in range(0, 50):
    cos += calc()
cos = float(f"{cos:.4f}")



#calculo para o seno
sen = sen(cos)


#imprimir as respostas
imprimir()


