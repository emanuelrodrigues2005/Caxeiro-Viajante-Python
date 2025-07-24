def encontrar_rota_vizinho_mais_proximo(matriz_adjacencia, cidade_inicial=0):
    num_cidades = len(matriz_adjacencia)

    if not matriz_adjacencia or num_cidades == 0:
        print("Erro: A matriz de adjacência não pode estar vazia.")
        return None, -1

    if not all(len(linha) == num_cidades for linha in matriz_adjacencia):
        print("Erro: A matriz de adjacência deve ser quadrada.")
        return None, -1

    if not (0 <= cidade_inicial < num_cidades):
        print(f"Erro: A cidade inicial '{cidade_inicial}' é inválida.")
        return None, -1

    rota = [cidade_inicial]
    cidades_visitadas = {cidade_inicial}
    custo_total = 0.0
    cidade_atual = cidade_inicial

    if num_cidades == 1:
        rota.append(cidade_inicial)
        return rota, 0.0

    while len(cidades_visitadas) < num_cidades:
        distancia_minima = float('inf')
        proxima_cidade = None

        for vizinha in range(num_cidades):
            if vizinha not in cidades_visitadas:
                distancia = matriz_adjacencia[cidade_atual][vizinha]
                if distancia < distancia_minima:
                    distancia_minima = distancia
                    proxima_cidade = vizinha
        
        if proxima_cidade is None:
            print("Erro: Grafo desconexo. Não é possível visitar todas as cidades.")
            return None, -1

        cidade_atual = proxima_cidade
        cidades_visitadas.add(cidade_atual)
        rota.append(cidade_atual)
        custo_total += distancia_minima

    custo_total += matriz_adjacencia[cidade_atual][cidade_inicial]
    rota.append(cidade_inicial)

    return rota, custo_total


if __name__ == "__main__":
    distancias_principais = [
        # A,  B,   C,   D,   E
        [0,  10,  15,  20,  30],  # A
        [10, 0,   35,  25,  5],   # B
        [15, 35,  0,   30,  20],  # C
        [20, 25,  30,  0,   10],  # D
        [30, 5,   20,  10,  0]   # E
    ]
    nomes_cidades = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}
    
    # Teste 1: Iterar sobre todas as cidades iniciais possíveis
    print("\nTeste 1")
    for i, nome in nomes_cidades.items():
        print(f"\nRota a partir da cidade '{nome}'")
        rota_indices, custo = encontrar_rota_vizinho_mais_proximo(distancias_principais, cidade_inicial=i)
        if rota_indices:
            rota_nomes = ' -> '.join([nomes_cidades[idx] for idx in rota_indices])
            print(f"  Rota encontrada: {rota_nomes}")
            print(f"  Custo total: {custo}")
