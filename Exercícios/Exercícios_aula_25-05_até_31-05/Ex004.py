'''4) Faça um programa que leia o nome, RA e média final de
uma aluno. Armazene todas as informações num
dicionário. No final programa deve imprimir as
informações do dicionário e situação do aluno
(reprovado, exame ou aprovado). Utilize as regras da
UNIFESP para definir a situação do aluno.'''

#dicionario
aluno = dict()

#input's
nome = aluno['Nome'] = str(input('Qual o nome do aluno:')).capitalize()
RA = aluno['RA'] = int(input(f'Qual o RA do {nome}:'))
media_final = aluno['media final'] = float(input(f'Qual é a média final do {nome}:'))

#imprimindo informações
print(f"O estudante {aluno['Nome']}, com o número do RA {aluno['RA']}, tirou "
      f"{aluno['media final']} na média final.")
print("Sua situação é de", end=' ')

if media_final >= 6:
    print('Aprovado!')
elif 6 > media_final > 3:
    print('Exame!')
else:
    print('Reprovdo!')