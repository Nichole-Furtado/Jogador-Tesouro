import numpy as np
from random import randint

###  Paradigma Funcional (indiretamente) = Ela não altera o estado do programa fora dela.
### Paradigma Procedural = Não chega a ser uma função pura, função pura é que modifica, mas é uma função que executa passos para exibir o mapa na tela.

def gerar_posicao_tesouro():
    return (randint(0, 4), randint(0, 4))
 
# começa o paradigma imperativo
while True:
    tesouro = gerar_posicao_tesouro()
    if tesouro != (0, 0):
        break

###  Paradigma Orientado a Objetos

class Jogador:
    def __init__(self, linha=0, coluna=0):
        self.linha = linha
        self.coluna = coluna

    def mover(self, direcao):
        movimentos = {
            "cima": (-1, 0),
            "baixo": (1, 0),
            "esquerda": (0, -1),
            "direita": (0, 1),
            "w": (-1, 0),
            "s": (1, 0),
            "a": (0, -1),
            "d": (0, 1)
        }

        if direcao in movimentos:
            nova_linha = self.linha + movimentos[direcao][0]
            nova_coluna = self.coluna + movimentos[direcao][1]
            if 0 <= nova_linha < 5 and 0 <= nova_coluna < 5:
                self.linha = nova_linha
                self.coluna = nova_coluna
                return True
            else:
                print("\n🚫 Movimento fora do limite!")
        else:
            print("\n⚠️ Direção inválida!")
        return False

    def posicao(self):
        return (self.linha, self.coluna) # Ele retorna a posição atual do jogador no mapa, como uma tupla no formato (linha, coluna).atributos

### Paradigma Procedural  é uma função que executa passos para exibir o mapa na tela.

def mostrar_mapa(mapa, jogador):
    mapa_temp = mapa.copy() # Isso evita modificar o mapa original enquanto mostramos o jogador nele.
    mapa_temp[jogador.linha, jogador.coluna] = -1 
    mapa_str = np.char.mod('%2d', mapa_temp) # Converte todos os números da matriz em strings formatadas com 2 dígitos (%2d).
    mapa_str[jogador.linha, jogador.coluna] = ' 😁'

    print("\nMapa atual:")
    for linha in mapa_str:
        print(" ".join(linha)) #Percorre cada linha do mapa e imprime os elementos separados por espaço e exibe a posição do jogador atual.

### Paradigma baseado em protótipos (simulação dinâmica)
###  Paradigma Procedural 

def dica(self, tesouro):
    dist = abs(self.linha - tesouro[0]) + abs(self.coluna - tesouro[1]) #O jogador está em (2, 3), O tesouro está em (4, 1). dist = abs(2 - 4) + abs(3 - 1)
    print(f"📍 Dica: Você está a {dist} passos do tesouro.")

setattr(Jogador, "dica", dica) #setattr é uma função que adiciona o método dica à classe Jogador

mapa = np.random.randint(1, 10, size=(5, 5))#numpy

### Paradigma Orientado a Objetos

jogador = Jogador()
pontuacao = 0

### Paradigma Imperativo ###

while True:
    mostrar_mapa(mapa, jogador)
    jogador.dica(tesouro)

    direcao = input("\nInforme a direção (cima, baixo, esquerda, direita ou W/A/S/D): ").strip().lower()

 ###Paradigma Imperativo###   

    if jogador.mover(direcao):
        pontuacao += 1
        if jogador.posicao() == tesouro:
            mostrar_mapa(mapa, jogador)
            print("\n🎉 PARABÉNS! Você encontrou o tesouro!")
            print(f"🏆 Pontuação final: {pontuacao}")
            print(f"📍 Tesouro estava em: {tesouro}")
            break