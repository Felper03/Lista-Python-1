import random

# Função para carregar a lista de palavras do arquivo
def carregar_palavras():
    with open('lista_palavras.txt', 'r') as arquivo:
        palavras = [linha.strip() for linha in arquivo]
    return palavras

# Função para escolher uma palavra aleatória da lista
def escolher_palavra(palavras):
    return random.choice(palavras)

# Função para mostrar o teclado com letras disponíveis
def mostrar_teclado(letras_disponiveis):
    return ' '.join(letras_disponiveis)

# Função para verificar a palavra digitada e dar feedback de cores
def verificar_palavra(palavra_secreta, palavra_digitada):
    feedback = []

    for i in range(len(palavra_secreta)):
        if palavra_digitada[i] == palavra_secreta[i]:
            feedback.append("\x1b[32m" + palavra_digitada[i] + "\x1b[0m")  # Verde para letras corretas
        elif palavra_digitada[i] in palavra_secreta:
            feedback.append("\x1b[33m" + palavra_digitada[i] + "\x1b[0m")  # Amarelo para letras na palavra, mas não na posição correta
        else:
            feedback.append("\x1b[31m" + palavra_digitada[i] + "\x1b[0m")  # Vermelho para letras erradas

    return ' '.join(feedback)

# Função principal do jogo
def jogo_term_ooo():
    print("Bem-vindo ao Jogo Term.ooo!")

    palavras = carregar_palavras()
    palavra_secreta = escolher_palavra(palavras)
    letras_disponiveis = set(palavra_secreta.lower())
    tentativas_restantes = 5

    print("\nDica: A palavra tem", len(palavra_secreta), "letras.")

    while tentativas_restantes > 0:
        print("\nTentativas Restantes:", tentativas_restantes)
        print("Letras Disponíveis:", mostrar_teclado(letras_disponiveis))

        palavra_digitada = input("\nDigite a palavra ({} letras): ".format(len(palavra_secreta))).lower()

        if len(palavra_digitada) != len(palavra_secreta):
            print("Digite uma palavra com", len(palavra_secreta), "letras.")
            continue

        if palavra_digitada == palavra_secreta:
            print("\nParabéns! Você acertou a palavra:", palavra_secreta)
            break
        else:
            tentativas_restantes -= 1
            letras_disponiveis -= set(palavra_digitada)
            feedback = verificar_palavra(palavra_secreta, palavra_digitada)
            print("Feedback:", feedback)

    if tentativas_restantes == 0:
        print("\nVocê perdeu! A palavra era:", palavra_secreta)

if __name__ == "__main__":
    jogo_term_ooo()
