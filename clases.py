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
    flow = 0
    label = ""

    def __init__(self, tail, head, flow):
        self.tail = tail
        self.head = head
        self.flow = flow
        self.label = "(" + tail.getName() + "," + head.getName() + ")"
        
    def __str__(self):
        return self.label
       
    def __eq__(self,other):
    	if(self.tail == other.tail and self.head == other.head):
    		return True
    	else:
    		return False

    def getTail(self):
        return self.tail

    def getHead(self):
        return self.head
        
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

    def getRev(self,e):
        for i in self.getEdges():
            if(e.tail() == i.head() and e.head() == i.tail()):
                return i
        return None
    
    def hgetPath(self,u,v,p,used):
        if(u == v):
            return p
        else:
            for i in self.getEdges():
                if(i.getTail() == u and i.getHead() not in used and i.getFlow() != 0):
                    p.append(i)
                    used.append(i)
                    return hgetPath(self,i.getHead(),v,p)
            
            t = p[len(p)]
            p = p[0:len(p)-1]
            return hgetPath(self,t,v,p,used)

    def getPath(self,u,v):
        return hgetPath(self,u,v,[],[])

    def hcut(self,u,v,p,used):
        if(u == v):
            return False
        else:
            for i in self.getEdges():
                if(i.getTail() == u and i.getHead() not in used and i.getFlow() != 0):
                    p.append(i)
                    used.append(i)
                    return hcut(self,u,v,p,used)
            
            if(len(p) == 0):
                return True
            else:
                t = p[len(p)]
                p = p[0:len(p)-1]
                return hcut(self,u,v,p,used)

    def cut(self,u,v):
        return hcut(self,u,v,[],[])

    def ford_fulkerson(self,s,t):

        while(cut(self,s,t)):
            for i in getPath(self,s,t):
                i.setFlow(1)
                self.getRev(i).setFlow(0)

    def getHorario(self):
        H = []
        for i in self.getEdges():
            if(i.getFlow() == 1 and i.tail().getLabel() == "M"):
                H.append(i)
        return H
                    
