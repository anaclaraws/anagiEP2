#1
def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    
    if orientacao == "vertical":
        for i in range(tamanho):
            posicoes.append([linha + i, coluna])
    else:  
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])
    
    return posicoes 
#2
def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome_navio not in frota:
        frota[nome_navio] = [posicoes]
    else:
        frota[nome_navio].append(posicoes)
    
    return frota
#3
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'  
    else:
        tabuleiro[linha][coluna] = '-' 
    return tabuleiro
#4 
def posiciona_frota(frota):
    tabuleiro = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        tabuleiro.append(linha)
    for nome_navio in frota:
        for posicoes in frota[nome_navio]:
            for linha, coluna in posicoes:
                tabuleiro[linha][coluna] = 1

    return tabuleiro
#5
def afundados(frota, tabuleiro):
    navios_afundados = 0

    for nome_navio in frota:
        for posicoes in frota[nome_navio]:
            afundado = True
            for linha, coluna in posicoes:
                if tabuleiro[linha][coluna] != 'X':
                    afundado = False
                    break
            if afundado:
                navios_afundados += 1

    return navios_afundados
#6
def posicao_valida (frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    for nome_navio in frota:
        for posicoes_existentes in frota[nome_navio]:
            for linha_existente, coluna_existente in posicoes_existentes:
                if [linha_existente, coluna_existente] in posicoes:
                    return False

    for linha, coluna in posicoes:
        if linha < 0 or linha >= 10 or coluna < 0 or coluna >= 10:
            return False
        
    return True
#8
def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto