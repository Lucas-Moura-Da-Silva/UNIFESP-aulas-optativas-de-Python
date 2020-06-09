#1) Crie um script em Python que solicite o nome, altura e peso de uma pessoa e mostre a seguinte
# mensagem: “João tem 90 kilos e altura de 1.78 e portanto o IMC é de 28.4”.

nome = input('Qual é o seu nome?')
alt = float(input('Qual a sua altura em metros?'))
peso = float(input('Qual é o seu peso em Kg?'))

#Calculo do IMC
imc = peso / (alt)**2

print('-='*20)

print(f'{nome} tem {peso}Kg e altura de {alt}m e portanto o IMC é de {imc:.2f}.')
