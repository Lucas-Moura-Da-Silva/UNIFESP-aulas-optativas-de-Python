'''1) Crie um vetor com 40 elementos igualmente espaçados entre
0 e 2π.'''

'''Os Exercícios efeito daqui por diante, usaremos a biblioteca Numpy e para uma melhor 
visualização das tabelas/matrizes é recomendado usar a ferramenta "spider", "jupyter", 
"colab" ou outra de sua preferencia.'''

#cores
cores = {'limpa':'\033[m',
         1:'\033[1;30m',
         2:'\033[1;31m',
         3:'\033[1;32m',
         4:'\033[1;33m',
         5:'\033[1;34m',
         6:'\033[1;35m',
         7:'\033[1;36m'}

import random

#importação da biblioteca numpy
import numpy as np

#linspace pega a passagem de 0 a 2pi e divide em 40 partes
angle = np.linspace(0,2 * np.pi, 40)

#imprimindo as partes
for repeticoes in range(0,40):
    print(f"{repeticoes + 1:2.0f}º elemento - {cores[random.randint(1,7)]}{angle[repeticoes]}"
            f"{cores['limpa']}")
