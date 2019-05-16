class Node:
    
    name = ""
    label = ""
    
    def __init__(self,name,label):
        self.label = label
        self.name = name

    def __str__(self):
        return self.name

    def __eq__(self,other):
    	return self.name == other.name

    def getName(self):
        return self.name

    def getLabel(self):
        return self.label


class Edge:

    tail = None
    head = None
    capacity = 0
    flow = 0
    label = ""

    def __init__(self, tail, head,flow, cap):
        self.tail = tail
        self.head = head
        self.flow = flow
        self.capacity = cap
        self.label = "(" + tail.getName() + "," + head.getName() + ")"
        
    def __str__(self):
        return self.label
       
    def __eq__(self,other):
    	if(self.tail == other.tail and self.head == other.head and self.capacity == other.capacity):
    		return True
    	elif(self.tail == other.head and self.head == other.tail and self.capacity == other.capacity):
    		return True
    	else:
    		return False

    def getTail(self):
        return self.tail

    def getHead(self):
        return self.head

    def capacity(self):
        return self.capacity
        
    def getFlow(self):
        return self.flow

    def setCapacity(self, newcap):
        self.capacity = newcap
    
    def setFlow(self,newflow):
    	self.flow = newflow

class Graph:

    V = []
    E = []

    def __init__(self, nodes, edges):
        self.V = nodes
        self.E = edges

    def getNodes(self):
        return self.V

    def getEdges(self):
        return self.E
