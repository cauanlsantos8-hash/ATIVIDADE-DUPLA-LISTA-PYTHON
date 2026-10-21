import os
os.system('cls')

numeros = []

for i in range(1, 9):
    numero = int(input(f'Digite o {i}º número inteiro: '))
    numeros.append(numero)
    
pesquisa = int(input('\nDigite um número para pesquisar: '))

posicoes = [i + 1 for i, num in enumerate(numeros) if num == pesquisa]

if posicoes:
    for pos in posicoes:
        print(f'Número encontrado na posição: {pos}')
    else:
        print('Número não encontrado.')