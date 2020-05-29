'''2) Crie um programa onde o usuário possa digitar 10 valores
numéricos e cadastre-os em 2 listas separadas. Sendo a
primeira contendo números primos e segunda não
primos.'''

#cores
cores = {'limpa':'\033[m',
         'branco':'\033[1;30m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'roxo':'\033[1;35m',
         'ciano':'\033[1;36m'}

#listas
primos = list()
naoprimos = list()

#input's
for repetição in range(1, 11):
    numero = int(input(f"Digite o {cores['amarelo']}{repetição}º{cores['limpa']} número:"))#input's
    primo = True

    if numero >= 2:
        for anteriores in range(2, numero):
            if numero % anteriores == 0:
                naoprimos.append(numero)
                primo = False
                break

        if primo == True:
            primos.append(numero)

    else:
        naoprimos.append(numero)

print(f"{cores['branco']}-¨{cores['limpa']}"*40)

#imprimindo os números primos
print(f"Dos números que você digitou, os {cores['vermelho']}numeros primos{cores['limpa']} são"
      f"{cores['azul']} ", end='')

for num_primos in primos:
    print(num_primos, end=' ')
print(f"{cores['limpa']}.")

#imprimir os números não primos
print(f"Dos números que você digitou, os {cores['verde']}numeros não primos{cores['limpa']} são "
      f"{cores['roxo']}", end='')

for num_n_primos in naoprimos:
    print(num_n_primos, end=' ')
print(f"{cores['limpa']}.")
