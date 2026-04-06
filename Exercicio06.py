# 6) Peça 10 números e separe em duas listas: pares e ímpares.
# Mostre as duas no final.



listaPares = []
listaImpares = []

print("Digite 10 números inteiros:")

for i in range(1, 11):
    num = int(input(f"Digite o {i}º número: "))

    if num % 2 == 0:
        listaPares.append(num)
    else:
        listaImpares.append(num)


print(f"\nNúmeros Pares ({len(listaPares)}): {listaPares}")
print(f"Números Ímpares ({len(listaImpares)}): {listaImpares}")
print("=" * 30)