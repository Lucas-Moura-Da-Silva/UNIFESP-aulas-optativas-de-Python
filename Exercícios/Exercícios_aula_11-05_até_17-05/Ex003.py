'''3) No sistema SI, a vazão de um fluido é medida em metros
cúbicos por segundo (m³ /s). A medida do sistema inglês
de vazão, o pé cúbico por segundo (ft³/s) é equivalente
a 0.028 m³/s. Escreva uma rotina que pede ao usuário pela
vazão em metros cúbicos por segundo e converte essa vazão
para a unidade inglesa, exibindo o seguinte ao usuário:

"Um fluxo de 15.2000 m³/s é equivalente a 542.8571 ft³/s."'''

#cores
cores = {'limpa':'\033[m',
         'branco':'\033[1;30m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'roxo':'\033[1;35m',
         'ciano':'\033[1;36m'}

#input's da quetão
fluxo_SI = float(input('Qual o valor do fluxo em m³/s?'))

#transformação de m³/s para ft³/s
fluxo_Ig = fluxo_SI/0.028

print('-='*30)
#retorno com a converção
print(f"Um fluxo de {cores['verde']}{fluxo_SI:.4f}{cores['limpa']} m³/s é equivalente a"
      f" {cores['ciano']}{fluxo_Ig:.4f}{cores['limpa']} ft³/s.")
