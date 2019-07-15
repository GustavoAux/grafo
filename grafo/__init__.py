from random import *
from desenhar import *

class Grafo:
    def __init__(self):
        self.grafos = []
        self._numero_vertices = 0
        self._numero_arestas = 0

    @property
    def numero_vertices(self):
        return self._numero_vertices

    @property
    def numero_arestas(self):
        return self._numero_arestas

    def addVertice(self, vertice):
        self.grafos.append({'vertice': vertice, 'aresta': []})
        self._numero_vertices += 1

    def addAresta(self, vertice, aresta, dirigido=False, ponderado=False):
        for grafo in self.grafos:
            if grafo['vertice'] == vertice:
                grafo['aresta'].append(aresta)
        self._numero_arestas += 1

    def mostrar(self):
        texto = ""
        for grafo in self.grafos:
            texto += str(grafo)+'\n'
        return texto
    
    def arquivo(self):
        arquivo = open('resultado', 'w+')
        for grafo in self.grafos:
            arquivo.write(str(grafo))
        arquivo.close()

    def randomizarGrafo(self):
        return choice(self.grafos)

    def desenhar(self):
        desenhar = Desenhar()
        # desenhar.desenharVertices(self.grafos)
        # desenhar.desenharArestas(self.grafos)
        desenhar.desenharVerticesArestas(self.grafos)
        