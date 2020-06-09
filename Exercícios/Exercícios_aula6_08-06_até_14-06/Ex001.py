'''1) Escreva uma função chamada fatorial para calcular o fatorial
de um número inteiro.'''

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
    cor = cores[randint(1, 7)]
    return cor

#função para limpar
def limpa():
    limpa = cores['limpa']
    return limpa


#Função fatorial
def fatorial(numfat):
    fat = 1
    for rep in range (num, 0, -1):
        fat *= rep

    return fat


#Programa principal
num = int(input('Digite um número para saber o seu fatorial:'))

fat = (fatorial(num))

print(f"O {color()}fatorial{limpa()} de {color()}{num}{cores['limpa']} é igual a {color()}{fat}{limpa()}.")