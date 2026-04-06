# 9) Crie um programa que leia uma sequência de números e determine quantos
# números são menores que a média.

# Exercicio 9
listaNum = []
print("(Digite 0 para parar de dar números")
i = 0

while True:
    valor = float(input(f'Digite o {i + 1}° valor: '))

    if valor == 0:
        break

    listaNum.append(valor)
    i += 1

if len(listaNum) > 1:
    soma = sum(listaNum)
    quantidade = len(listaNum)
    media = soma / quantidade

    contadorMenores = 0

    for i in listaNum:
        if i < media:
            contadorMenores += 1

    print(f"\nVocê digitou {quantidade} números")
    print(f"A média deles é: {media:.2f}")
    print(f"Desses números, {contadorMenores} estão abaixo da média")
else:
    print("Você não digitou nenhum número")


