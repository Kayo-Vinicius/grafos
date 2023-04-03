import heapq

class Grafo():
    """Define um grafo utilizando matriz de adjacências.

        Args:
            arestas (list): uma lista de listas onde o indice é o 
                            vértice e cada elemento da lista é o vizinho
    """

    def __init__(self, arestas: list):
        self.adj = [[] for _ in range(len(arestas))]
        self.dist = [99999 for _ in range(len(arestas))]
        self.adiciona_arestas(arestas)

    def adiciona_arestas(self, arestas: list) -> None:
        """Adiciona todas as arestas ao grafo

        Args:
            arestas (list): a lista contendo todas as definições de arestas do grafo
        """
        for i in range(len(arestas)):
            for j in range(len(arestas[i])):
                self.__adiciona_aresta(i, arestas[i][j])

    def __adiciona_aresta(self, u: int, v: int) -> None:
        """Adiciona a aresta na matriz de adjacência

        Args:
            u (int): vértice u
            v (int): vértice v
        """
        if v[0] not in self.adj[u]:
            self.adj[u].append([v[1], v[0]])

    def _peso_entre_u_e_v(self, u: int, v: int) -> float:
        """Retorna o peso entre os vértices u e v

        Args:
            u (int): vértice u 
            v (int): vértice v

        Returns:
            float: peso entre u e v 
        """
        for vertice in self.adj[v[1]]:
            if vertice[1] == u:
                return vertice[0]

    def dijkstra(self, start: int) -> list:
        """Retorna a lista de distância do vértice start até todos os vértices

        Args:
            start (int): vértice inicial

        Returns:
            list: lista de distâncias
        """
        distancia = self.dist.copy()
        S = set()  # Conjunto de vértices explorados
        distancia[start] = 0

        while True:
            V = set([(i, distancia[i]) for i in range(len(self.adj))])
            diferenca_de_conjuntos = list(V.difference(S))
            if not diferenca_de_conjuntos:
                break

            heapq.heapify(diferenca_de_conjuntos)
            u, distancia_u = heapq.heappop(diferenca_de_conjuntos)

            S.add((u, distancia[u]))
            for v in self.adj[u]:
                if distancia[v[1]] > distancia_u + self._peso_entre_u_e_v(u, v):
                    distancia[v[1]] = distancia_u + \
                        self._peso_entre_u_e_v(u, v)

        return distancia


arestas = [[[0, 2], [0, 4]],            # Vizinhos do vértice 0.
           [[1, 1], [1, 5], [1, 4]],                      # Vizinhos do vértice 1.
           [[2, 2], [2, 10], [2, 8], [2, 1]],  # Vizinhos do vértice 2.
           [[3, 8], [3, 5], [3, 2], [3, 6]],          # Vizinhos do vértice 3.
           [[4, 6], [4, 2]],                      # Vizinhos do vértice 4.
           [[5, 2], [5, 10], [5, 2]]                     # Vizinhos do vértice 5.
           ]

grafo = Grafo(arestas)
print(grafo.dijkstra(0))