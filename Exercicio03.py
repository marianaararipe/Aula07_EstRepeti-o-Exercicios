# 3) Monte um sistema que repita um menu até o usuário escolher sair.
# Use while e break.

opcoes_menu = ["Chocolate Quente", "Café", "Leite", "Suco de Laranja"]

while True:
    print("\n[S] Visualizar Menu")
    print("[N] Sair do Programa")

    escolha = input("Deseja visualizar o menu? (S/N): ").upper()

    if escolha == "S":
        print("\n--- Cardápio em exibição ---")
        for item in opcoes_menu:
            print(f"- {item}")

    elif escolha == "N":
        print("Programa encerrado!")
        break
    else:
        print("\nOpção inválida! Por favor, digite apenas S ou N")
