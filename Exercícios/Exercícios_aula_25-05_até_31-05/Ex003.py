'''3) Crie um programa que crie uma matriz de dimensão 3x3
e preencha com valores lidos pelo teclado. No final,
mostre a matriz na tela com a formatação correta.'''

#lista com a matriz
matriz = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

#colocando os números na lista
for linha in range (0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = float(input(f'Digite um numero na posição [{linha}, {coluna}]:'))

print('-='*15)
print('MATRIZ')
print('[lin\col] | [  1  ] [  2  ] [  3  ]')
print('-'*9, '+', '-'*24) #demarcação entre as coordenadas

#immprimiindo a matriz
for linha in range(0, 3):
    print(f'[{linha+1:^7.0f}] |', end=' ')
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]:^5.0f}]", end=' ')
    print()