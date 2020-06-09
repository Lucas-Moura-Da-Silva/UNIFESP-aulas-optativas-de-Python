'''5) Escreva uma função chamada área_triang que receba a
base e a altura de um triangulo e retorne sua aréa.'''

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


#Função da área do triângulo
def área_triang(bas, alt):
    area = (bas * alt) / 2
    res = f"A {color()}área de um triângulo{limpa()} com {color()}{bas}m de base{limpa()} e" \
          f" {color()}{alt}m de altura{limpa()} é de {color()}{area}m²{limpa()}."
    return res


# Função do título
def titulo():
    print(f"{color()}-{limpa()}" * len(tit))
    print(f"{color()}{tit}{limpa()}")
    print(f"{color()}-{limpa()}" * len(tit))


# Função da resposta
def resposta(res):
    print(f"{color()}__" * len(tit))

    print(res)

    print(f"{color()}--" * len(tit))


#----------------------------------------------#
            #programa principal

tit = "|     Área de um triângulo     |"
titulo()

base = float(input(f"Qual a {color()}base do triângulo{limpa()}?"))
altura = float(input(f"Qual a {color()}altura do triângulo{limpa()}?"))

# imprimir a resposta e a chamada da Função
resposta(área_triang(base, altura))
