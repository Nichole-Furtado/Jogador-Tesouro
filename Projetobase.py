## Objetivo é navegar até achar o tesouro ##

import numpy as np #apelido np

#Mapa 5x5

mapa = np.random.randint(1,10, size=(5,5)) #cria um mapa 5x5 com valores aleatórios entre 1 e 10

#Posiciona o tesouro em uma posição aleatória do mapa

while True:
    tesouro_linha, tesouro_coluna = np.random.randint(0,5, size=2)
    if (tesouro_linha, tesouro_coluna) != (0,0):
        break

#Posiciona o jogador na posição (0,0)
posicao_jogador = (0,0)
pontuacao = 0

#Função para mostrar o mapa

def mostrar_mapa(mapa, posicao_jogador):
    mapa_com_jogador = mapa.copy()
    linha, coluna = posicao_jogador
    mapa_com_jogador[linha, coluna] = -1 #marca a posição do jogador com -1
    mapa_com_jogador_str = np.char.mod('%2d', mapa_com_jogador)  # Converte todos para string
    mapa_com_jogador_str[linha, coluna] = ' N'  # Marca jogador com 'N'

    print("\n Mapa atual:")
    for linha in mapa_com_jogador_str:
        print(" ".join(linha))

# Fluxo Principal do jogo
while True:
    mostrar_mapa(mapa, posicao_jogador) #mostra o mapa

    direcao = input("Informe a direção que deseja mover? (cima, baixo, esquerda, direita): ").strip().lower() #Dicionario pede a direção que o jogador quer mover

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
        nova_posicao = (posicao_jogador [0] + movimentos [direcao][0], 
                        posicao_jogador[1] + movimentos[direcao][1])
    else:
        print("⚠️⚠️⚠️ Direção inválida. Tente novamente!⚠️⚠️⚠️")
        
# Verifica se a nova posição é valida

    if not ( 0 <= nova_posicao[0] < mapa.shape[0] and 0 <= nova_posicao[1] < mapa.shape[1]):
        print("\n 🚫🚫🚫 Movimento Fora do Limite. Tente novamente!🚫🚫🚫")
        continue #pula para a próxima iteração do loop

    posicao_jogador = nova_posicao
    pontuacao += 1

    if posicao_jogador == (tesouro_linha, tesouro_coluna):
        mostrar_mapa(mapa, posicao_jogador)
        print("\n\n🎉 PARABÉNS! Você encontrou o tesouro!")
        print(f"🏆 Pontuação Final: {pontuacao}")
        print(f"📍 Tesouro estava na posição: ({tesouro_linha}, {tesouro_coluna})")
        break #sai do loop e termina o jogo 