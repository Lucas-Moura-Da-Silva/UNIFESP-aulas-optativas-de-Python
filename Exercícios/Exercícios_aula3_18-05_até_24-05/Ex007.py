'''7) Escreva um script que exibe a seguinte tábua de
multiplicação na tela:
1
2 4
3 6 9
4 8 12 16
5 10 15 20 25'''

from random import randint

#cores
cores = {'limpa':'\033[m',
         1:'\033[1;30m',
         2:'\033[1;31m',
         3:'\033[1;32m',
         4:'\033[1;33m',
         5:'\033[1;34m',
         6:'\033[1;35m',
         7:'\033[1;36m'}

quantos_mutiplicar = int(input('Até quantos numeros você quer multiplicar?'))

#repetição FOR
for repeticao in range(1, quantos_mutiplicar + 1):

    #condição
    if repeticao % 2 == 0:
        print(end=f"{cores[randint(1,7)]}")
    else:
        print(end=f"{cores[randint(1,7)]}")

    #repetição
    for c in range(1, repeticao+1):
        multiplicacao = repeticao * c
        print(f"{multiplicacao}", end=' ')

    print( end='\n')