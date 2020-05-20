'''2) Escreva um programa que leia 3 números e que imprima
o maior e o menor'''

#cores
cores = {'limpa':'\033[m',
         'branco':'\033[1;30m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'roxo':'\033[1;35m',
         'ciano':'\033[1;36m'}

#input's da questão
numero_1 = float(input('Digite um número:'))
numero_2 = float(input('Digite outro número:'))
numero_3 = float(input('Digite outro número novamente:'))

print('-='*17)

#Condições IF-ELIF-ELSE
if numero_1 > numero_2 > numero_3:
    print(f"O maior valor é o {cores['roxo']}{numero_1}{cores['limpa']}.")
    print(f"O menor valor é o {cores['ciano']}{numero_3}{cores['limpa']}")

elif numero_1 > numero_3 > numero_2:
    print(f"O maior valor é o {cores['roxo']}{numero_1}{cores['limpa']}.")
    print(f"O menor valor é o {cores['ciano']}{numero_2}{cores['limpa']}")

elif numero_2 > numero_1 > numero_3:
    print(f"O maior valor é o {cores['roxo']}{numero_2}{cores['limpa']}.")
    print(f"O menor valor é o {cores['ciano']}{numero_3}{cores['limpa']}")

elif numero_2> numero_3 > numero_1:
    print(f"O maior valor é o {cores['roxo']}{numero_2}{cores['limpa']}.")
    print(f"O menor valor é o {cores['ciano']}{numero_1}{cores['limpa']}")

elif numero_3 > numero_1 > numero_2:
    print(f"O maior valor é o {cores['roxo']}{numero_3}{cores['limpa']}.")
    print(f"O menor valor é o {cores['ciano']}{numero_2}{cores['limpa']}")

else:
    print(f"O maior valor é o {cores['roxo']}{numero_3}{cores['limpa']}.")
    print(f"O menor valor é o {cores['ciano']}{numero_1}{cores['limpa']}")

