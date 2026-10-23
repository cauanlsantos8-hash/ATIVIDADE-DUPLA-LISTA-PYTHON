import os
os.system('cls')

numeros = []
positivos = []

for i in range(1, 11):
    numero = int(input(f'Digite o {i}º número inteiro: '))
    numeros.append(numero)
    
    if numero > 0:
        positivos.append(numero)
        
print('\n-- Vetor de Números Positivos --')
if positivos:
    print(positivos)
else:
    print('Nenhum número positivo foi digitado.')
    
print(f'\nQuantidades de elementos copiados: {len(positivos)}')
