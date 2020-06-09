'''7) Crie um vetor x com 60 pontos linearmente espaçados entre
-2π e 2π e construa o gráfico a baixo. Utilize as bibliotecas
numpy e matplotlib'''

#cores
cores = {'limpa':'\033[m',
         1:'\033[1;30m',
         2:'\033[1;31m',
         3:'\033[1;32m',
         4:'\033[1;33m',
         5:'\033[1;34m',
         6:'\033[1;35m',
         7:'\033[1;36m'}


#função para cores aleatorias
def color():
    return cores[randint(1, 7)]

#função para limpar
def limpa():
    return cores['limpa']


#importação da biblioteca numpy
import numpy as np

#importação da biblioteca matplotlib
import matplotlib.pyplot as plt

#importação da biblioteca random
from random import randint

#----------------------------------------------#
            #progrma principal

#variavel de -2pi até 2pi
x = np.linspace(-(2*np.pi), 2*np.pi, 60)

#separação do gráfico
plt.subplot(2,2,1)

#primeiro gráfico
plt.title("Função sen(x)")

senoy = list()

for repeticao in x:
    sen = np.math.sin(repeticao)
    senoy.append(sen)

plt.xlabel("valor de x")
plt.ylabel("valor de sen(x)")


plt.plot(x, senoy, color = (0.8, 0.2, 1, 0.9))


#----------------------------------------------#

#segundo gráfico
plt.subplot(2,2,2)

plt.title("Função cos(x)")

cosy = list()

for repeticao in x:
    cos = np.math.cos(repeticao)
    cosy.append(cos)

plt.xlabel("valor de x")
plt.ylabel("valor de cos(x)")


aleatorio = str(randint(0, 20))

# faz mudar de cor aleatóriamente
plt.bar(x, cosy, color='C' + aleatorio)


#----------------------------------------------#

#terceiro gráfico
plt.subplot(2,2,3)

plt.title("Função tg(x)")

tgy = list()

for repeticao in x:
    tg = np.math.tan(repeticao)
    tgy.append(tg)

plt.xlabel("valor de x")
plt.ylabel("valor de tg(x)")

plt.scatter(x, tgy, color = (0.9, 0.4, 0.4, 0.9))


#----------------------------------------------#

plt.show()
