import os
os.system('cls')

vetor_A = []
vetor_B = []
vetor_C = []

print('-- PREENCHENDO VETOR A --')
for i in range(1, 6):
    numero = int(input(f'Digite o {i}º número de A: '))
    vetor_A.append(numero)
    
print('\n-- PREENCHENDO O VETOR B --')
for i in range(1, 6):
    numero = int(input(f'Digite o {i}º número de B: '))
    vetor_B.append(numero)
    
for i in range(5):
    vetor_C.append(vetor_A[i] + vetor_B[i])

print('\n-- VETOR A --')
print(vetor_A)

print('\n-- VETOR B --')
print(vetor_B)

print('\n-- VETOR C --')
print(vetor_C)