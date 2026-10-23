import os
os.system('cls')

print('-- Ficanceira Confia - Pré-Análise De Crédito --')

renda = float(input('Digite a renda mensal do cliente (R$): '))
valor_emprestimo = float(input('Digite o valor do empréstimo solicitado (R$): '))
numero_prestacoes = int(input('Digite o número de prestações: '))

prestacao = valor_emprestimo / numero_prestacoes
limite_emprestimo = renda * 10
limite_prestacao = renda * 0.30

print('\n-- Resultado Da Análise --')
print(f'Valor de cada prestação: R$ {prestacao}')

if valor_emprestimo <= limite_emprestimo and prestacao <= limite_prestacao:
    print('Status do crédito: APROVADO')
else:
    print('Status do crédito: NEGADO')
    if valor_emprestimo > limite_emprestimo:
        print(f'- Motivo: O empréstimo ultrapassa 10x a renda (limite R$ {limite_emprestimo})')
    if prestacao > limite_prestacao:
        print(f'- Motivo: A prestação ultrapassa 30% da renda (Limite: R$ {limite_prestacao})')