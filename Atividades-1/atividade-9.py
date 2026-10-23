import os
os.system('cls')

vetor_original = []

for i  in range(1, 7):
    numero = int(input(f'Digite o {i}º número inteiro: '))
    vetor_original.append(numero)
    
vetor_modificado = [0 if num % 2 == 0 else 1 for num in vetor_original]

print('\n-- Vetor Antes --')
print(vetor_original)

print('\n-- Vetor Depois --')
print(vetor_modificado)