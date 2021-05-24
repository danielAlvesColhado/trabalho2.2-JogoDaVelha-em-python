def cria_tabuleiro():
    tabuleiro = []
    for linha in range(0, 3):
        linha = []
        for posicao in range(0, 3):
            linha.append('nada')
        tabuleiro.append(linha)
    return tabuleiro