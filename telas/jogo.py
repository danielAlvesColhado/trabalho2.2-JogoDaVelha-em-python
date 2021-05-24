from jogo.trocar_vez import trocar_vez
from telas.jogadores import buscar_nome_jogador_da_vez
from telas.mensagens import mensagem_jogador_ganhou

quantidade_de_rodadas = 0


def jogada(jogador1, jogador2, tabuleiro, jogador, nome_jogador_da_vez):
    posicao_ocupada = True
    marcador = 'X' if jogador['id'] == 1 else 'O'
    print(f'vez do {nome_jogador_da_vez}')
    while posicao_ocupada:
        linha = int(input(f'{nome_jogador_da_vez} Informe qual linha deseja por um {marcador}'))
        coluna = int(input(f'{nome_jogador_da_vez} Agora informe qual coluna: '))
        if tabuleiro[linha][coluna] == 'nada':
            tabuleiro[linha][coluna] = marcador
            posicao_ocupada = False
        else: print('Essa posiçao já foi ocupada! tente outra: ')
    trocar_vez(jogador1, jogador2)



def ver_se_alguem_ganhou(jogador1, jogador2 , tabuleiro, quantidade_de_rodadas):
    #olhando as linhas:
    for linha in range(0, 3):
        if tabuleiro[linha] == ['X', 'X', 'X']:
            return True, mensagem_jogador_ganhou(jogador1, quantidade_de_rodadas)
        elif tabuleiro[linha] == ['O', 'O', 'O']:
            return True, mensagem_jogador_ganhou(jogador2, quantidade_de_rodadas)
    #olhando as colunas:
    for j in range(0, 3):
        if tabuleiro[0][j] + tabuleiro[1][j] + tabuleiro[2][j] == 'XXX':
            return True, mensagem_jogador_ganhou(jogador1, quantidade_de_rodadas)
        elif tabuleiro[0][j] + tabuleiro[1][j] + tabuleiro[2][j] == 'OOO':
            return True, mensagem_jogador_ganhou(jogador2, quantidade_de_rodadas)
    #olhando as diagonais:
        if tabuleiro[0][0] + tabuleiro[1][1] + tabuleiro[2][2] == 'XXX' \
                or tabuleiro[0][2] + tabuleiro[1][1] + tabuleiro[2][0] == 'XXX':
            return True, mensagem_jogador_ganhou(jogador1, quantidade_de_rodadas)
        elif tabuleiro[0][0] + tabuleiro[1][1] + tabuleiro[2][2] == 'OOO' \
                or tabuleiro[0][2] + tabuleiro[1][1] + tabuleiro[2][0] == 'OOO':
            return True, mensagem_jogador_ganhou(jogador2, quantidade_de_rodadas)

        if quantidade_de_rodadas == 9:
            print('OCORREU UM EMPATE! JOGO ENCERRADO')
            return True