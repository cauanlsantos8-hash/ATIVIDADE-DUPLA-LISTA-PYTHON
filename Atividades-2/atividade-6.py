import os
os.system('cls')

print('-- Instituto Dados Já - RESUMO DE COLETA --')

soma = 0
pares = 0
impares = 0

for i in range(1, 6):
    while True:
        try:
            numero = int(input(f'Digite o {i}º número inteiro: '))
            soma += numero

            if numero % 2 == 0:
                pares += 1
            else: impares += 1
            break
        except ValueError:
            print('Entrada inválida! Digite apenas números inteiros.')

print('\n-- RESUMO DA COLETA --')
print(f'Quantidade de números pares: {pares}')
print(f'Quantidade de números impares: {impares}')
print(f'Soma de todos os números: {soma}')
