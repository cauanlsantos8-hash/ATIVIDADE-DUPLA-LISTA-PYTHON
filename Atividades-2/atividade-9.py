import os
os.system('cls')


total_pagar = 0.0
quantidade_pratos = 0
continuar = "S"

while continuar.upper() == "S":
    
    print("=== RESTAURANTE SABOR DA TERRA - CARDÁPIO ===")
    print("1 - Prato Feito .............. R$ 20.00")
    print("2 - Feijoada ................. R$ 30.00")
    print("3 - Filé de Frango ........... R$ 15.00")
    print("4 - Salada Fit ............... R$ 8.00")
    print("5 - Suco da Fruta ............. R$ 7.00")
    print("-----------------------------------------")
    
    try:
        codigo = int(input("Digite o código do prato desejado: "))

        match codigo:
            case 1:
                total_pagar += 20.00
                quantidade_pratos += 1
                print("\n>> Prato Feito adicionado!")
            case 2:
                total_pagar += 30.00
                quantidade_pratos += 1
                print("\n>> Feijoada adicionada!")
            case 3:
                total_pagar += 15.00
                quantidade_pratos += 1
                print("\n>> Filé de Frango adicionado!")
            case 4:
                total_pagar += 8.00
                quantidade_pratos += 1
                print("\n>> Salada Fit adicionada!")
            case 5:
                total_pagar += 7.00
                quantidade_pratos += 1
                print("\n>> Suco da Fruta adicionado!")
            case _:
                print("\n>> Código inválido! Nenhum item adicionado.")
    except ValueError:
        print("\n>> Entrada inválida! Por favor, digite apenas um número inteiro.")

    continuar = input("\nDeseja outro prato? (S/N): ").strip()

print("\n=== RESUMO DO PEDIDO ===")
print(f"Quantidade total de itens: {quantidade_pratos}")
print(f"Total a pagar: R$ {total_pagar}")