def pedir_nome(id):
    return input(f'jogador{id} Informe seu nome: ')

def buscar_nome_jogador_da_vez(jogador1, jogador2):
    nome_jogador_da_vez = jogador1.get('nome') if jogador1.get('vez') else jogador2.get('nome')
    return nome_jogador_da_vez