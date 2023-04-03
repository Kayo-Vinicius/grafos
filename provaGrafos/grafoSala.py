from grafo import GrafoListaAdj
from centroArvore import CentroArvore

G = GrafoListaAdj(orientado=False)

G.DefinirN(5, VizinhancaDuplamenteLigada=True)
e = G.AdicionarAresta(1, 2)
#e.custo = 3
#e = G.AdicionarAresta(1, 3)
#e.custo = 1
e = G.AdicionarAresta(1, 3)
#e.custo = 2
e = G.AdicionarAresta(1, 4)
e = G.AdicionarAresta(1, 5)

#e.custo = 4

"""
for V in G.V():
    for no in G.N(V, IterarSobreNo = True):
        u = no.Viz
        print((V, u), no.e.custo)
"""
c = CentroArvore(G)
print(c)
