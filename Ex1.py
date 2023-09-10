def criar_tabuleiro():
    # Esta função cria um tabuleiro vazio usando um dicionário onde as chaves são tuplas (linha, coluna) e os valores são espaços em branco
    return {(linha, coluna): ' ' for linha in range(3) for coluna in range(3)}

def exibir_tabuleiro(tabuleiro):
    # Esta função exibe o tabuleiro na tela
    for linha in range(3):
        for coluna in range(3):
            print(tabuleiro[(linha, coluna)], end='')
            if coluna < 2:
                print(' | ', end='')
        print()
        if linha < 2:
            print('-' * 5)

def realizar_jogada(tabuleiro, linha, coluna, jogador):
    # Esta função realiza uma jogada verificando se a posição está vazia e, se estiver, coloca o símbolo do jogador na posição escolhida
    if tabuleiro[(linha, coluna)] == ' ':
        tabuleiro[(linha, coluna)] = jogador
        return True
    else:
        return False

def verificar_vitoria(tabuleiro, jogador):
    # Esta função verifica se o jogador atual venceu o jogo, percorrendo todas as possíveis combinações
    linhas_vitoria = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]

    for linha_vitoria in linhas_vitoria:
        if all(tabuleiro[c] == jogador for c in linha_vitoria):
            return True
    return False

def jogo_da_velha():
    # Função principal que controla o jogo
    tabuleiro = criar_tabuleiro()
    jogador_atual = 'X'
    jogo_acabou = False

    while not jogo_acabou:
        exibir_tabuleiro(tabuleiro)
        linha = int(input(f'Jogador {jogador_atual}, escolha a linha (0, 1, 2): '))
        coluna = int(input(f'Jogador {jogador_atual}, escolha a coluna (0, 1, 2): '))

        if realizar_jogada(tabuleiro, linha, coluna, jogador_atual):
            if verificar_vitoria(tabuleiro, jogador_atual):
                exibir_tabuleiro(tabuleiro)
                print(f'Jogador {jogador_atual} venceu!')
                jogo_acabou = True
            elif ' ' not in tabuleiro.values():
                exibir_tabuleiro(tabuleiro)
                print('Empate!')
                jogo_acabou = True
            else:
                jogador_atual = 'O' if jogador_atual == 'X' else 'X'

if __name__ == "__main__":
    jogo_da_velha()

