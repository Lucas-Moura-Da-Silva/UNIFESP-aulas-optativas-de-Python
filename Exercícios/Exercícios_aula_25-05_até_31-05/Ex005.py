'''5) Crie um programa que leia nome, sexo, peso e altura de
várias pessoas. guarde os dados de cada pessoa num
dicionário individual e acrescente o IMC da pessoa.
Organize todos os dicionários em uma lista. No final
mostre
a. Quantas pessoas foram cadastradas
b. Qual é o peso médio das pessoas
c. Qual é a altura média das pessoas
d. Qual é IMC médio das pessoas'''

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
pessoa = dict()
#lista
dados_pessoais = list()

#input's
quantidade_de_pessoas = int(input('Quantas pessoas serão cadastradas?'))
print(f"{cores['ciano']}-={cores['limpa']}"*25)

for repetições in range(1, quantidade_de_pessoas+1):
    nome = pessoa['Nome'] = str(input(f"Nome da {repetições}º pessoa que irá se cadastrar:")).capitalize()
    sexo = pessoa['Sexo'] = str(input(f"Sexo do(a) {cores['azul']}{nome}{cores['limpa']}:"))
    peso = pessoa['Peso'] = float(input(f"Peso do(a) {cores['azul']}{nome}{cores['limpa']} em Kg:"))
    altura = pessoa['Altura'] = float(input(f"Altura do(a) {cores['azul']}{nome}{cores['limpa']} em metros(m):"))

    calc_imc = (peso) / (altura)**2

    IMC = pessoa['IMC'] = float(f"{calc_imc:.2f}")

    dados_pessoais.append(pessoa.copy())
    print(f"{cores['ciano']}-={cores['limpa']}"*25)

#cada pessoa cadastrada
for repetições in dados_pessoais:
    for indice, valor in repetições.items():
        print(f"{cores['amarelo']}{indice}{cores['limpa']}:{cores['verde']}{valor}{cores['limpa']}")
    print(f"{cores['ciano']}-{cores['limpa']}"*50)


#a. Quantas pessoas foram cadastradas
numero_de_cadastros = len(dados_pessoais)
print(f"Foram cadastrados {cores['vermelho']}{numero_de_cadastros} pessoa(s){cores['limpa']}.")

print(f"{cores['ciano']}={cores['limpa']}"*50)

#b. Qual é o peso médio das pessoas
soma_peso = 0
for repetições in dados_pessoais:
    soma_peso += repetições['Peso']

media_peso = soma_peso / numero_de_cadastros
print(f"A média dos pesos das pessoas foi de {cores['roxo']}{media_peso:.2f}Kg{cores['limpa']}.")
print(f"{cores['ciano']}={cores['limpa']}"*50)

#c. Qual é a altura média das pessoas
soma_altura = 0
for repetições in dados_pessoais:
    soma_altura += repetições['Altura']

media_altura = soma_altura / numero_de_cadastros
print(f"A média das alturas das pessoas doi de {cores['roxo']}{media_altura:.2f}m{cores['limpa']}.")
print(f"{cores['ciano']}={cores['limpa']}"*50)

#d. Qual é IMC médio das pessoas
soma_IMC = 0
for repetições in dados_pessoais:
    soma_IMC += repetições['IMC']

media_IMC = soma_IMC / numero_de_cadastros
print(f"A média dos IMC's foi de {cores['roxo']}{media_IMC:.2f}{cores['limpa']}.")
