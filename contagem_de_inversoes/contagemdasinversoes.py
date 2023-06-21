def merge_sort_contagem_inversoes(lista):
    if len(lista) <= 1:
        return lista, 0
    
    meio = len(lista) // 2
    esquerda, inversoes_esq = merge_sort_contagem_inversoes(lista[:meio])
    direita, inversoes_dir = merge_sort_contagem_inversoes(lista[meio:])
    intercalado, inversoes = merge_contagem_inversoes(esquerda, direita)
    
    return intercalado, inversoes + inversoes_esq + inversoes_dir

def merge_contagem_inversoes(esquerda, direita):
    intercalado = []
    inversoes = 0
    i = j = 0
    
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            intercalado.append(esquerda[i])
            i += 1
        else:
            intercalado.append(direita[j])
            inversoes += len(esquerda) - i
            j += 1
    
    intercalado.extend(esquerda[i:])
    intercalado.extend(direita[j:])
    
    return intercalado, inversoes

def contar_inversoes(lista):
    _, inversoes = merge_sort_contagem_inversoes(lista)
    print(f'total de inversoes: {inversoes}')
    return inversoes
contar_inversoes(lista=[1,5,4,8,10,2,6,9,12,11,3,7])