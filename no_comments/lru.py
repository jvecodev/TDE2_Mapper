def algoritmo_lru(sequencia_paginas, num_quadros, pagina_alvo):

    quadros = []
    uso_recente = {}

    for tempo, pagina in enumerate(sequencia_paginas):
        if pagina in quadros:
            uso_recente[pagina] = tempo
        else:
            if len(quadros) < num_quadros:
                quadros.append(pagina)
                uso_recente[pagina] = tempo
            else:
                pagina_lru = min(uso_recente, key=uso_recente.get)
                indice_substituicao = quadros.index(pagina_lru)
                quadros[indice_substituicao] = pagina
                del uso_recente[pagina_lru] 
                uso_recente[pagina] = tempo

    try:
        indice = quadros.index(pagina_alvo)
        quadro_final = indice + 1
        return f"Para a sequência fornecida, a página {pagina_alvo} se encontra no Quadro {quadro_final}."
    except ValueError:
        return f"Ao final, a página {pagina_alvo} não estava na memória."


sequencia_a = [4, 3, 25, 8, 19, 6, 25, 8, 16, 35, 45, 22, 8, 3, 16, 25, 7]
sequencia_b = [4, 5, 7, 9, 46, 45, 14, 4, 64, 7, 65, 2, 1, 6, 8, 45, 14, 11]
sequencia_c = [4, 6, 7, 8, 1, 6, 10, 15, 16, 4, 2, 1, 4, 6, 12, 15, 16, 11]

quadros_memoria = 8

resultado_a = algoritmo_lru(sequencia_a, quadros_memoria, 7)
print(f"Resultado da Sequência A: {resultado_a}")

resultado_b = algoritmo_lru(sequencia_b, quadros_memoria, 11)
print(f"Resultado da Sequência B: {resultado_b}")

resultado_c = algoritmo_lru(sequencia_c, quadros_memoria, 11)
print(f"Resultado da Sequência C: {resultado_c}")
