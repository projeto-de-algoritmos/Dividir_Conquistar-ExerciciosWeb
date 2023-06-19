# [395. Substring mais longa com pelo menos K caracteres repetidos](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/)
dificuldade : Médio

Dada uma string se um inteiro k, retorne o comprimento da substring mais longa de s tal que a frequência de cada caractere nessa substring seja maior ou igual a k .
#
*Exemplo 1:*

Entrada: s = "aaabb", k = 3

 Saída: 3

 Explicação: A substring mais longa é "aaa", pois 'a' é repetido 3 vezes.

#
*Exemplo 2:*



Entrada: s = "ababbc", k = 2

 Saída: 5

 Explicação: A substring mais longa é "ababb", pois 'a' é repetido 2 vezes e 'b' é repetido 3 vezes.
 



## Restrições:

1 <= s.length <= 104

sconsiste apenas em letras minúsculas do inglês.

1 <= k <= 105