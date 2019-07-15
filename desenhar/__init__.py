from turtle import *
from time import *
from random import *

class Desenhar:
    def __init__(self):
        self.janela = Screen()
        self.caneta = Pen()
        self.janela.onclick(self.escreve)
        

    def desenharVertices(self, grafos):
        for grafo in grafos:
            self.caneta.penup()
            self.caneta.goto(grafo['vertice'])
            self.caneta.pendown()
            self.caneta.circle(5)
            sleep(1)
        self.janela.exitonclick()

    def desenharVerticesArestas(self, grafos):
        for grafo in grafos:
            self.caneta.color(
                choice(['black', 'red','blue', 'green', 'orange', 'yellow'])
            )
            self.caneta.penup()
            self.caneta.goto(grafo['vertice'])
            self.caneta.pendown()
            self.caneta.begin_fill()
            self.caneta.circle(5)
            self.caneta.end_fill()
            self.escreve()
            sleep(0.5)
            for aresta in grafo['aresta']:
                self.caneta.pendown()
                self.caneta.color('gray')
                self.caneta.goto(aresta)
                self.caneta.penup()
                self.caneta.goto(grafo['vertice'])
                sleep(0.5)
        
        
        self.janela.exitonclick()
    
    def escreve(self):
        print(self.caneta.pos())

    def desenharArestas(self, grafos):
        for grafo in grafos:
            for aresta in grafo['aresta']:
                self.caneta.penup()
                self.caneta.goto(aresta)
                self.caneta.pendown()
                
                self.caneta.right(90)
                self.caneta.forward(10)

                self.caneta.right(120)
                self.caneta.forward(10)

                self.caneta.right(120)
                self.caneta.forward(10)

                sleep(1)
        self.janela.exitonclick()
    