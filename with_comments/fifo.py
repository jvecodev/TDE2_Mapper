def algoritimo_fifo(sequencia_paginas, num_quadros, pagina_alvo):
    """
    Simula o algoritmo FIFO silenciosamente e retorna a posição final de uma página específica.

    Args:
        sequencia_paginas (list): A lista de páginas a serem acessadas.
        num_quadros (int): O número de quadros disponíveis na memória.
        pagina_alvo (int): A página cuja posição final queremos encontrar.
    
    Returns:
        str: Uma string informando a posição final da página alvo.
    """
    quadros = []
    ponteiro = 0

    for pagina in sequencia_paginas:
        if pagina not in quadros:
            if len(quadros) < num_quadros:
                quadros.append(pagina)
            else:
                quadros[ponteiro] = pagina
                ponteiro = (ponteiro + 1) % num_quadros
    # --- Fim da Simulação ---

    # Tenta encontrar a página alvo na lista final de quadros
    try:
        # O método .index() retorna a posição (começando em 0) da página
        indice = quadros.index(pagina_alvo)
        # Adicionamos 1 para ter o número do quadro (começando em 1)
        quadro_final = indice + 1
        return f"Para a sequência fornecida, a página {pagina_alvo} se encontra no Quadro {quadro_final}."
    except ValueError:
        # Este erro acontece se a página_alvo não for encontrada na lista final
        return f"Ao final, a página {pagina_alvo} não estava na memória."

# --- Definição das Sequências e Parâmetros ---

sequencia_a = [4, 3, 25, 8, 19, 6, 25, 8, 16, 35, 45, 22, 8, 3, 16, 25, 7]
sequencia_b = [4, 5, 7, 9, 46, 45, 14, 4, 64, 7, 65, 2, 1, 6, 8, 45, 14, 11]
sequencia_c = [4, 6, 7, 8, 1, 6, 10, 15, 16, 4, 2, 1, 4, 6, 12, 15, 16, 11]

quadros_memoria = 8

resultado_a = algoritimo_fifo(sequencia_a, quadros_memoria, 7)
print(f"Resultado da Sequência A: {resultado_a}")

resultado_b = algoritimo_fifo(sequencia_b, quadros_memoria, 11)
print(f"Resultado da Sequência B: {resultado_b}")

resultado_c = algoritimo_fifo(sequencia_c, quadros_memoria, 11)
print(f"Resultado da Sequência C: {resultado_c}")