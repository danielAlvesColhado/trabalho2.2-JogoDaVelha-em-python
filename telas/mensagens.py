
def mensagem_inicializacao_do_jogo():
    print()
    print('INICIANDO O JOGO..')
    print()


def mensagem_criacao_jogador(jogador):
    print(f'criacao do {jogador}!')

def mensagem_jogador_ganhou(jogador, quantidade_de_rodadas):
    print('')
    print(f"jogador {jogador.get('nome')} Ganhou apos {quantidade_de_rodadas} rodadas!")
    print('Parabens!')