'''2) Crie um programa onde o usuário possa digitar 10 valores
numéricos e cadastre-os em 2 listas separadas. Sendo a
primeira contendo números primos e segunda não
primos.'''

#listas
primos = list()
naoprimos = list()

for repetição in range(1, 11):
    numero = int(input(f'Digite o {repetição}º número:'))#input's
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

#imprimindo resusltados
print(f"Dos números que você digitou, os numeros primos são {primos}.".replace('[','').replace(
    ']', '')) #trocaresmos o '[' e os ']' por um espaço vazio

print(f"Dos números que você digitou, os numeros não primos são {naoprimos}.".replace('[',
    '').replace(']', ''))#trocaresmos o '[' e os ']' por um espaço vazio
