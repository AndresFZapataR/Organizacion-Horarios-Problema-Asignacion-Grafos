#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun May 12 12:15:27 2019

@author: Sara Palacios & Andrés Zapata
"""
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
        return self.label + str(self.getFlow())
       
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
            if(e.getTail() == i.getHead() and e.getHead() == i.getTail()):
                return i
        return None
    
    def hgetPath(self,u,v,p,used):
        if(u == v):
            return p
        else:
            for i in self.getEdges():
                if(i.getTail() == u and i not in used and i.getFlow() == 0):
                    p.append(i)
                    used.append(i)
                    return self.hgetPath(i.getHead(),v,p,used)
            t = p[len(p)-1].getTail()
            p = p[0:len(p)-1]
            return self.hgetPath(t,v,p,used)

    def getPath(self,u,v):
        return self.hgetPath(u,v,[],[])

    def hcut(self,u,v,p,used):
        if(u == v):
            return False
        else:
            for i in self.getEdges():
                if(i.getTail() == u and i not in used and i.getFlow() == 0):
                    p.append(i)
                    used.append(i)
                    return self.hcut(i.getHead(),v,p,used)
            
            if(len(p) == 0):
                return True
            else:
                t = p[len(p)-1].getTail()
                p = p[0:len(p)-1]
                return self.hcut(t,v,p,used)

    def cut(self,u,v):
        return self.hcut(u,v,[],[])

    def ford_fulkerson(self,s,t):

        while(not self.cut(s,t)):
            print("si hay p")
            for i in self.getPath(s,t):
                i.setFlow(1)
                (self.getRev(i)).setFlow(0)

    def getHorario(self):
        H = []
        for i in self.getEdges():
            if(i.getFlow() == 1 and (i.getTail()).getLabel() == "A" and (i.getHead().getLabel() == "H")):
                H.append(i)
        return H
                    
