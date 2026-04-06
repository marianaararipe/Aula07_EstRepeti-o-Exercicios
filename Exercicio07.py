# 7) Peça uma frase e conte quantas dic_vogais há nela. Mostre o total de cada
# uma (a, e, i, o, u). [cite: 15, 16]



dic_vogais = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0,
}

frase = input("Digite uma frase ou palavra: ")

for letra in frase:
    if dic_vogais.__contains__(letra):
        dic_vogais[letra.lower()] += 1

print(f"A: {dic_vogais['a']}"
      f"\nE: {dic_vogais['e']}"
      f"\nI: {dic_vogais['i']}"
      f"\nO: {dic_vogais['o']}"
      f"\nU: {dic_vogais['u']}")
