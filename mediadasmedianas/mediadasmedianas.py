import statistics
import pytest
def mediana_das_medianas(lista, k):
    if len(lista) <= 5:
        return statistics.median(lista)
    subgrupos = [lista[i:i+5] for i in range(0, len(lista), 5)]
    medianas = [statistics.median(subgrupo) for subgrupo in subgrupos]
    
    pivo = mediana_das_medianas(medianas, len(medianas) // 2)
    
    menores = [x for x in lista if x < pivo]
    maiores = [x for x in lista if x > pivo]
    iguais = [x for x in lista if x == pivo]
    
    if k < len(menores):
        return mediana_das_medianas(menores, k)
    elif k < len(menores) + len(iguais):
        return pivo
    else:
        return mediana_das_medianas(maiores, k - len(menores) - len(iguais))

lista = [2,54,44,4,25,5,5,32,23,39,9,87,18,26,47,19,9,13,16,56,24,10,2,19,71]
k = len(lista)/2

resultado = mediana_das_medianas(lista, k)
print(f"A mediana das medianas é {resultado}")

