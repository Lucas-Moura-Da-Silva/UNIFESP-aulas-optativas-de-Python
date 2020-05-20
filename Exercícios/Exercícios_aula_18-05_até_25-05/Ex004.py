'''4) Desenvolva um programa que solicite o primeiro número
de uma PA e sua razão. O programa deve imprimir os 10
primeiros termos.'''

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
primeiro_numero = int(input(f"Qual é o {cores['vermelho']}número{cores['limpa']} de você quer fazer "
                            f"uma PA?"))
razão = int(input(f"Qual é a {cores['vermelho']}razão{cores['limpa']} da PA?"))

#repetição FOR
for repetição in range(0,10):
    print(f"{primeiro_numero} ->", end=' ')

    #logica da PA
    proximo_numero = primeiro_numero + razão
    primeiro_numero = proximo_numero

print("FIM")