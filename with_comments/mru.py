def algoritmo_mru(sequencia_paginas, num_quadros, pagina_alvo):
    """
    Simula o algoritmo MRU (Most Recently Used) silenciosamente e retorna
    a posição final de uma página específica.

    Args:
        sequencia_paginas (list): A lista de páginas a serem acessadas.
        num_quadros (int): O número de quadros disponíveis na memória.
        pagina_alvo (int): A página cuja posição final queremos encontrar.
    
    Returns:
        str: Uma string informando a posição final da página alvo.
    """
    quadros = []  # Lista que armazenará as páginas atualmente na memória
    uso_recente = {}  # Dicionário para registrar o último uso de cada página

    for tempo, pagina in enumerate(sequencia_paginas):
        # Caso a página já esteja na memória, atualiza seu tempo de uso
        if pagina in quadros:
            uso_recente[pagina] = tempo
        else:
            # Caso ainda haja espaço disponível
            if len(quadros) < num_quadros:
                quadros.append(pagina)
                uso_recente[pagina] = tempo
            else:
                # Encontra a página mais recentemente usada
                pagina_mru = max(uso_recente, key=uso_recente.get)
                indice_substituicao = quadros.index(pagina_mru)

                # Substitui a página antiga pela nova
                quadros[indice_substituicao] = pagina

                # Atualiza os registros de uso
                del uso_recente[pagina_mru]
                uso_recente[pagina] = tempo
    # --- Fim da Simulação ---

    # Tenta encontrar a página alvo na lista final de quadros
    try:
        indice = quadros.index(pagina_alvo)
        quadro_final = indice + 1
        return f"Para a sequência fornecida, a página {pagina_alvo} se encontra no Quadro {quadro_final}."
    except ValueError:
        return f"Ao final, a página {pagina_alvo} não estava na memória."


# --- Definição das Sequências e Parâmetros ---
sequencia_a = [4, 3, 25, 8, 19, 6, 25, 8, 16, 35, 45, 22, 8, 3, 16, 25, 7]
sequencia_b = [4, 5, 7, 9, 46, 45, 14, 4, 64, 7, 65, 2, 1, 6, 8, 45, 14, 11]
sequencia_c = [4, 6, 7, 8, 1, 6, 10, 15, 16, 4, 2, 1, 4, 6, 12, 15, 16, 11]

quadros_memoria = 8

resultado_a = algoritmo_mru(sequencia_a, quadros_memoria, 7)
print(f"Resultado da Sequência A: {resultado_a}")

resultado_b = algoritmo_mru(sequencia_b, quadros_memoria, 11)
print(f"Resultado da Sequência B: {resultado_b}")

resultado_c = algoritmo_mru(sequencia_c, quadros_memoria, 11)
print(f"Resultado da Sequência C: {resultado_c}")
