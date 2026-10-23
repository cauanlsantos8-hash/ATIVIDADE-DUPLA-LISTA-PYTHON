import os
os.system('cls')

print('-- Mundo Eletro - Módulo De Pagamento --')

try:
    valor_produto = float(input('Digite o valor do produto (R$): '))

    print('\nFormas de pagamento:')
    print('1 - À vista (10% de desconto)')
    print('2 - A prazo (até 6x sem juros)')
    forma_pagamento = int(input('Escolha a opção (1 ou 2): '))

    match forma_pagamento:
        case 1:
            desconto = valor_produto * 0.10
            valor_total = valor_produto - desconto

            print('\n-- Resumo Do Pagamento --')
            print(f'Valor do produto: R$ {valor_produto}')
            print(f'Forma de pagamento: À vista')
            print(f'Desconto aplicado (10%): R$ {desconto}')
            print(f'Valor Total a pagar: R$ {valor_total}')

        case 2:
            numero_parcelas = int(input('Digite a quantidade de parcelas (máximo 6): '))

            if 1 <= numero_parcelas <= 6:
                valor_total = valor_produto
                valor_parcela = valor_total / numero_parcelas

                print('\n-- Resumo Do Pagamento --')
                print(f'Valor do produto: R$ {valor_produto}')
                print(f'Valor do produto: R$ {valor_produto}')
                print('Forma de pagamento: A prazo')
                print(f'Quantidade de parceloas: {numero_parcelas}x')
                print(f'Valor de cada parcela: R$ {valor_parcela}')
                print(f'Valor Total a Pagar: R$ {valor_total}')
            else:
                print('\nErro: Número de parcelas Inválido. Permitido apenas de 1 a 6 parcelas.')

        case _:
            print('\nErro: Forma de pagamento inválida.')

except ValueError:
    print("\nErro: Por favor, informe apenas valores numéricos válidos.")