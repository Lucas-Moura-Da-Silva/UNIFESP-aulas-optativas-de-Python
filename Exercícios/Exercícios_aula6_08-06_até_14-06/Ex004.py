'''4) Escreva uma função chamada área_quad que recebe os
lados de um retângulo e retorne sua área.'''

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


# Função da área do retangulo
def área_quad(lar, com):
    area = lar * com
    return area


# Função do título
def titulo():
    print(f"{color()}-" * len(tit))
    print(f"{color()}{tit}{limpa()}")
    print(f"{color()}-" * len(tit))


# Função do resposta
def resposta():
    print(f"{color()}__" * len(tit))

    print(
        f"A área de um retangulo de {color()}{largura}m{limpa()} x {color()}{comprimento}m{limpa()} é de"
        f" {color()}{área_quad(largura, comprimento)}m²{limpa()}."
          )

    print(f"{color()}--" * len(tit))


# Programa principal
tit = '|     Área do retangulo     |'
titulo()

largura = float(input(f"{color()}LARGURA(m){limpa()}: "))
comprimento = float(input(f"{color()}COMPRIMENTO(m){limpa()}: "))

# imprimir a resposta e a chamada da Função
resposta()