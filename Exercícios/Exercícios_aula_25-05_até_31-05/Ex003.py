'''3) Crie um programa que crie uma matriz de dimensão 3x3
e preencha com valores lidos pelo teclado. No final,
mostre a matriz na tela com a formatação correta.'''

#cores
cores = {'limpa':'\033[m',
         'branco':'\033[1;30m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'roxo':'\033[1;35m',
         'ciano':'\033[1;36m'}

#lista com a matriz
matriz = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

print(f"{cores['branco']}-={cores['limpa']}"*18)

#colocando os números na lista
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = float(input(f'Digite um numero na posição [{linha}, {coluna}]:'))

print(f"{cores['branco']}-={cores['limpa']}"*18, '\n')

print(f"{cores['vermelho']}---------------MATRIZ---------------{cores['limpa']}\n")

#linha 1
print(f"{cores['verde']}[lin\col]{cores['limpa']} {cores['roxo']}|{cores['limpa']} "
      f"{cores['amarelo']}[  1  ] [  2  ] [  3  ]{cores['limpa']}")

#linha 2
print(f"{cores['roxo']}-{cores['limpa']}"*9, f"{cores['roxo']}+{cores['limpa']}",
      f"{cores['roxo']}-{cores['limpa']}"*24) #demarcação entre as coordenadas

#restantes das linhas
#immprimiindo a matriz
for linha in range(0, 3):
    print(f"{cores['amarelo']}[{linha+1:^7.0f}]{cores['limpa']} {cores['roxo']}|{cores['limpa']}",
          end=' ')
    for coluna in range(0, 3):
        print(f"{cores['ciano']}[{matriz[linha][coluna]:^5.0f}]{cores['limpa']}", end=' ')
    print()