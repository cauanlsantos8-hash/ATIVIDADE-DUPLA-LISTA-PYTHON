import os
os.system('cls')

numeros = []


for i in range(1, 6):
    numero = int(input(f"Digite o {i}º número inteiro: "))
    numeros.append(numero)


print("\n-- Ordem Direta --")
for i, numero in enumerate(numeros, start=1):
    print(f"Posição {i}: {numero}")

print("\n-- Ordem Inversa --")
for i in range(len(numeros) - 1, -1, -1):
    print(f"Posição {i + 1}: {numeros[i]}")