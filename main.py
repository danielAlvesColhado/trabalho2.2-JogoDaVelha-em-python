from jogo.jogadores import criar_jogadores, sortear_jogador_inicial, jogador_da_vez
from jogo.tabuleiro import cria_tabuleiro
from telas.jogadores import buscar_nome_jogador_da_vez
from telas.jogo import jogada, ver_se_alguem_ganhou
from telas.mensagens import mensagem_inicializacao_do_jogo
from telas.tabuleiro import mostrar_tabuleiro

jogador1 = None
jogador2 = None


def rodar_jogo_da_veia():
    quantidade_de_rodadas = 0
    mensagem_inicializacao_do_jogo()
    jogador1, jogador2 = criar_jogadores()
    sortear_jogador_inicial(jogador1, jogador2)
    tabuleiro = cria_tabuleiro()

    jogadas = True
    while jogadas:
        mostrar_tabuleiro(tabuleiro)
        jogada(jogador1=jogador1, jogador2=jogador2, jogador=jogador_da_vez(jogador1, jogador2), tabuleiro=tabuleiro,
               nome_jogador_da_vez=buscar_nome_jogador_da_vez(jogador1, jogador2))
        quantidade_de_rodadas += 1
        if ver_se_alguem_ganhou(jogador1, jogador2, tabuleiro, quantidade_de_rodadas):
            jogadas = False









rodar_jogo_da_veia()



#faltou contar os pontos e determinar jogadas maximas(empate)
#mostrar ganhador


