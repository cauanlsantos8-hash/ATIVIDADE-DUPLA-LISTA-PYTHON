import os
os.system('cls')

idades = []
quantidade_maiores = 0

for i in range(1, 6):
    while True:
        try:
            idade = int(input(f"Digite a idade da {i}ª pessoa (0 a 120): "))
            if 0 <= idade <= 120:
                idades.append(idade)
                if idade >= 18:
                    quantidade_maiores += 1
                break
            else:
                print("Idade inválida! Digite um valor entre 0 e 120.")
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")

maior = max(idades)
menor = min(idades)

print("\n=== RESULTADOS ===")
print(f"Maior idade: {maior} anos")
print(f"Menor idade: {menor} anos")
print(f"Quantidade de maiores de idade: {quantidade_maiores}")