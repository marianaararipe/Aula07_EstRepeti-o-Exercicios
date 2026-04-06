"""
1) Simulação de Populações de Coelhos:
Crie um programa que simule o crescimento de uma população de coelhos ao longo de várias gerações.
Os coelhos se reproduzem a uma taxa fixa a cada geração, e uma porcentagem deles morre a cada geração.
O programa deve solicitar ao usuário a taxa de reprodução, a taxa de mortalidade e o número inicial de coelhos.
Use um loop for ou while para simular várias gerações e exiba a população de coelhos após um número de
gerações especificado pelo usuário.
"""

populacao_atual = int(input("Insira o número inicial de coelhos: "))
taxa_reproducao = float(input("Insira a taxa de reprodução (em %): "))
taxa_mortalidade = float(input("Insira a taxa de mortalidade (em %): "))
geracoes = int(input("Quantas gerações deseja simular? "))

for i in range(1, geracoes+1):
    nascimentos = populacao_atual * (taxa_reproducao / 100)
    mortes = populacao_atual * (taxa_mortalidade / 100)

    populacao_atual = populacao_atual + nascimentos - mortes

    print(f"Geração {i}: {populacao_atual} coelhos")

    if populacao_atual < 1:
        populacao_atual = 0
        print("A população foi extinta")
        break

print(f"População final após a simulação: {populacao_atual} coelhos.")




#reproducao = int(input("Insira a taxa de reprodução (em %): "))
# mortalidade = int(input("Insira a taxa de mortalidade (em %): "))
# inicial = int(input("Insira o número inicial de coelhos: "))
# nova_populacao = inicial
#
# for x in range(100):
#     nova_populacao = inicial - ((mortalidade / 100) * inicial) + ((reproducao / 100) * inicial)
#     inicial = nova_populacao
#     print(f"Geração {x + 1}: {int(nova_populacao)}")
#
#     if nova_populacao < 1:
#         print("Extintos.")
#         break