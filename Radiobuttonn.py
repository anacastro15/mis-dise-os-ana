from tkinter import *

def seleccionar():
    monitor.config(text="{}".format(opcion.get()))

def reset():
    opcion.set(None)        #reiniciar el selecionable
    monitor.config(text="")   #reiniciamos la etiqueta

root = Tk() 
root.config(bd=50)

opcion = IntVar()

Radiobutton(root, text="opcion 1", variable=opcion, 
            value=1, command=seleccionar).pack()
Radiobutton(root, text="opcion 2", variable=opcion, 
            value=2, command=seleccionar).pack()
Radiobutton(root, text="opcion 3", variable=opcion,   
            value=3, command=seleccionar).pack()
Radiobutton(root, text="opcion 4", variable=opcion,   
            value=4, command=seleccionar).pack()

monitor = Label(root)
monitor.pack()

Button(root, text="Reiniciar", command=reset).pack()

# Finalmente bucle de la aplicación
root.mainloop()