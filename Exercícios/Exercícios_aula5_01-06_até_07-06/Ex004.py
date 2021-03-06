'''4) Crie uma rotina na qual calcula o valor do cos a partir da sÃ©rie
de Taylor ( 50 primeiros termos) e seno a partir da seguinte
identidade. OBS: essa funÃ§Ã£o nÃ£o pode conter funÃ§Ãµes de loop
tal como: for while. Dica procure no google qual a funÃ§Ã£o em
numpy/python que calcula o fatorial.'''

#cores
cores = {'limpa':'\033[m',
         'branco':'\033[1;30m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'roxo':'\033[1;35m',
         'ciano':'\033[1;36m'}

#importação do numpy
import numpy as np

#importando da biblioteca scipy a função factorial
from scipy.special import factorial

#input da questão
angle_graus = float(input("Qual ângulo em grau você quer saber o cosseno e o seno?"))

#Converção de graus para radianos
angle_rad = np.math.radians(angle_graus)

print(f"{cores['ciano']}-={cores['limpa']}"*30)

#expoentes
exp = np.arange(0,100,2)

x = angle_rad**exp

fact = factorial(exp)

#expressões da série de Taylor
termos = x/fact
termos[1::2]= -1*termos[1::2]

#resultado da série de Taylor
cos = termos.sum()

# imprimindo o cos(x)
print(f"O cosseno de {cores['roxo']}{angle_graus}°{cores['limpa']} ou {cores['amarelo']}"
      f"{angle_rad:.4f}rad{cores['limpa']} é {cores['verde']}{cos:.4f}{cores['limpa']}.")

print(f"{cores['ciano']}-={cores['limpa']}"*30)

#calculo para o seno
sen = np.sqrt(1 - (cos**2))

if 360 > angle_graus >= 180 :
    if angle_graus != 270:
        cos = float(str(cos)[0:6])
        sen = np.sqrt(1 - (cos ** 2))
        if angle_graus == 180:
            sen *= (-1)
    sen *= (-1)

# imprimindo o sen(x)
print(f"O seno de {cores['azul']}{angle_graus}°{cores['limpa']} ou {cores['vermelho']}"
      f"{angle_rad:.4f}rad{cores['limpa']} é {cores['branco']}{sen:.4f}{cores['limpa']}.")