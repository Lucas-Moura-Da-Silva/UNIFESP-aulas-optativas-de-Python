#3) Escreva um script que leia a quantidade de dias,horas, minutos e segundos para o usuário.
# Calcule o total em segundos.

dias = int(input('Qunatos dias se passaram?'))
horas = int(input('Quantas horas se passaram?'))
minutos = int(input('Quantos minutos se passaram?'))
segundos = int(input('Quantos segundos se passaram?'))

#contagem de segundos totais:
segtotal = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos

print('-='*30)

print(f'No total foram contados {segtotal} segundos')