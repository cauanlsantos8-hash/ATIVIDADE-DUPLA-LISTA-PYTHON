import os
os.system('cls')

print('-- Atacarejo Bom Preço - Caixa --')

produto = input('Nome do produto: ')
quantidade = int(input('Quantidade comprada: '))
preco_unitario = float(input('Preço unitário (R$): '))

total_bruto = quantidade * preco_unitario

if quantidade <=5:
    percentual_desconto = 0.02
elif quantidade <= 10:
    percentual_desconto = 0.03
else:
    percentual_desconto = 0.05

valor_desconto = total_bruto * percentual_desconto
total_pagar = total_bruto - valor_desconto

print('\n-- Resumo Da Compra --')
print(f'Produto: {produto}')
print(f'Quantidade: {quantidade}')
print(f'Preço Unitário: R$ {preco_unitario}')
print(f'Total Bruto: R$ {total_bruto}')
print(f'Desconto ({int(percentual_desconto * 100)}%): R$ {valor_desconto}')
print(f'Total a Pagar: R$ {total_pagar}')