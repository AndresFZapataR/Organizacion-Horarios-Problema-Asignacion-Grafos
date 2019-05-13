import tkinter as tk
from tkinter import ttk

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
    file = open(name + ".txt", "r")
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
