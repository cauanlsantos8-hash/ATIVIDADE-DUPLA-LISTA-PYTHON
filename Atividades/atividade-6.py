import os
os.system('cls')

vetor_A = []
vetor_B = []
vetor_C = []

print('-- Preenchendo o Vetor A --')
for i in range(1, 6):
    numero = int(input(f'Digite o {i}º número de A: '))
    vetor_A.append(numero)
    
print('\n-- Preenchendo o Vetor B --')
for i in range(1, 6):
    numero = int(input(f'Digite o {i}º número de B: '))
    vetor_B.append(numero)
    
for i in range(5):
    vetor_C.append(vetor_A[i] + vetor_B[i])

print('\n-- Vetor A --')
print(vetor_A)

print('\n-- Vetor B --')
print(vetor_B)

print('\n-- Vetor C --')
print(vetor_C)