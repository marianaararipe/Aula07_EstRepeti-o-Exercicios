# 2) Crie um programa que simule o uso de senha com tentativas infinitas até
# digitar a senha correta (use while True).


SENHA_CORRETA = "12345" # variaveis fixas em maiusculo
tentativas = 0

while True:
    tentatativas += 1
    senha_digitada = input(f"Tentativa {tentativas} - Digite a senha: ")

    if (senha_digitada == SENHA_CORRETA):
        print(f"Senha correta digitada após {tentativas} tentativas")
        break
    else:
        print("Senha incorreta! Tente novamente\n")