class Solution:
    def longestSubstring(self, s, k):
        return self.divideAndConquer(s, k, 0, len(s))

    def divideAndConquer(self, s, k, start, end):
        # Caso base: tamanho da substring é menor que k
        if end - start < k:
            return 0

        counter = {}
        # Conta a frequência de cada caractere na substring atual
        for i in range(start, end):
            counter[s[i]] = counter.get(s[i], 0) + 1

        for i in range(start, end):
            # Verifica se algum caractere possui contagem menor que k
            if counter[s[i]] < k:
                # Divide a substring em duas partes e chama recursivamente a função para cada parte
                left = self.divideAndConquer(s, k, start, i)
                right = self.divideAndConquer(s, k, i + 1, end)
                return max(left, right)

        # Se todos os caracteres possuem contagem maior ou igual a k, retorna o tamanho da substring
        return end - start