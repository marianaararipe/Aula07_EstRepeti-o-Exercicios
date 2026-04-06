"""
2) Jogo da Forca:
Crie um jogo da forca, onde:
- Palavra oculta: A palavra é escolhida aleatoriamente de uma lista de palavras pré-definidas.
- A palavra deve ser exibida com espaços (_) representando cada letra. O jogador deve tentar adivinhar
  as letras da palavra.
- Feedback dinâmico: O jogo deve mostrar a palavra com as letras corretas já adivinhadas a cada tentativa.
- O jogo também deve mostrar as letras erradas que o jogador já tentou, para evitar que ele repita a mesma letra.
- Caso o jogador tente uma letra que já tenha sido usada (correta ou incorreta), o jogo deve informar
  que ele já tentou essa letra, pedindo que ele tente outra.
- Número de tentativas: O jogador tem um total de 6 tentativas para errar antes de perder o jogo.
  A cada erro, o número de tentativas diminui.
- Mensagens de vitória ou derrota: O jogo deve informar ao jogador quando ele ganhar, revelando a
  palavra completa. Caso o jogador perca, o jogo deve revelar a palavra e informar que ele perdeu.


"""

import random

palavras = [
    "galaxia", "nuvem", "labirinto", "orquestra", "horizonte",
    "ampulheta", "mochila", "eclipse", "viagem", "esmeralda"
]

palavra = random.choice(palavras)
letras_tentadas = []
erros = 0
limite = 6

print("\n=== JOGO DA FORCA ===")

while erros < limite:
    acertou = True


    print("\nPalavra: ", end="")
    for letra in palavra:
        if letra in letras_tentadas: #mostra a letra na posição
            print(letra, end=" ")
        else:
            print("_", end=" ") # substitui os caracteres por _
            acertou = False

    # Verifica vitória
    if acertou:
        print("\nVocê venceu!")
        print("Palavra:", palavra)
        break

    # alguns status
    print("\nLetras tentadas:", letras_tentadas)
    print("Tentativas restantes:", limite - erros)


    # entrada das letras
    tentativa = input("Digite uma letra: ").lower()

    # Validação
    if tentativa in letras_tentadas:
        print("Você já tentou essa letra! Escolha outra letra")
        continue

    letras_tentadas.append(tentativa)


    # erros e acertos
    if tentativa not in palavra:
        erros += 1
        print("❌ Errou!")
    else:
        print("✅ Acertou!")

# Derrota
if erros == limite:
    print("\nVocê perdeu!")
    print("A palavra era:", palavra)
