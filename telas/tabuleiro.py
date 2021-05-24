from utils.utils import adiciona_cor


def mostrar_tabuleiro(tabuleiro):
    for i, linha in enumerate(tabuleiro):
        if i == 0:
            mostrar_indice_coluna(len(linha))
        mostrar_indice_linha(i)
        for posicao in linha:
            if posicao == 'nada':
                mostrar = ' - '
            elif posicao == 'X':
                mostrar = ' X '
            else: mostrar = ' O '
            print(f"{mostrar}", end=' ')
        print('')



def mostrar_indice_coluna(tamanho_linha):
    for count in range(0, tamanho_linha):
        end = '\n' if count == tamanho_linha - 1 else ' '
        espaco_extra = '  ' if count == 0 else ''
        print(f'{espaco_extra} {adiciona_cor("33m", count)} ', end=end)



def mostrar_indice_linha(indice):
    print(adiciona_cor("33m", indice), end=':')