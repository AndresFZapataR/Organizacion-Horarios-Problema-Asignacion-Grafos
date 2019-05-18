from clases import *

def delete(horarios):
    aux = []
    for i in horarios:
        if(i != ''):
            aux.append(i)
    horarios = aux
    i = 0
    while(i < len(horarios) -1):
        hora1 = horarios[i].split(" ")
        for k in range(len(hora1)):
                hora1[k] = hora1[k].split("-")
        j = i + 1
        print(hora1)
        while(j < len(horarios)):
            
            hora2 = horarios[j].split(" ")
            delete = False
            for k in range(len(hora2)):
                hora2[k] = hora2[k].split("-")
            print(hora2)
            if (len(hora1) >= len(hora2)):
                for k in hora1:
                    ini = int(k[1])
                    fin = int(k[2])
                    for z in hora2:
                        if(k[0] == z[0] and not delete):
                            if(int(z[1]) in range(ini,fin) or int(z[2]) in range(ini+1,fin+1)):
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
                            if(int(z[1]) in range(ini,fin) or int(z[2]) in range(ini+1,fin+1)):
                                horarios.pop(i)
                                i = i - 1
                                j = j - 1
                                delete = True

            j = j + 1
        i = i + 1

                
    print("delete finalizado")                          
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
        file = open("Asignaturas\\" + nombre + ".txt", "r")
        horas = []
        for j in file:
            horas.append(j[0:len(j)-1])
        aux = []
        for x in horas:
            if(x != ''):
                aux.append(x)
            horas = aux
        indice = 0
        
        for j in range(len(horas)):
            horas1 = horas[j].split(" ")
            for k in range(len(horas1)):
                horas1[k] = horas1[k].split("-")
            for k in range(len(asignaturas),len(nodes)-2):
                horas2 = nodes[k].getName().split(" ")
                for l in range(len(horas2)):
                    horas2[l] = horas2[l].split("-")

                if(len(horas1) >= len(horas2)):
                    for x in horas1:
                        ini = int(x[1])
                        fin = int(x[2])
                        for h in horas2:
                            if(x[0] == h[0]):
                                if(int(h[1]) in range(ini,fin) or int(h[2]) in range(ini+1,fin+1)):
                                    indice = k
                else:
                    for x in horas2:
                        ini = int(x[1])
                        fin = int(x[2])
                        for h in horas1:
                            if(x[0] == h[0]):
                                if(int(h[1]) in range(ini,fin) or int(h[2]) in range(ini+1,fin+1)):
                                    indice = k
            
            if(indice != 0):
                edges.append(Edge(nodes[i],nodes[indice],0))
                edges.append(Edge(nodes[indice],nodes[i],1))

    for i in range(len(asignaturas)):
        edges.append(Edge(nodes[len(nodes)-2],nodes[i],0))
        edges.append(Edge(nodes[i],nodes[len(nodes)-2],1))

    for i in range(len(asignaturas),len(nodes)-2):
        edges.append(Edge(nodes[i],nodes[len(nodes)-1],0))
        edges.append(Edge(nodes[len(nodes)-1],nodes[i],1))

    return edges

def Horario(lista):
    asig = []
    hora = []
    
    for i in lista:
        asig.append(i.getTail().getName())
        hora.append(i.getHead().getName())

    for i in range(len(asig)):
        h = []
        file = open("Asignaturas\\" + asig[i] +".txt", "r")
        for j in file:
            h.append(j[0:len(j)-1])
        aux = []
        for j in h:
            if(j == ''):
                aux.append(j)
        h = aux
        print("lectura")
        eq = False  
        for j in h:
            if(hora[i] == j):
                eq = True
            elif(not eq):
                horas1 = hora[i].split(" ")
                for k in range(len(horas1)):
                    horas1[k] = horas1[k].split("-")
                horas2 = j.split(" ")
                for k in range(len(horas2)):
                    horas2[k]= horas2[k].split("-")
                    
                if(len(horas1) >= len(horas2)):
                    for k in horas1:
                        ini = int(k[1])
                        fin = int(k[2])
                        for x in horas2:
                            if(k[0] == x[0]):
                                if(int(x[1]) in range(ini,fin) or int(x[2]) in range(ini+1,fin+1)):
                                    hora[i] = j
                else:
                    for k in horas2:
                        ini = int(k[1])
                        fin = int(k[2])
                        for x in horas1:
                            if(k[0] == x[0]):
                                if(int(x[1]) in range(ini,fin) or int(x[2]) in range(ini+1,fin+1)):
                                    hora[i] = j
    print("return")
    return (asig,hora)
"""                
file = open("Estudiantes\\Sara.txt", "r")
asignaturas = []
for i in file:
    asignaturas.append(i[0:len(i)-1])
horas = []
for i in range(len(asignaturas)):
    nombre = asignaturas[i]
    arch = open("Asignaturas\\" + nombre+".txt", "r")
    
    for j in arch:
        horas.append(j[0:len(j)-1])

horario = delete(horas)

nodos = initNodes(asignaturas, horario)

aristas = initEdges(nodos, asignaturas, horario)


for i in aristas:
    print(i)
"""
