'''1) Crie uma rotina que solicite ao usuário dois lados de um
triângulo e ângulo , em graus, entre eles e retorna o
comprimento do terceiro lado. Use a lei dos cossenos.'''

#cores
cores = {'limpa':'\033[m',
         'branco':'\033[1;30m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'roxo':'\033[1;35m',
         'ciano':'\033[1;36m'}

#importação da biblioteca/módulo "math"
import math as m

#input's do questão
lado_a = float(input('Qual o valor do primeiro lado do triângulo?'))
lado_b = float(input('Qual o valor do segundo lado do triângulo?'))
angulo = int(input('Qual o ângulo oposto ao lado de você quer descobrir em graus?'))

#transformando o angulo de grau para radianos
angulo_rad = (m.pi*angulo)/180

#calculo do terceiro lado por lei dos cossenos
lei_cosseno = m.sqrt(lado_a**2 + lado_b**2 - 2*lado_a*lado_b*m.cos(angulo_rad))

print('-='*23)
#retorno com o terceito lado do triãngulo
print(f"O terceiro lado do triângulo vale {cores['roxo']}{lei_cosseno:.2f}{cores['limpa']}.")
