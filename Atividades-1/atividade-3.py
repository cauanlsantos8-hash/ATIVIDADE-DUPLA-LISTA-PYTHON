import os
os.system('cls')

numeros = []
soma_total = 0
quantidade_maiores_10 = 0

for i in range(1, 11):
    numero = int(input(f'Digite o {i}º número inteiro: '))
    numeros.append(numero)

    soma_total += numero
    if numero > 10:
        quantidade_maiores_10 += 1

print('\n -- Resultados --')
print(f'Soma de todos os elementos: {soma_total}')
print(f'Quantidade de números maiores que 10: {quantidade_maiores_10}')