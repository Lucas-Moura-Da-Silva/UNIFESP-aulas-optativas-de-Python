'''2) Escreva uma expressão que possa selecionar apenas os
elementos de índice par em um vetor, independente do
tamanho do vetor. Teste essa expressão em alguns vetores da
sua escolha.'''

import numpy as np

lista = list()
qntd = int(input('Quantos números você quer colocar no vetor?'))

for repeticao in range(1, qntd + 1):
    num = float(input(f"{repeticao}º número:"))

    if num % 2 == 0:
        lista.append(num)

pares = np.array(lista)

print(pares)