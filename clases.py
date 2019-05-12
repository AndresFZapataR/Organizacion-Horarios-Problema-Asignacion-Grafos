class Node:

    label = ' '
    entrada = 0
    salida = 0

    def __init__(self,label):
        self.label = label

    def __init__(self,label,cape,caps):
        self.label = label
        self.entrada = cape
        self.salida = caps

    def name(self):
        return self.label

    def setEntrada(self,newe):
        self.entrada = newe

    def setSalida(self,news):
        self.salida = news

class Edge:

    t = Node(' ')
    h = Node(' ')
    cap = 0
    label = ' '

    def __init__(self, tail, head, cap, label):
        self.t = tail
        self.h = head
        self.cap = cap
        self.label = label

    def tail(self):
        return self.t

    def head(self):
        return self.h

    def capacity(self):
        return self.cap

    def label(self):
        return self.label

    def setCapacity(self, newcap):
        self.cap = newcap

class Graph:

    V = []
    E = []

    def __init__(self, nodes, edges):
        self.V = nodes
        self.E = edges

    def nodes(self):
        return self.V

    def edges(self):
        return self.E
