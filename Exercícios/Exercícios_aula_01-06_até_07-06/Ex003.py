'''3) Crie uma matriz 4 x 3 de números aleatórios inteiros no
intervalo -5 a 5 e armazene em uma variável “mat”.
    a) Escreva um comando que retorna o valor absoluto dos
elementos dessa matriz.
    b) Escreva um comando que retorna o seno dos valores
contidos na primeira linha dessa matriz.
    c) Escreva um comando que retorne o valor máximo das
colunas da matriz
    d) Calcule a soma dos elementos em cada coluna da matriz
    e) Calcule a soma dos elementos em cada linha da matriz
    f) Calcule o produto entre os elementos de cada coluna da
matriz. Dica: procure no google como resolver isso'''

#cores
cores = {'limpa':'\033[m',
         'vermelho':'\033[1;31m',
         'ciano':'\033[1;36m',
         1: '\033[1;30m',
         2: '\033[1;31m',
         3: '\033[1;32m',
         4: '\033[1;33m',
         5: '\033[1;34m',
         6: '\033[1;35m',
         7: '\033[1;36m'}

#importação da biblioteca random
import random

#importação da biblioteca Numpy
import numpy as np

#criação da matriz mat
mat = np.random.randint(-5, 5,(4,3))
print(f"{cores[random.randint(1,7)]}  MATRIZ:")
print(f"{cores[random.randint(1,7)]}{mat}{cores['limpa']}")

print(f"{cores['ciano']}-={cores['limpa']}"*30)

#a) Escreva um comando que retorna o valor absoluto dos
#elementos dessa matriz.
soma = np.sum(mat) #soma
print(f"A soma do vetor mat é {cores['vermelho']}{soma}{cores['limpa']}.")

print(f"{cores['ciano']}-={cores['limpa']}"*30)

#b) Escreva um comando que retorna o seno dos valores
#contidos na primeira linha dessa matriz.
numseno = np.sin(mat)[0] #seno

for elementos in range(0, 3):
    print(f"O seno da {cores[random.randint(1,7)]}{elementos + 1}º{cores['limpa']} elemento da "
          f"matriz mat é {cores[random.randint(1,7)]}{numseno[elementos]}{cores['limpa']}.")
print(numseno)

print(f"{cores['ciano']}-={cores['limpa']}"*30)

#c) Escreva um comando que retorne o valor máximo das
#colunas da matriz
for elementos in range(1, 4):
    print(f"O valor máximo da {cores[random.randint(1,7)]}{elementos}º{cores['limpa']} coluna é "
          f"{cores[random.randint(1,7)]}{mat.max(0)[elementos-1]}{cores['limpa']}.")

print(mat.max(0))

print(f"{cores['ciano']}-={cores['limpa']}"*30)

#d) Calcule a soma dos elementos em cada coluna da matriz
for elementos in range(1,4):
    print(f"A soma da {cores[random.randint(1,7)]}{elementos}º{cores['limpa']} coluna é de "
          f"{cores[random.randint(1,7)]}{mat.sum(0)[elementos - 1]}{cores['limpa']}.")

print(mat.sum(0))

print(f"{cores['ciano']}-={cores['limpa']}"*30)

#e) Calcule a soma dos elementos em cada linha da matriz
for elementos in range(1,5):
    print(f"A soma da {cores[random.randint(1,7)]}{elementos}º{cores['limpa']} linha é de "
          f"{cores[random.randint(1,7)]}{mat.sum(1)[elementos -1]}{cores['limpa']}.")

print(mat.sum(1))

print(f"{cores['ciano']}-={cores['limpa']}"*30)

#f) Calcule o produto entre os elementos de cada coluna da
#matriz. Dica: procure no google como resolver isso
for elementos in range(1,4):
    print(f"O produto da {cores[random.randint(1,7)]}{elementos}º{cores['limpa']} coluna é de "
          f"{cores[random.randint(1,7)]}{mat.prod(0)[elementos -1]}{cores['limpa']}.")

print(mat.prod(0))
