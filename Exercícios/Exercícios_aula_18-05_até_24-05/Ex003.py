'''3) Escreva um programa que pergunte a distância que um
passageiro deseja percorrer em km. Calcule o preço da
passagem cobrando 0,50 por Km rodado para viagens até
200Km e 0,45 para viagens mais longas.'''

#cores
cores = {'limpa':'\033[m',
         'branco':'\033[1;30m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'roxo':'\033[1;35m',
         'ciano':'\033[1;36m'}

#input da questão
distacian_percorrida = float(input('Qual é a distância que você quer percorrer?'))

#Condições IF-ELSE
if distacian_percorrida <= 200:
    gasto_abaixo_de_200 = distacian_percorrida * 0.5

    print(f"O preço da passagem de {cores['vermelho']}{distacian_percorrida}Km{cores['limpa']} é de "
          f"{cores['azul']}R${gasto_abaixo_de_200:.2f}{cores['limpa']}.")

else:
    gasto_acima_de_200 = distacian_percorrida * 0.45

    print(f"O preço da passagem de {cores['roxo']}{distacian_percorrida}Km{cores['limpa']} é de "
          f"{cores['ciano']}R${gasto_acima_de_200:.2f}{cores['limpa']}.")