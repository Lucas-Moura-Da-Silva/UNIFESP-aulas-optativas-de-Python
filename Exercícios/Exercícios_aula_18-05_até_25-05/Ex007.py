'''7) Escreva um script que exibe a seguinte tábua de
multiplicação na tela:
1
2 4
3 6 9
4 8 12 16
5 10 15 20 25'''

#cores
cores = {'limpa':'\033[m',
         'branco':'\033[1;30m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'roxo':'\033[1;35m',
         'ciano':'\033[1;36m'}

quantos_mutiplicar = int(input('Até quantos numeros você quer multiplicar?'))

#repetição FOR
for repeticao in range(1, quantos_mutiplicar + 1):

    #condição
    if repeticao % 2 == 0:
        print(end=f"{cores['azul']}")
    else:
        print(end=f"{cores['roxo']}")

    #repetição
    for c in range(1, repeticao+1):
        multiplicacao = repeticao * c
        print(f"{multiplicacao}", end=' ')

    print( end='\n')