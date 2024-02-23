# Astro Ape

Bem-vindo ao Astro Ape, um jogo emocionante onde você controla um macaco no espaço! Seu objetivo é levar o macaco até o planeta dos macacos, desviando das bananas que atuam como atratores gravitacionais. 

## Como jogar

- Use o mouse para controlar o lançamento do macaco.
- Clique para impulsionar o macaco na direção que o mouse aponta.
- A velocidade pode ser controlada pela distância do mouse até o macaco, sendo representada na barrinha de velocidade no canto inferior esquerdo.
- Desvie das bananas para não ser puxado por sua gravidade.
- Chegue ao planeta dos macacos para ganhar o jogo!

## Como executar o programa

1. Certifique-se de ter o Python e a biblioteca Pygame instalados em seu computador.
2. Clone este repositório em sua máquina.
3. Abra um terminal na pasta do jogo e execute o seguinte comando:

    python main.py

4. Divirta-se jogando Astro Ape!

## Modelo físico

O modelo físico do jogo Astro Ape é baseado na interação entre o macaco, as bananas e os planetas. A força gravitacional é calculada usando a lei da gravitação universal de Newton, com algumas pequenas alterações com a finalidade de ser mais lúdico. A equação para a força gravitacional entre duas massas é dada por:

$$ F = G \cdot \frac{{m_1 \cdot m_2}}{{r^2}} $$

onde:
- \( F \) é a força gravitacional entre as duas massas,
- \( G \) é a constante gravitacional,
- \( m_1 \) e \( m_2 \) são as massas das duas massas,
- \( r \) é a distância entre os centros das duas massas.

No jogo, o macaco é atraído pela gravidade das bananas, que por sua vez tem uma constante de força, que acaba por "substituir" todas as constantes da fórmula, sendo elas o G, o m_1 e o m_2. Isso se fez necessário, pois dessa forma obtém-se o mesmo resultado e fica mais fácil de manipular a força de atração que a banana tem, que conforme passam as fases, sobe gradativamente. A força resultante sobre o macaco é a soma vetorial das forças de atração de todas as bananas dispostas na fase. Essa força resultante é então usada para atualizar a velocidade e a posição do macaco no próximo quadro do jogo.

Além da gravidade, também incorpora a interação do jogador com o mouse. Quando o jogador clica na tela, o macaco recebe um impulso na direção do cursor do mouse, proporcionando um controle adicional sobre o movimento do macaco no espaço.

## Créditos

- Desenvolvido por Ana Helena Caiafa e Esther Caroline Cunha Rodrigues