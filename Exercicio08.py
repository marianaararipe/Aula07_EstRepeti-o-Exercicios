# 8) Simule o lançamento de uma moeda até sair "cara" três vezes seguidas.
# (Dica: usar random.choice(["cara", "coroa"]) e while).


import random

contadorSeguindas = 0
totalLancamentos = 0


while contadorSeguindas < 3:
    resultado = random.choice(["cara", "coroa"])
    totalLancamentos += 1

    print(f"{totalLancamentos}º Lançamento: {resultado.upper()}")

    if resultado == "cara":
        contadorSeguindas += 1
    else:
        contadorSeguindas = 0  # se cair coroa, reinicia a variavel


print(f"\nTotal de lançamentos necessários: {totalLancamentos}")
"""
contador = 0

while contador < 3:
    resultado = random.choice(["cara", "coroa"])
    print(resultado)
    contador = contador + 1 if resultado == "cara" else 0

"""