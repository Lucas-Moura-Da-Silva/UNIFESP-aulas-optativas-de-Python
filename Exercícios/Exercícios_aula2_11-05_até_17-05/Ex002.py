'''2) Crie uma rotina que solicite uma frase ao usuário e retorne
o número de caracteres na frase e o número de espaços.'''

#cores
cores = {'limpa':'\033[m',
         'branco':'\033[1;30m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'roxo':'\033[1;35m',
         'ciano':'\033[1;36m'}

#input da questão
frase = input('Digite uma frase').strip()

#número de caracteres
num_carac = len(frase)

#número de espaços
num_esp = frase.count(' ')

print('-='*30)
#retorno com o número da questão e o numero de espaços
print(f"O número de caracteres é {cores['azul']}{num_carac}{cores['limpa']} e o número de espaços é"
      f" {cores['branco']}{num_esp}{cores['limpa']}.")