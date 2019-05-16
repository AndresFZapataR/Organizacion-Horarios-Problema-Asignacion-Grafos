from clases import *

def delete(horarios):
    for i in range(len(horarios) - 1):
        for j in range(i+1,len(horarios)):
        
            hora1 = horarios[i].split(" ")
            hora2 = horarios[j].split(" ")
            delete = False
        
            for k in range(len(hora1)):
                hora1[k] = hora1[k].split("-")
            
            for k in range(len(hora2)):
                hora2[k] = hora2[k].split("-")
            
            if (len(hora1) >= len(hora2)):
                for k in hora1:
                    ini = int(k[1])
                    fin = int(k[2])
                    for z in hora2:
                        if(k[0] == z[0] and not delete):
                            if(int(z[1]) in range(ini,fin+1) or int(z[2]) in range(ini+1,fin+1)):
                                horarios.pop(j)
                                if(j != i+1):
                                    j = j - 1
                                delete = True
                                
            else:
                for k in hora2:
                    ini = int(k[1])
                    fin = int(k[2])
                    for z in hora1:
                        if(k[0] == z[0] and not delete):
                            if(int(z[1]) in range(ini,fin+1) or int(z[2]) in range(ini+1,fin+1)):
                                horarios.pop(i)
                                j = j - 1
                                i = i - 1
                                delete = True
    return horarios


def initNodes(asignaturas, horarios):
    N = []
    for i in asignaturas:
        N.append(Node(i, "A"))
    for i in horarios:
        N.append(Node(i, "H"))

    N.append(Node("s", "S"))
    N.append(Node("t","T"))
    
    return N

def initEdges(nodes, asignaturas, horarios):

    edges = []
    for i in range(len(asignaturas)):
        nombre = nodes[i].getName()
        file = open("Asignaturas\\" +nombre + ".txt", "r")
        horas = []
        for j in file:
            horas.append(j[0:len(j)-1])
            
        indice = 0
        

        for j in horas:
            horas1 = j.split(" ")
            for k in range(len(horas1)):
                horas1[k] = horas1[k].split("-")

            for k in range(len(asignaturas)+1,len(nodes)-2):
                horas2 = nodes[k].getName.split(" ")
                for l in range(len(horas2)):
                    horas[l] = horas[l].split("-")

            if(len(horas1) >= len(horas2)):
                for k in horas1:
                    ini = int(k[1])
                    fin = int(k[2])
                    for h in horas2:
                        if(k[0] == h[0]):
                            if(int(h[1]) in range(ini,fin+1) or int(h[2]) in range(ini+1,fin+1)):
                                indice = k
            else:
                for k in horas2:
                    ini = int(k[1])
                    fin = int(k[2])
                    for h in horas1:
                        if(k[0] == h[0]):
                            if(int(h[1]) in range(ini,fin+1) or int(h[2]) in range(ini+1,fin+1)):
                                indice = k
            
            if(indece != 0):
                edges.append(Edge(nodes[i],nodes[indice],0,1))

    for i in len(asignaturas):
        edges.append(Edge(Nodes[len(nodes)-2],Node[i],0,1))

    for i in len(horarios):
        edges.append(Edge(Nodes[len(asignaturas)+ 1 + i],Nodes[len(nodes)-1],0,1))

    return edges


        
        
                    
file = open("Estudiantes\\Sara.txt", "r")
asignaturas = []
for i in file:
    asignaturas.append(i[0:len(i)-1])

for i in range(len(asignaturas)):
    arch = open("Asignaturas
        
            
            
    





















    
    
