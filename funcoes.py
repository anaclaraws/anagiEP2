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
