class Node:

    label = ' '
    entrada = 0
    salida = 0
    ie = []

    def __init__(self,label):
        self.label = label

    def __init__(self,label,cape,caps, lista):
        self.label = label
        self.entrada = cape
        self.salida = caps
        self.ie = lista
        
    def __eq__(self,other):
    	return self.label == other.label

    def name(self):
        return self.label

    def setEntrada(self,newe):
        self.entrada = newe

    def setSalida(self,news):
        self.salida = news
    
    def getEdges(self):
    	return self.ie

class Edge:

    t = Node(' ')
    h = Node(' ')
	f = 0
    cap = 0
    label = ' '

    def __init__(self, tail, head,flujo, cap, label):
        self.t = tail
        self.h = head
        self.f = flujo
        self.cap = cap
        self.label = label
       
    def __eq__(self,other):
    	if(self.t == other.t and self.h == other.h and self.cap == other.cap):
    		return True
    	elif(self.t == other.h and self.h == other.t and self.cap == other.cap):
    		return True
    	else:
    		return False

    def tail(self):
        return self.t

    def head(self):
        return self.h

    def capacity(self):
        return self.cap
        
	def flujo(self):
		return self.f

    def label(self):
        return self.label

    def setCapacity(self, newcap):
        self.cap = newcap
    
    def setFlujo(self,newflujo):
    	self.f = newflujo

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
