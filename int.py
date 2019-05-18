import tkinter as tk
from tkinter import ttk
from clases import *
import funciones as f


count = 0
materias = []

def asigs(entr, wn):
    
    def num(entry):        
        count = int(entry.get())
        return count
    
    def seleccion(lb, asigs, ent):
        selecl = lb.curselection()
        asig = asigs[selecl[0]]
        materias.append(asig)
        lb.delete(selecl[0])
        asigs.pop(selecl[0])
        cant = int(ent.get())
        if cant == len(materias):
            print(materias)
            horarios = []
            for i in materias:
                file = open("Asignaturas\\" + i + ".txt", "r")
                hora = []
                for j in file:
                    hora.append(j[0:len(j)-1])
                
                for j in hora:
                    if(j != ''):
                        horarios.append(j)
            horarios = f.delete(horarios)
            print("horarios")
            for i in horarios:
                print(i)
            nodes = f.initNodes(materias,horarios)
            edges = f.initEdges(nodes,materias,horarios)
            print("nodos y aristeas")
            for i in nodes:
                print(i)
            for i in edges:
                print(i)
            G = Graph(nodes,edges)
            G.ford_fulkerson(nodes[len(nodes)-2],nodes[len(nodes)-1])
            print("G")
            for i in G.getNodes():
                print(i)
            for i in G.getEdges():
                print(i)
            H = G.getHorario()
            print("H")
            for i in H:
                print(i)
            final = f.Horario(H)
            print(final)
            wn = tk.Tk()
            wn.title("horario")
            
            
        
    main = tk.Tk()
    main.geometry("500x500")
    main.title("Seleccion de asignaturas")
    label2 = tk.Label(main,
                      text="Por favor indique las asignaturas que desea inscribir")
    label2.grid(column=0, row=2)
    asignaturas=[]
    label3 = tk.Label(main,
                      text="¿Cuantas asignaturas desea inscribir?")
    label3.grid(column=0, row=0)
    
    cantidad = tk.Entry(main)
    cantidad.grid(column=1, row=0)
    name = entr.get()
    file = open("Estudiantes\\" + name + ".txt", "r")
    for i in file:
        asignaturas.append(i[0:len(i)-1])
    lista = tk.Listbox(main, selectmode=tk.EXTENDED)
    lista.grid(column=0, row=3)
    for i in range(len(asignaturas)):
        lista.insert(tk.END,asignaturas[i])
    
    bot3 = tk.Button(main, text="Seleccionar",
                     command = lambda:seleccion(lista, asignaturas, cantidad) )
    bot3.grid(column=1, row= 3)

root = tk.Tk()
root.title("Generador de horarios")
root.geometry("300x300")

label1 = tk.Label(root, text= "Ingrese su nombre: " )
label1.grid(column=0, row=0)
nombre = tk.Entry(root)
nombre.grid(column=1, row=0)

bot = tk.Button(root, text="Siguiente", command=lambda:asigs(nombre, root))
bot.grid(column=0, row=1)

root.mainloop()
