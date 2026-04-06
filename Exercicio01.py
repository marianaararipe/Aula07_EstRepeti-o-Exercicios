# 1) Peça 10 números e conte quantos são múltiplos de 3. Use for.


listaNum = []
contadorMultiplos = 0

print("Digite 10 números inteiros:")

for i in range(10):
    num = int(input(f"Digite o {i + 1}º número: "))
    listaNum.append(num)

for n in listaNum:
    if n % 3 == 0:
        contadorMultiplos += 1

if len(listaNum) > 0:
    print(f"\nVocê digitou 10 números")
    print(f"Desses números, {contadorMultiplos} são múltiplos de 3")
else:
    print("Nenhum número foi digitado!")