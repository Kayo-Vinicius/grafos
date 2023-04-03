#include <stdio.h>
#include <vector>
#include <list>	
 
#define fori(i, b, n) for(int i = b; i<n; ++i)
#define inf 10000002  //colocar aqui o valor maximo dos pesos multiplicado pela quantidade maxima de arestas mais um
 
using namespace std;
 
int pesos[251][251]; //colocar a quantidade maxima de vertices mais um.
list<int> index;	//para guardar os vertices que serão visitados;
list<int>::iterator it, aux;
 
int main(){
 
	int n, m, v1, v2, peso, explorando, menor, inicio, fim, custo, vis;
 
	scanf("%d %d", &n, &m);	//para vertices de 0 a n
 
	//colocar aqui o vertice inicial e o vertice final para calcular o caminho:
	inicio = 0;
	fim = n;
 
	vector<int> adj[n+1];
	int estimativa[n+1];
	bool aberto[n+1];
 
	//abrindo os vertices e colocando a estimativa inicial infinita:
	fori(i, 0, n+1){
		estimativa[i] = inf;
		aberto[i] = true;
	}
 
	//lendo o grafo:
	fori(i, 0, m){
		scanf("%d %d %d", &v1, &v2, &peso); 
 
		pesos[v1][v2] = peso;
		pesos[v2][v1] = peso;
 
		adj[v2].push_back(v1); //guardando apenas as adjacencias
		adj[v1].push_back(v2);	//pois os pesos serao guardados apenas na matriz
	}
 
 
 
 
 
	//iniciando o dijkstra:
	estimativa[inicio] = 0;
	index.push_back(inicio);
 
	while( !index.empty()){
		//encontrando o vertice aberto com a menor estimativa:
		menor = inf;
		for( it = index.begin(); it != index.end(); ++it){
			vis = (*it);
			if(estimativa[vis] < menor){
				menor = estimativa[vis];
				explorando = vis;
				aux = it;
			}			
		}
 
		//removendo o vertice para nao ser visitado novamente e fechando-o
		index.erase(aux);
		aberto[explorando] = false;
 
 
		//atualizando a estimativa dos vertices visinhos do explorando
		fori(i, 0, int(adj[explorando].size())){
			vis = adj[explorando][i];
 
			if(aberto[vis]){
				//custo para chegar até esse vertice atravez do visitando
				custo = pesos[explorando][vis] + estimativa[explorando];
 
				//se for a primeira vez que chegou neste vertice (vizinho)
				if(estimativa[vis] == inf){
					estimativa[vis] = custo;
					index.push_back(vis);
				}
				else{//se ja tiver chegado neste vertice
					if(custo < estimativa[vis]){
						estimativa[vis] = custo;
						//printf("Estimativa do vertice %d foi alterada para %d precedente é %d\n", j, estimativa[j], explorando);
					}
				}
			}
		}
	}
 
 
 
 
	//imprimindo o resultado:
	if(estimativa[fim] == inf){
		printf("NO\n");	//informar que o vertice inicial nao chega no final
	}
	else{
		printf("%d\n", estimativa[fim]);
	}
 
	index.clear();
 
}