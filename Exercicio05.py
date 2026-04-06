# 5) O usuário tem 3 tentativas para acertar a senha. Se errar todas, o acesso
# é bloqueado. Use while.


SENHA_DEFINIDA = "12345"
tentativas_maximas = 3
tentativas_usadas = 0
acesso_concedido = False

while tentativas_usadas < tentativas_maximas:
    tentativas_restantes = tentativas_usadas - tentativas_usadas
    tentativa = int(input(f"Digite a senha ({tentativas_restantes} tentativas restantes): "))

    if tentativa == SENHA_DEFINIDA:
        print("Você acertou a senha! Acesso liberado")
        acesso_concedido = True
        break
    else:
        tentativas_usadas += 1
        print("Senha incorreta! Tente novamente")

if not acesso_concedido:
    print("\nACESSO BLOQUEADO! Você errou as 3 tentativas.")
