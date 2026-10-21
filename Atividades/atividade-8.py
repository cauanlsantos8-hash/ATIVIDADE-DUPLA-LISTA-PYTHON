import os
os.system('cls')

nomes = []
salarios = []

for i in range(1, 6):
    nome = input(f'Digite o nome do {i}º funcionário: ')
    salario = float(input(f'Digite o salário de {nome}: R$ '))
    nomes.append(nome)
    salarios.append(salario)
    
maior_salario = max(salarios)
indice_maior = salarios.index(maior_salario)
nome_maior = nomes[indice_maior]

quantidade_acima_2000 = sum(1 for s in salarios if s > 2000.00)

print('\n-- Resultados --')
print(f'Funcionários com maior salário: {nome_maior} (R$ {maior_salario})')
print(f'Quantidade de funcinários que ganham acima de 2.000,00: {quantidade_acima_2000}')
