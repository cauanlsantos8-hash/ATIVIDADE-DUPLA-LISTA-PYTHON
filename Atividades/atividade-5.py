import os
os.system('cls')

notas = []

for i in range(1, 6):
    nota = float(input(f'Digite a {i}º nota: '))
    notas.append(nota)

soma = sum(notas)
media = soma/len(notas)

quantidade_acima = sum(1 for nota in notas if nota > media)

print('\n-- NOTAS INFORMADAS --')
for i, nota in enumerate(notas, start=1):
    print(f'Nota {i}: {nota}')

print(f'\nMédia da turma: {media}')
print(f'Quantidade de notas acima da média: {quantidade_acima}')