# [218. The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/)

O horizonte deve ser representado como uma lista de "pontos-chave" classificados por sua coordenada x no formato [[x1,y1],[x2,y2],...]. Cada ponto-chave é o ponto final esquerdo de algum segmento horizontal no horizonte, exceto o último ponto na lista, que sempre tem uma coordenada y 0 e é usado para marcar o término do horizonte onde termina o edifício mais à direita. Qualquer terreno entre os edifícios mais à esquerda e mais à direita deve fazer parte do contorno do horizonte.

Nota: Não deve haver linhas horizontais consecutivas de igual altura na linha do horizonte de saída. Por exemplo, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] não é aceitável; as três linhas de altura 5 devem ser mescladas em uma na saída final como tal: [...,[2 3],[4 5],[12 7],...]

#
*Exemplo 1:*

![Exampl1_leetcode](https://assets.leetcode.com/uploads/2020/12/01/merged.jpg)

Entrada: edifícios = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Saída: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Explicação:
A Figura A mostra os edifícios da entrada.
A Figura B mostra o horizonte formado por esses edifícios. Os pontos vermelhos na figura B representam os pontos-chave na lista de saída.

#
*Exemplo 2:*



Entrada: edifícios = [[0,2,3],[2,5,3]]
Saída: [[0,3],[5,0]]




## Restrições:

1 <= edifícios.comprimento <= 104

0 <= esquerdai < direitai <= 231 - 1

1 <= altura <= 231 - 1

edifícios é classificado por lefti em ordem não decrescente.