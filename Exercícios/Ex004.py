#4) Faça um script que calcule o aumento de salário. Ele deve solicitar o valor do salário e a
# porcentagem de aumento. Exiba o valor do aumento e do novo salário.

salario = float(input('Qual é o seu salário atual?'))
porc = float(input('Qual é o aumento do salário em porcentagem?'))

#aumento do salário
aumentoSalario = salario * (porc/100)
salarioAtual = salario + aumentoSalario

print('-='*25)

#output da frase
print(f'O salario antigo de R${salario:.2f} com o aumento de {porc:.2f}%, ficará R$'
      f'{salarioAtual:.2f}. Seu aumento foi de R${aumentoSalario:.2f} ')