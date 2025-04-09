# 🗺️ Jogo "Jogador vs Tesouro"

Bem-vindo ao **Jogador vs Tesouro**, um jogo simples em Python onde o jogador precisa explorar um mapa em busca de um tesouro escondido! Ideal para quem está começando no mundo da programação ou quer praticar conceitos como orientação a objetos, leitura de arquivos, e interação via terminal.

---

## 📂 Estrutura do Projeto

```
Jogador-Tesouro/
├── Jogador.py     # Classe responsável pelo controle do jogador
├── Tesouro.py     # Classe que gerencia a posição do tesouro
├── mapa.txt       # Representação visual do mapa do jogo
├── main.py        # Arquivo principal para executar o jogo
└── README.md      # Este arquivo
```

---

## 🚀 Como Rodar o Jogo

1. **Clone ou baixe o repositório**

   ```bash
   git clone https://github.com/seu-usuario/Jogador-Tesouro.git
   cd Jogador-Tesouro
   ```
2. **Execute o jogo com Python 3**

   ```bash
   python main.py
   ```

---

## 🎮 Como Jogar

- O jogador se movimenta em um mapa lido de um arquivo (`mapa.txt`).
- O objetivo é encontrar o **tesouro escondido** em algum ponto do mapa.
- As posições do jogador e do tesouro são atualizadas a cada jogada.
- O jogo termina quando o jogador encontra o tesouro.

---

## 🧠 Conceitos Envolvidos

- Leitura e manipulação de arquivos (`mapa.txt`)
- Programação orientada a objetos (classes `Jogador` e `Tesouro`)
- Loops e controle de fluxo
- Lógica de movimentação em matrizes

---

## 📌 Exemplo de Mapa (`mapa.txt`)

```
##########
#        #
#  J     #
#     T  #
##########
```

- `#`: Parede (intransponível)
- Espaço em branco: Caminho livre
- `J`: Jogador
- `T`: Tesouro

---

## 🔧 Personalização

Você pode modificar o arquivo `mapa.txt` para criar seus próprios desafios, alterar o tamanho do mapa ou adicionar obstáculos!

---

## ✨ Sugestões de Melhorias

- Adicionar obstáculos aleatórios
- Criar inimigos ou armadilhas
- Contador de passos
- Interface gráfica com `pygame`
