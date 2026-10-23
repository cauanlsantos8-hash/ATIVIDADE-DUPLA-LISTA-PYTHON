import os
os.system('cls')

print("=== COLÉGIO SABER - BOLETIM ESCOLAR ===")

soma = 0.0

for i in range(1, 4):
    while True:
        try:
            nota = float(input(f"Digite a {i}ª nota (0 a 10): "))
            if 0 <= nota <= 10:
                soma += nota
                break
            else:
                print("Nota inválida! A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Digite apenas números.")

media = soma / 3

if media >= 7.0:
    status = "APROVADO"
elif media >= 5.0:
    status = "RECUPERAÇÃO"
else:
    status = "REPROVADO"

print("\n=== RESULTADO FINAL ===")
print(f"Média do aluno: {media:.2f}")
print(f"Situação: {status}")
