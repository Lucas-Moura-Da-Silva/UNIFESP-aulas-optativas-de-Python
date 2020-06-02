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

#importação da biblioteca Numpy
import numpy as np

#criação da matriz mat
mat = np.random.randint(-5, 5,(4,3))

#a) Escreva um comando que retorna o valor absoluto dos
#elementos dessa matriz.
soma = np.sum(mat) #soma
print(f"A soma do vetor mat é {soma}")

print("-="*30)

#b) Escreva um comando que retorna o seno dos valores
#contidos na primeira linha dessa matriz.
numseno = np.sin(mat[[0], :]) #seno

for elementos in range(0, 3):
    print(f"O seno da {elementos + 1}º elemento da matriz mat é {numseno[0][elementos]}")
print(numseno)

print("-="*30)

#c) Escreva um comando que retorne o valor máximo das
#colunas da matriz
for elementos in range(1, 4):
    print(f"O valor máximo da {elementos}º coluna é {mat.max(0)[elementos-1]}")
print(mat.max(0))

print("-="*30)

#d) Calcule a soma dos elementos em cada coluna da matriz
for elementos in range(1,4):
    print(f"A soma da {elementos}º coluna é de {mat.sum(0)[elementos - 1]}")
print(mat.sum(0))

print("-="*30)

#e) Calcule a soma dos elementos em cada linha da matriz
for elementos in range(1,5):
    print(f"A soma da {elementos}º linha é de {mat.sum(1)[elementos -1]}")
print(mat.sum(1))

print("-="*30)

#f) Calcule o produto entre os elementos de cada coluna da
#matriz. Dica: procure no google como resolver isso
for elementos in range(1,4):
    print(f"O produto da {elementos}º coluna é de {mat.prod(0)[elementos -1]}")
print(mat.prod(0))
