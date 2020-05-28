'''1) Faça um programa que leia o nome e nota da P1 de vários
alunos guardando tudo em uma lista e no final mostre:
a. Quantas alunos foram cadastradas
b. O nome do aluno com maior nota
c. O nome da pessoa menor nota
d. O nota média da sala.'''

'''problemas:
Se as notas forem iguais, a ultima não será contabilizada.'''

#lista dos alunos
alunos = list()

#dicionario do aluno
aluno = dict()

#estrutura de repetição-WHILE
while True:
    aluno['nome'] = str(input('Nome do aluno:'))
    aluno['nota da P1'] = float(input(f"Nota do {aluno['nome']}:"))
    alunos.append(aluno.copy())

    cont = str(input('Você quer continuar anotando as notas e os nomes dos alunos?')).upper()
    if 'N' in cont:
        break

print('-='*25)

#a. Quantas alunos foram cadastradas
alunosNumero = len(alunos) #número de alunos

print(f"Foram cadastrador {alunosNumero} aluno(s).")

print('-='*25)

#b. O nome do aluno com maior nota
maior = 0
#repetição em alunos
for aluno in alunos:
    if (aluno['nota da P1']) > maior:
        maior = aluno['nota da P1']
        alunoMaior = aluno['nome']

print(f"O aluno com maior nota foi {alunoMaior}.")

print('-='*25)

#c. O nome da pessoa menor nota
menor = maior
#repetição em alunos
for aluno in alunos:
    if (aluno['nota da P1']) < menor:
        menor = aluno['nota da P1']
        alunoMenor = aluno['nome']

print(f"O aluno com maior nota foi {alunoMenor}.")

print('-='*25)

#d. O nota média da sala.
soma = 0
#repetição em alunos
for aluno in alunos:
    soma += aluno['nota da P1']
mediaSala = soma/alunosNumero

print(f"A média da sala é {mediaSala:.2f}.")
