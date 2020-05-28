'''6) Faça um programa que calcule a soma os números
impares e múltiplos de 3 que se encontram no intervalo
de 1 até 500'''

#cores
cores = {'limpa':'\033[m',
         'branco':'\033[1;30m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'roxo':'\033[1;35m',
         'ciano':'\033[1;36m'}

soma_impares_mult3 = conjunto_de_15 = 0

#repetição FOR
for numeros in range(1, 501):

    #Condição IF
    if numeros%2 != 0 and numeros%3 == 0:
        soma_impares_mult3 += numeros
        print(f"{numeros} ->", end=' ')

        conjunto_de_15 += 1

        #quebra de linha
        if conjunto_de_15%15 == 0:
            print(end='\n')

print('FIM')
print('-='*30)
print(f"A soma dos números impares e dos multiplos de 3 é igual a {cores['ciano']}"
      f"{soma_impares_mult3}{cores['limpa']}.")