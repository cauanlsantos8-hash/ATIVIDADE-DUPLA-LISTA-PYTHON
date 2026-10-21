import os
os.system('cls')

temperaturas = []

for i in range(1, 8):
    temperatura = float(input(f"Digite a temperatura do {i}º dia (°C): "))
    temperaturas.append(temperatura)

soma = sum(temperaturas)
media = soma / len(temperaturas)
maior = max(temperaturas)
menor = min(temperaturas)

print("\n-- Temperaturas Registradas --")
for i, temperatura in enumerate(temperaturas, start=1):
    print(f"Dia {i}: {temperatura} °C")

print("\n-- Resumo da Semana --")
print(f"Média da semana: {media} °C")
print(f"Maior temperatura: {maior} °C")
print(f"Menor temperatura: {menor} °C")