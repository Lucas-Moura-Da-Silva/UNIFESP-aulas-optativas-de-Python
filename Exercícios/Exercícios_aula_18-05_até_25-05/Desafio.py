'''Faça um código em python que solicite ao usuário um numero
inteiro e diga se ele é um numero primo'''

possivel_nprimo = int(input('Digite um número inteiro para ver se ele é primo ou não:'))
possibilidade = 0

for c in range(1, possivel_nprimo+1):
    if possivel_nprimo % c == 0:
        possibilidade += 1

if possibilidade == 2:
    print(f"O número {possivel_nprimo} é um número primo")
else:
    print(f"O número {possivel_nprimo} não é um número primo.")
