import os
os.system('cls')

print('-- Calculadora CrediFácil --')
numero_1 = float(input('Digite o primeiro número: '))
numero_2 = float(input('Digite o segundo número: '))
operador = input("Digite o operador (+, -, * ou /): ").strip()

valido = True
resultado = 0.0

match operador:
    case "+":
        resultado = numero_1 + numero_2
    case "-":
        resultado = numero_1 - numero_2
    case "*":
        resultado = numero_1 * numero_2
    case "/":
        if numero_2 != 0:
            resultado = numero_1 / numero_2
        else:
            print('\nErro: Não é possível dividir por zero!')
            valido = False
    case _:
        print('\nErro: Operador Inválido!')
        valido = False
if valido:
    print('\n-- Resultado Da Operação --')
    print(f'Número 1: {numero_1}')
    print(f'Operador: {operador}')
    print(f'Número 2: {numero_2}')
    print(f'Resultado: {resultado}')
    