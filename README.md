# Astro Ape

Esse é o Astro Ape, ou como o nome indica, o "Macaco Astronauta". O personagem principal do jogo é um macaquinho muito sagaz que está em uma aventura para voltar ao seu planeta de origem, o planeta dos Macacos! O jogo é composto por três fases, sendo cada uma delas um planeta novo que o macaquinho deve chegar e explorar, adquirindo cada vez mais destreza em sua jornada. No entanto ele terá de enfrentar um desafio muito difícil..resistir à força gravitacional das bananas que o desviam de sua rota original! Tome cuidado com elas e faça uma boa viagem! 

## Como jogar

- Use o mouse para controlar o lançamento do macaco, apontando para o destino: o planeta.
- Clique para impulsionar o macaco na direção que o mouse aponta.
- A velocidade pode ser controlada pela distância do mouse até o macaco, sendo representada na barrinha de velocidade no canto inferior esquerdo.
- Desvie das bananas para não ser puxado por sua gravidade.
- Chegue ao planeta dos macacos para ganhar o jogo!

## Como executar o programa

1. Instale o Python e as bibliotecas Pygame e numpy.
2. Clone este repositório em seu computador.
3. Abra um terminal na pasta do jogo e execute no terminal: python main.py

## Modelo físico

O modelo físico utilizado no jogo é baseado na interação entre o macaco, as bananas e os planetas. Foi feito o uso da fórmula da lei de gravitação de Newton para representar essa interação, como podemos verficar abaixo: 

$$ F = G \cdot \frac{{m_1 \cdot m_2}}{{r^2}} $$

onde:
- F é a força gravitacional,
- G é a constante gravitacional,
- $m_1$ e $m_2$ são as massas dos planetas,
- r é a distância entre os centros dos planetas.

No jogo, o macaco é atraído pela força gravitacional das bananas, que atuam como os corpos celestes de nosso sistema solar. Para representar isso, as constantes que definem a força gravitacional (G, $m_1$ e $m_2$) estão sendo representadas pela variável "constant_banana", que por sua vez, simula o valor das mesmas, tornando mais fácil a manipulação da atração dos corpos, podendo deixá-la mais ou menos potente. O valor da constante é dividido pela distância ao quadrado entre os corpos, que está sendo calculada pela diferença vetorial entre o macaco e o planeta, e após isso, normaliza-se o vetor com a intenção de manipular sua velocidade de forma uniforme. A força resultante que atua sobre o macaco é a soma vetorial das forças de atração de todas as bananas que estão na fase. Dessa forma, pode-se atualizar a velocidade e a posição do macaco no próximo quadro do jogo.

## Créditos

- Desenvolvido por Ana Helena Caiafa e Esther Caroline Cunha Rodrigues