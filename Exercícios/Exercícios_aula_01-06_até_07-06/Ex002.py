'''2) Escreva uma expressão que possa selecionar apenas os
elementos de índice par em um vetor, independente do
tamanho do vetor. Teste essa expressão em alguns vetores da
sua escolha.'''

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
import random

#importação da biblioteca numpy
import numpy as np

lista = list()
qntd = int(input('Quantos números você quer colocar no vetor?'))

for repeticao in range(1, qntd + 1):
    num = float(input(f"{cores[random.randint(1,7)]}{repeticao}º número:{cores['limpa']}"))

    if num % 2 == 0:
        lista.append(num)

pares = np.array(lista)

print(f"Os números pares são ", end='')
for repeticoes in range(0, len(pares)):
    print(f"{cores[random.randint(1,7)]}{pares[repeticoes]}{cores['limpa']}", end='')

    if repeticoes == len(pares)-1:
        print('.')

    else:
        print(',', end=' ')
