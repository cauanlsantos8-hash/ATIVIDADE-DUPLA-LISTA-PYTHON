import os
os.system('cls')
import time


print('-- Escola Aprender+ - GERADOR DE TABUADA --')

try:
    numero = int(input('Digite um número inteiro para ver a sua tabuada: '))

    print(f'\n-- Tabuada Do {numero} --')

    for i in range(1, 11):
        resultado = numero * i
        print(f'{numero} x {i} = {resultado}')
        time.sleep(1)

except ValueError:
    print('\nErro: Por favor, informe um número inteiro válido.')