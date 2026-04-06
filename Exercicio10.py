# 10) Crie um programa que leia uma sequência de números e determine o segundo
# maior número.



# Exercicio 10

print("(Digite 0 para parar de dar números")

maior = None
segundo_maior = None
listaNum = []
i = 0

while True:
    num = float(input(f'Digite o {i + 1}° número: '))
    i += 1

    if num == 0:
        break

    if maior is None:
        maior = num
    elif num > maior:
        segundo_maior = maior
        maior = num
    elif segundo_maior is None or num > segundo_maior:
        segundo_maior = num

if segundo_maior is not None:
    print(f"\nO maior número digitado foi {maior}")
    print(f"O segundo maior número digitado foi {segundo_maior}")
else:
    print("Não foram digitados números suficientes para comparação")