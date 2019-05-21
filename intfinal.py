#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 08:31:55 2019

@author: Sara Palacios & Andrés Zapata
"""
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from clases import *
import funciones as f

materias=[]
materiasf=[]

def registro():
    name = []
    def GuardarNombre(entradas, asigs, lb):
        
        def CrearArchivo(archivo, asigs, lb): 
            selecl = lb.curselection()
            asig = asigs[selecl[0]]
            materias.append(asig)
            lb.delete(selecl[0])
            asigs.pop(selecl[0])
            but5=tk.Button(wn2, text="Finalizar", font=("Century Gothic", 8),
                           command=lambda:AgregarAsignatura(materias, estudiante))
            but5.grid(column=1, row=9, sticky="W")

        def AgregarAsignatura(lista, archivo):
            for i in range(len(lista)):
                archivo.write(lista[i])
                archivo.write("\n")
            archivo.close()
        
            wn2.iconify()
            wn.deiconify()
            
        for i in range(len(entradas)):
            name.append(str(entradas[i].get()))
        for i in name:
            if i== "NA":
                name.remove(i)
        fullname="_".join(name)
        estudiante= open(fullname + ".txt", "w")
        but4=tk.Button(wn2, text="Guargar Asignatura", font=("Century Gothic", 8),
                       command=lambda:CrearArchivo( estudiante, asigs, lb))
        but4.grid(column=1, row=7, sticky="W")
    wn2=tk.Toplevel(wn)
    wn.iconify()
    wn2.title("Registro")
    wn2.geometry("500x500")
    
    #--------Labels--------
    lb3 = tk.Label(wn2, text= "Necesitamos su información para crear su horario",
                   font=("Century Gothic", 11))
    lb3.grid(column=0, row=0, sticky="W")
    lb4 = tk.Label(wn2, text= "Primer Nombre: ",
                   font=("Century Gothic", 11))
    lb4.grid(column=0, row=1, sticky="W", pady=10)
    lb5 = tk.Label(wn2, text= "Segundo Nombre: ",
                   font=("Century Gothic", 11))
    lb5.grid(column=0, row=1, sticky="E")
    lbe5 = tk.Label(wn2, text= "Si no tiene segundo nombre escriba NA",
                   font=("Century Gothic", 7))
    lbe5.grid(column=0, row=4, sticky="E")
    lb6 = tk.Label(wn2, text= "Primer Apellido: ",
                   font=("Century Gothic", 11))
    lb6.grid(column=0, row=3, sticky="W", pady=10)
    lb7 = tk.Label(wn2, text= "Segundo Apellido: ",
                   font=("Century Gothic", 11))
    lb7.grid(column=0, row=3, sticky="E", pady=10)
    lb8 = tk.Label(wn2, text= "Asignaturas disponibles para el registro:*  ",
                   font=("Century Gothic", 11))
    lb8.grid(column=0, row=5, sticky="W", pady=10)
    lb9 = tk.Label(wn2, text= "*Tenga en cuenta que son solo asignaturas MACC",
                   font=("Century Gothic", 7))
    lb9.grid(column=0, row=6, sticky="W")
    lb10 = tk.Label(wn2, text= "*Debe guardar una por una",
                   font=("Century Gothic", 7))
    lb10.grid(column=1, row=7, sticky="s", pady=50)
    
    #--------Entrys--------
    ent1=tk.Entry(wn2, width=15)
    ent1.grid(column=0, row=1,sticky="W", pady=10, padx= 120)
    ent2=tk.Entry(wn2, width=15)
    ent2.grid(column=1, row=1,sticky="W", pady=10)
    ent3=tk.Entry(wn2, width=15)
    ent3.grid(column=0, row=3,sticky="W", pady=10, padx= 120)
    ent4=tk.Entry(wn2, width=15)
    ent4.grid(column=1, row=3,sticky="W", pady=10)
    entradas=[ent1, ent2, ent3, ent4]
    
    #------ListBox-----
    asig=[]
    file = open("Asignaturas_MACC.txt", "r")
    for i in file:
        asig.append(i[0:len(i)-1])
    lista = tk.Listbox(wn2, selectmode=tk.EXTENDED, width=40)
    lista.grid(column=0, row=7)
    for i in range(len(asig)):
        lista.insert(tk.END,asig[i])

    
   
    #---------Botones-------
    but3=tk.Button(wn2, text="Guardar Nombre", font=("Century Gothic", 8),
                   command=lambda:GuardarNombre(entradas, asig, lista))
    but3.grid(column=1, row=4,sticky="W", pady=10)

def GenerarHorario():
    def seleccion(lb, asigs, ent,wn):
        sell = lb.curselection()
        asig = asigs[sell[0]]
        materiasf.append(asig)
        lb.delete(sell[0])
        asigs.pop(sell[0])
        cant = int(ent.get())
        if cant == len(materiasf):
            wn.iconify()
            horarios = []
            for i in materiasf:
                file = open("Asignaturas\\" + i + ".txt", "r")
                hora = []
                for j in file:
                    hora.append(j[0:len(j)-1])
                
                for j in hora:
                    if(j != ''):
                        horarios.append(j)
            horarios = f.delete(horarios)
            nodes = f.initNodes(materiasf,horarios)
            edges = f.initEdges(nodes,materiasf,horarios)
            G = Graph(nodes,edges)
            G.ford_fulkerson(nodes[len(nodes)-2],nodes[len(nodes)-1])
            H = G.getHorario()
            final = f.Horario(H)
            asignaturas = final[0]
            horario = final[1]
            clases = []
            for i in range(len(asignaturas)):
                clases.append(asignaturas[i].replace("_", " "))
            wn = tk.Tk()
            wn.title("Horario")
            wn.geometry("500x250")
            texto = tk.Text(wn)
            texto.grid()
            texto.insert(tk.END, "Su horario sin horas cruzadas es: ")
            texto.insert(tk.END, "\n")
            for i in range(len(clases)):
                texto.insert(tk.END, "{0}: {1}".format(clases[i],horario[i]))
                texto.insert(tk.END, "\n")
            texto.config(state="disabled")
            
    
    def asigs(entrada, wn):
        asignaturas=[]
        main = tk.Tk()
        main.geometry("500x500")
        main.title("Seleccion de asignaturas")
        #------Label-----
        label2 = tk.Label(main,
                          text="Por favor indique las asignaturas que desea inscribir",
                          font=("Century Gothic", 10))
        label2.grid(column=0, row=2)
        label3 = tk.Label(main,text="¿Cuantas asignaturas desea inscribir?",
                          font=("Century Gothic", 10))
        label3.grid(column=0, row=0)
        #------Entrada-------
        cantidad = tk.Entry(main)
        cantidad.grid(column=1, row=0)
        name = entrada.get()
        nombre=name.replace(" ", "_")
        file = open(nombre + ".txt", "r")
        for i in file:
            asignaturas.append(i[0:len(i)-1])
        lista = tk.Listbox(main, selectmode=tk.EXTENDED, width=40)
        lista.grid(column=0, row=3)
        for i in range(len(asignaturas)):
            lista.insert(tk.END,asignaturas[i])
        
        bot3 = tk.Button(main, text="Seleccionar", font=("Century Gothic", 10),
                         command = lambda:seleccion(lista, asignaturas, cantidad, main) )
        bot3.grid(column=1, row= 3)
        wn.iconify()
        
    root = tk.Tk()
    root.title("Generador de horarios")
    root.geometry("400x150")
    #------Labels-----
    l = tk.Label(root, text= "Ahora, crearemos su horario ",
                      font=("Century Gothic", 10))
    l.grid(column=0, row=0)
    label1 = tk.Label(root, text= "Ingrese su nombre completo: ",
                      font=("Century Gothic", 10))
    label1.grid(column=0, row=1)
    #----Entrada-----
    nombre = tk.Entry(root)
    nombre.grid(column=1, row=1)
    #-----Boton----
    bot = tk.Button(root, text="Siguiente",font=("Century Gothic", 8),
                    command=lambda:asigs(nombre, root))
    bot.grid(column=0, row=2)
    wn.iconify()
    
    
    
                   
    


wn = tk.Tk()
wn.title("Inicio")
wn.geometry("500x250")

#--------Labels--------
lb = tk.Label(wn, text= "Bienvenido")
lb.grid(column=0, row=0, sticky="W")
lb.config(font=("Century Gothic", 11))

lb2 = tk.Label(wn, text= "Por favor indique lo que desea hacer: ")
lb2.grid(column=0, row=1, sticky="W")
lb2.config(font=("Century Gothic", 11))
#---------Botones-------
but1 = tk.Button(wn, text="Registrarse", command=lambda: registro())
but1.grid(column=0, row=2, pady=20)
but1.config(font=("Century Gothic", 11))

but2 = tk.Button(wn, text="Generar Horario", command=lambda:GenerarHorario())
but2.grid(column=1, row=2, pady=20)
but2.config(font=("Century Gothic", 11))



            
