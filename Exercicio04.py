# 4) Crie um programa que peça dois números inteiros e exiba todos os números
# entre eles que são primos. Use for.


listaPrimos = []

inicio = int(input("Digite o primeiro número: "))
fim = int(input("Digite o segundo número: "))

# inverte valores pro programa funcionar
if inicio > fim:
    inicio, fim = fim, inicio


for num in range(inicio, fim + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                break
        else:
            listaPrimos.append(num)

if len(listaPrimos) > 0:
    print(f"\nNúmeros primos entre {inicio} e {fim}")
    for primo in listaPrimos:
        print(f"-> {primo}")
    print(f"\nNúmero total de primos encontrados: {len(listaPrimos)}")

else:
    print(f"Não foram encontrados nenhum número primo entre {inicio} e {fim}")