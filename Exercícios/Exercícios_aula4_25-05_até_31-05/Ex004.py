'''4) Faça um programa que leia o nome, RA e média final de
uma aluno. Armazene todas as informações num
dicionário. No final programa deve imprimir as
informações do dicionário e situação do aluno
(reprovado, exame ou aprovado). Utilize as regras da
UNIFESP para definir a situação do aluno.'''

#cores
cores = {'limpa':'\033[m',
         'branco':'\033[1;30m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'roxo':'\033[1;35m',
         'ciano':'\033[1;36m'}

#dicionario
aluno = dict()

#input's
nome = aluno['Nome'] = str(input('Qual o nome do aluno:')).title()
RA = aluno['RA'] = int(input(f"Qual o RA do {cores['vermelho']}{nome}{cores['limpa']}:"))
media_final = aluno['media final'] = float(input(f"Qual é a média final do {cores['vermelho']}"
                                                 f"{nome}{cores['limpa']}:"))

print(f"{cores['ciano']}¬{cores['limpa']}"*75)

#imprimindo informações
print(f"O estudante {cores['vermelho']}{aluno['Nome']}"
      f"{cores['limpa']}, com o número do RA {cores['azul']}{aluno['RA']}{cores['limpa']}, "
      f"tirou {cores['verde']}{aluno['media final']}{cores['limpa']} na média final.")

print(f"A situação do(a) {cores['vermelho']}{aluno['Nome']}{cores['limpa']} é de", end=' ')

if media_final >= 6:
    print(f"{cores['roxo']}Aprovado!{cores['limpa']}")
elif 6 > media_final >= 3:
    print(f"{cores['verde']}Exame!{cores['limpa']}")
else:
    print(f"{cores['amarelo']}Reprovado!{cores['limpa']}")