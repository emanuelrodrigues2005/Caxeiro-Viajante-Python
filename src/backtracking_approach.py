class BacktrackingPCV:
    def __init__(self, matriz_distancias):
        self.distancias = matriz_distancias
        self.n = len(matriz_distancias)
        self.melhor_custo = float('inf')
        self.melhor_rota = []
        
    def busca_solucao_otimo(self, cidade_inicial=0):
        self.melhor_custo = float('inf')
        self.melhor_rota = []
        
        visitado = [False] * self.n
        rota_parcial = []
        
        visitado[cidade_inicial] = True
        rota_parcial.append(cidade_inicial)
        
        self.backtracking(cidade_inicial, 1, 0, rota_parcial, visitado)
        
        return self.melhor_rota, self.melhor_custo
    
    def backtracking(self, cidade_atual, num_cidades_visitadas, custo_parcial, rota_parcial, visitado):
        if num_cidades_visitadas == self.n:
            custo_retorno = self.distancias[cidade_atual][rota_parcial[0]]
            
            if custo_retorno > 0:
                custo_final = custo_parcial + custo_retorno
                
                if custo_final < self.melhor_custo:
                    self.melhor_custo = custo_final
                    self.melhor_rota = rota_parcial + [rota_parcial[0]]
            return
        
        for proxima_cidade in range(self.n):
            if not visitado[proxima_cidade] and self.distancias[cidade_atual][proxima_cidade] > 0:
                custo_potencial = custo_parcial + self.distancias[cidade_atual][proxima_cidade]
                
                if custo_potencial >= self.melhor_custo:
                    continue
                
                visitado[proxima_cidade] = True
                rota_parcial.append(proxima_cidade)
                
                self.backtracking(
                    proxima_cidade, 
                    num_cidades_visitadas + 1, 
                    custo_potencial, 
                    rota_parcial, 
                    visitado
                )
                
                rota_parcial.pop()
                visitado[proxima_cidade] = False