'''4) Faça um programa que leia o nome completo de uma
pessoa e imprime somente o primeiro e o último nome
separadamente.'''

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
nome_completo = input('Qual é o seu nome completo?').split()

#primeiro nome
primeiro_nome = nome_completo[0]

#ultimo nome
ultimo_nome = nome_completo[len(nome_completo) - 1]

#retorno com o primeiro e ultimo nome
print(f"O seu primeiro nome é {cores['vermelho']} {primeiro_nome} {cores['limpa']} e o seu " \
    f"ultimo nome é {cores['amarelo']}{ultimo_nome}{cores['limpa']}.")