'''1) Escreva um programa que pergunte a velocidade do carro
de um usuário. Caso ultrapasse 80 km/h, exiba uma
mensagem dizendo que o usuário foi multado. Nesse
caso, exiba o valor da multa, cobrando 5 reais por Km
acima de 80Km/h.'''

#cores
cores = {'limpa':'\033[m',
         'branco':'\033[1;30m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'roxo':'\033[1;35m',
         'ciano':'\033[1;36m'}

velocidade_Usuario = float(input('Qual é a sua velocidade em Km/h?'))

#Condições IF-ELSE
if velocidade_Usuario > 80:
    print(f"Você está {cores['amarelo']}acima{cores['limpa']} da velocidade permitida!!")

    velocidade_acima_do_permitido = velocidade_Usuario - 80
    multa = velocidade_acima_do_permitido * 5

    #retorno com velocidade abaixo de 80Km/h
    print(f"Você será multado em um valor de {cores['vermelho']}R${multa:.2f}{cores['limpa']}.")

else:
    #retorno com velocidade abaixo de 80Km/h
    print(f"Você está {cores['azul']}abaixo{cores['limpa']} do limite de velocidade.")

print('-='*25)
print('Tenha um bom dia!!!')