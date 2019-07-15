from grafo import *
from random import *

grafo = Grafo()

mapa = []
for rua in range(randrange(3,4)):
    paradas = []
    if rua != 0:
        y = rua * 100
    else:
        y = rua
    for quantidade in range(-3, 4):
        if quantidade != 0:
            x = quantidade*100
        else:
            x = quantidade
        paradas.append((x, y))
    mapa.append(paradas)


print('#'*100)
for rua in mapa:
    for parada  in rua:
        print(str(parada), end=' ')
        vertice = parada
        grafo.addVertice(vertice)
    print()
print('#'*100)

cont = 0
cont_y =0
for i, ponto in enumerate(mapa):
    if i <= 0:
        cont_y = i + 1
    if i > 0:
        cont_y = i - 1
    for i, parada in enumerate(ponto):
        if i < (len(ponto) - 1):
            cont += 1

        print(parada,ponto[cont], end=' ')
        grafo.addAresta(parada, ponto[cont])
        print()
    cont = 0
    grafo.addAresta(parada, ponto[cont_y])
            


# print(grafo.mostrar())
# print(grafo.numero_vertices)
# print(grafo.numero_arestas)
grafo.desenhar()