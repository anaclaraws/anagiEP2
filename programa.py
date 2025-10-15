frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}  
tipos = [
    ("porta-aviões", 4, 1),
    ("navio-tanque", 3, 2),
    ("contratorpedeiro", 2, 3),
    ("submarino", 1, 4)
]
from funcoes import *
#1
for nome, tamanho, quantidade in tipos:
    for i in range(quantidade):
        while True:
            print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))

            if tamanho == 1:
                orientacao = "vertical"
            else:
                op = int(input("[1] Vertical [2] Horizontal >"))
                orientacao = "vertical" if op == 1 else "horizontal"

            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                break
            else:
                print("Esta posição não está válida!")
print(frota)