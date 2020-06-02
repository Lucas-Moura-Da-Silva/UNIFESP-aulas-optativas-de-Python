'''1) Crie um vetor com 40 elementos igualmente espaçados entre
0 e 2π.'''

'''Os Exercícios efeito daqui por diante, usaremos a biblioteca Numpy e para uma melhor 
visualização das tabelas/matrizes é recomendado usar a ferramenta "spider", "jupyter", 
"colab" ou outra de sua preferencia.'''

#importação da biblioteca numpy
import numpy as np

#linspace pega a passagem de 0 a 2pi e divide em 40 partes
angle = np.linspace(0,2 * np.pi, 40)

#imprimindo as partes
print(angle)
