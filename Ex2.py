def criar_tabuleiro(dimensao):
    # Esta função cria um tabuleiro vazio usando um dicionário onde as chaves são tuplas (linha, coluna) e os valores são espaços em branco
    return {(linha, coluna): ' ' for linha in range(dimensao) for coluna in range(dimensao)}

def exibir_tabuleiro(tabuleiro):
    # esta funçao exibe o tabuleiro na tela, adaptando-se a dimensão fornecida
    dimensao = int(len(tabuleiro) ** 0.5)
    for linha in range(dimensao):
        for coluna in range(dimensao):
            print(tabuleiro[(linha, coluna)], end='')
            if coluna < dimensao - 1:
                print(' | ', end='')
        print()
        if linha < dimensao - 1:
            print('-' * (4 * dimensao - 1))

def realizar_jogada(tabuleiro, linha, coluna, jogador):
    # Esta função realiza uma jogada verificando se a posição está vazia e, se estiver, coloca o símbolo do jogador na posição escolida
    if tabuleiro[(linha, coluna)] == ' ':
        tabuleiro[(linha, coluna)] = jogador
        return True
    else:
        return False

def verificar_vitoria(tabuleiro, jogador):
    # Esta função verifica se o jogador atual venceu o jogo, percorrendo todas as possíveis combinações de vitória na dimensão atual
    dimensao = int(len(tabuleiro) ** 0.5)
    for i in range(dimensao):
        linha_vitoria = [(i, j) for j in range(dimensao)]
        coluna_vitoria = [(j, i) for j in range(dimensao)]
        if all(tabuleiro[c] == jogador for c in linha_vitoria) or all(tabuleiro[c] == jogador for c in coluna_vitoria):
            return True

    diagonal1 = [(i, i) for i in range(dimensao)]
    diagonal2 = [(i, dimensao - i - 1) for i in range(dimensao)]

    if all(tabuleiro[c] == jogador for c in diagonal1) or all(tabuleiro[c] == jogador for c in diagonal2):
        return True

    return False

def jogo_da_velha():
    # Função principal que controla o jogo com dimensões flexíveis
    dimensao = int(input('Informe o número de linhas e colunas: '))
    tabuleiro = criar_tabuleiro(dimensao)
    jogador_atual = 'X'
    jogo_acabou = False

    while not jogo_acabou:
        exibir_tabuleiro(tabuleiro)
        linha = int(input(f'Jogador {jogador_atual}, escolha a linha (0 a {dimensao - 1}): '))
        coluna = int(input(f'Jogador {jogador_atual}, escolha a coluna (0 a {dimensao - 1}): '))

        if 0 <= linha < dimensao and 0 <= coluna < dimensao:
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
            else:
                print('Essa posição já está ocupada. Tente novamente.')
        else:
            print(f'Posição inválida. Escolha uma linha e coluna entre 0 e {dimensao - 1}.')

if __name__ == "__main__":
    jogo_da_velha()
