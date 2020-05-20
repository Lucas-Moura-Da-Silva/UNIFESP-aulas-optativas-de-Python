'''5) Escreva um programa que pergunte o deposito inicial e a
taxa de Juros de uma poupança. Exiba os valores mês a
mês para os 24 primeiros meses. No final deve imprimir o
total de ganho com juros no período.'''

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
capital_inicial = float(input('Qual é a continha do deposito inicial?'))
juros_porcentagem = float(input('Qual é a taxa de juros da poupança por mês em porcentagem?'))

juros_decimais = juros_porcentagem / 100

#repetição FOR
for meses in range(1,25):
    #formula do montante
    Montante = capital_inicial * (1 + juros_decimais)**(meses)

    print('-'*50)
    print(f"Você tem uma valor total de {cores['roxo']}R${Montante:.2f}{cores['limpa']} no "
          f"{cores['amarelo']}{meses}º mês{cores['limpa']}.")

#formula do juros
Juros_compostos = Montante - capital_inicial

print('-='*30)
print(f"Seu ganho total com juros nesse período foi de {cores['verde']}R${Juros_compostos:.2f}"
      f"{cores['limpa']}.")