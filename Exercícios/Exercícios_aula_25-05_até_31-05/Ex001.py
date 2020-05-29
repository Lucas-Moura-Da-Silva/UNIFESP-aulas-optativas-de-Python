'''1) Faça um programa que leia o nome e nota da P1 de vários
alunos guardando tudo em uma lista e no final mostre:
a. Quantas alunos foram cadastradas
b. O nome do aluno com maior nota
c. O nome da pessoa menor nota
d. O nota média da sala.'''

'''problemas:
Se as notas forem iguais, a ultima não será contabilizada.'''

#cores
cores = {'limpa':'\033[m',
         'branco':'\033[1;30m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'roxo':'\033[1;35m',
         'ciano':'\033[1;36m'}

#lista dos alunos
alunos = list()

#dicionario do aluno
aluno = dict()

#estrutura de repetição-WHILE
while True:
    aluno['nome'] = str(input('Nome do aluno:')).title()
    aluno['nota da P1'] = float(input(f"Nota do {cores['vermelho']}{aluno['nome']}{cores['limpa']}:"))
    alunos.append(aluno.copy())

    print(f"{cores['ciano']}-&{cores['limpa']}"*30)
    cont = str(input('Você quer continuar anotando as notas e os nomes dos alunos?')).upper()
    if 'N' in cont:
        break

print(f"{cores['ciano']}-={cores['limpa']}"*25)

#a. Quantas alunos foram cadastradas
alunosNumero = len(alunos) #número de alunos

print(f"Foram cadastrador {cores['roxo']}{alunosNumero}{cores['limpa']} aluno(s).")

print(f"{cores['ciano']}-={cores['limpa']}"*25)

#b. O nome do aluno com maior nota
maior = alunos[0]['nota da P1']
alunoMaior = alunos[0]['nome']
#repetição em alunos
for aluno in alunos:
    if (aluno['nota da P1']) > maior:
        maior = aluno['nota da P1']
        alunoMaior = aluno['nome']

print(f"O aluno com maior nota foi {cores['azul']}{alunoMaior}{cores['limpa']}.")

print(f"{cores['ciano']}-={cores['limpa']}"*25)

#c. O nome da pessoa menor nota
menor = alunos[0]['nota da P1']
alunoMenor = alunos[0]['nome']
#repetição em alunos
for aluno in alunos:
    if (aluno['nota da P1']) < menor:
        menor = aluno['nota da P1']
        alunoMenor = aluno['nome']

print(f"O aluno com menor nota foi {cores['amarelo']}{alunoMenor}{cores['limpa']}.")

print(f"{cores['ciano']}-={cores['limpa']}"*25)

#d. O nota média da sala.
soma = 0
#repetição em alunos
for aluno in alunos:
    soma += aluno['nota da P1']
mediaSala = soma/alunosNumero

print(f"A média da sala é {cores['verde']}{mediaSala:.2f}{cores['limpa']}.")
