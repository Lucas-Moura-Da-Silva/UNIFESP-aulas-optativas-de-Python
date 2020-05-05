#5) Escreva um script que pergunte a quantidade de Km percorridos por um carro alugado pelo
# usuário e a quantidade de dias pelo qual o carro foi alugado. Calcule o preço a pagar sabendo
# que o carro custa 60 reais por dia e 15 centavos por Km rodado.

dia = int(input('Quantos dias você ficou com o carro?'))
km = float(input('Quantos quilometros você rodou com o carro nesses dias?'))

#calculo dos custos
custo = (dia * 60) + (km * 0.15)

print('-='*30)

#output do custo
print(f'O custo dos {dia} dias com o carro mais os {km:.2f}Km corridos, foi R${custo:.2f}.')