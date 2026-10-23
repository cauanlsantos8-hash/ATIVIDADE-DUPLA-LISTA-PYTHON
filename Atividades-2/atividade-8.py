import os
os.system("cls")

print("=== CLÍNICA VIDAPLENA - CADASTRO DE ACESSO ===")
login_cadastrado = input("Cadastre seu login: ").strip()
senha_cadastrada = input("Cadastre sua senha: ").strip()


print("=== CLÍNICA VIDAPLENA - LOGIN ===")

tentativas = 0
max_tentativas = 3
autenticado = False

while tentativas < max_tentativas and not autenticado:
    tentativas += 1
    
    login_digitado = input("Login: ").strip()
    senha_digitada = input("Senha: ").strip()

    if login_digitado == login_cadastrado and senha_digitada == senha_cadastrada:
        autenticado = True
    else:
        tentativas_restantes = max_tentativas - tentativas
        if tentativas_restantes > 0:
            print(f"Login ou senha incorretos! Tentativas restantes: {tentativas_restantes}\n")

if autenticado:
    print("\nBem-vindo(a) ao portal da Clínica VidaPlena!")
else:
    print("\nAcesso bloqueado! Número máximo de tentativas excedido.")