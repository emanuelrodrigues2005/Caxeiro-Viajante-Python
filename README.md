# Caxeiro-Viajante-Python

## Sobre o Projeto

Este repositório contém a implementação em Python de duas abordagens para solucionar o Problema do Caixeiro Viajante (PCV), um famoso problema de otimização na ciência da computação. O objetivo é encontrar a rota mais curta possível que visita um conjunto de cidades e retorna à cidade de origem.

As duas abordagens implementadas são:

* **Algoritmo de Backtracking:** Uma solução de força bruta otimizada que garante encontrar a melhor rota possível.
* **Algoritmo Guloso (Vizinho Mais Próximo):** Uma heurística que encontra uma solução aproximada de forma muito mais rápida.

O código serve como um material de estudo e comparação entre um método exato e um método heurístico, demonstrando o trade-off entre a qualidade da solução e o tempo de execução.

## Algoritmos Implementados

### 1. Backtracking (`src/backtracking_approach.py`)

A abordagem de backtracking explora recursivamente todas as rotas possíveis. Para otimizar a busca, a implementação utiliza uma técnica de "poda": se o custo de uma rota parcial já é maior que o menor custo encontrado até o momento, esse caminho é abandonado, evitando a exploração de ramos заведомо subótimos da árvore de busca.

**Características:**
* **Garantia de Otimalidade:** Sempre encontrará a rota com o menor custo.
* **Alto Custo Computacional:** O tempo de execução é fatorial (O(n!)), tornando-o impraticável para um número elevado de cidades.

### 2. Algoritmo Guloso (`src/greedy_approach.py`)

Esta abordagem, também conhecida como heurística do "vizinho mais próximo", constrói a rota de forma incremental. A partir de uma cidade inicial, o algoritmo sempre escolhe se mover para a cidade mais próxima que ainda não foi visitada. O processo se repete até que todas as cidades tenham sido percorridas, e então retorna à cidade inicial.

**Características:**
* **Rapidez:** É uma solução muito rápida, com complexidade de tempo O(n²), sendo viável para um grande número de cidades.
* **Solução Aproximada:** Não há garantia de que a rota encontrada seja a ótima. A qualidade da solução depende fortemente da cidade de partida e da disposição das distâncias.

## Como Utilizar

### Pré-requisitos

* Python 3.x

### Executando os Algoritmos

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/emanuelrodrigues2005/caxeiro-viajante-python.git](https://github.com/emanuelrodrigues2005/caxeiro-viajante-python.git)
    cd caxeiro-viajante-python/src
    ```

2.  **Para usar a abordagem de Backtracking:**
    * Importe a classe `BacktrackingPCV` do arquivo `backtracking_approach.py`.
    * Crie uma instância da classe, passando a matriz de distâncias.
    * Chame o método `busca_solucao_otimo()` para encontrar a melhor rota e seu custo.

    ```python
    # Exemplo de uso do Backtracking
    from backtracking_approach import BacktrackingPCV

    distancias = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    pcv = BacktrackingPCV(distancias)
    melhor_rota, melhor_custo = pcv.busca_solucao_otimo(cidade_inicial=0)

    print(f"Melhor rota (Backtracking): {melhor_rota}")
    print(f"Custo total: {melhor_custo}")
    ```

3.  **Para usar a abordagem Gulosa:**
    * Importe a função `encontrar_rota_vizinho_mais_proximo` do arquivo `greedy_approach.py`.
    * Chame a função passando a matriz de distâncias e, opcionalmente, a cidade inicial.

    ```python
    # Exemplo de uso do Algoritmo Guloso
    from greedy_approach import encontrar_rota_vizinho_mais_proximo

    distancias = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    rota, custo = encontrar_rota_vizinho_mais_proximo(distancias, cidade_inicial=0)

    print(f"Rota encontrada (Guloso): {rota}")
    print(f"Custo total: {custo}")
    ```

## Estrutura do Projeto
