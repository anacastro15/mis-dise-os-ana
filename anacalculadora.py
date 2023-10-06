from tkinter import*

ventana = Tk()
ventana.title("Calculadora Hexadecimal")
ventana.configure(bg='yellow')

# Entrada
e_texto = Entry(ventana, font=("Arial 35"))
e_texto.configure(bg="pink")
e_texto.grid(row=0, columnspan=4, padx=5, pady=5)

i = 0

def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1

def resultado():
    ecuacion = e_texto.get()
    resultado = eval(ecuacion)
    e_texto.delete(0, END)
    e_texto.insert(0, resultado)
    i = 0

def borrar():
    e_texto.delete(0, END)
    i = 0

def operacion():
    ecuacion = e_texto.get()
    try:
        resultado = hex(eval(ecuacion))
        e_texto.delete(0, END)
        e_texto.insert(0, resultado)
        i = 0
    except Exception as e:
        e_texto.delete(0, END)
        e_texto.insert(0, "Error")

def retroceder():
    global i
    i = i - 1
    e_texto.delete(i, END)

boton1 = Button(ventana, text="1", width=5, height=2, command=lambda: click_boton("1"), bg="sky blue")
boton2 = Button(ventana, text="2", width=5, height=2, command=lambda: click_boton("2"), bg="sky blue")
boton3 = Button(ventana, text="3", width=5, height=2, command=lambda: click_boton("3"), bg="sky blue")
boton4 = Button(ventana, text="4", width=5, height=2, command=lambda: click_boton("4"), bg="sky blue")
boton5 = Button(ventana, text="5", width=5, height=2, command=lambda: click_boton("5"), bg="sky blue")
boton6 = Button(ventana, text="6", width=5, height=2, command=lambda: click_boton("6"), bg="sky blue")
boton7 = Button(ventana, text="7", width=5, height=2, command=lambda: click_boton("7"), bg="sky blue")
boton8 = Button(ventana, text="8", width=5, height=2, command=lambda: click_boton("8"), bg="sky blue")
boton9 = Button(ventana, text="9", width=5, height=2, command=lambda: click_boton("9"), bg="sky blue")
boton0 = Button(ventana, text="0", width=5, height=2, command=lambda: click_boton("0"), bg="sky blue")
botonA = Button(ventana, text="A", width=5, height=2, command=lambda: click_boton("A"), bg="sky blue")
botonB = Button(ventana, text="B", width=5, height=2, command=lambda: click_boton("B"), bg="sky blue")
botonC = Button(ventana, text="C", width=5, height=2, command=lambda: click_boton("C"), bg="sky blue")
botonD = Button(ventana, text="D", width=5, height=2, command=lambda: click_boton("D"), bg="sky blue")
botonE = Button(ventana, text="E", width=5, height=2, command=lambda: click_boton("E"), bg="sky blue")
botonF = Button(ventana, text="F", width=5, height=2, command=lambda: click_boton("F"), bg="sky blue")


boton_borrar = Button(ventana, text="AC", width=4, height=2, command=lambda: borrar(), bg="sky blue")
boton_Parentesis1 = Button(ventana, text="(", width=4, height=2, command=lambda: click_boton("("), bg="sky blue")
boton_Parentesis2 = Button(ventana, text=")", width=5, height=2, command=lambda: click_boton(")"), bg="sky blue")
boton_Punto = Button(ventana, text=".", width=5, height=2, command=lambda: click_boton("."), bg="sky blue")
boton_igual = Button(ventana, text="=", width=5, height=2, command=lambda: resultado(), bg="sky blue")
boton_div = Button(ventana, text="/", width=5, height=2, command=lambda: click_boton("/"), bg="sky blue")
boton_mult = Button(ventana, text="x", width=5, height=2, command=lambda: click_boton("*"), bg="sky blue")
boton_suma = Button(ventana, text="+", width=5, height=2, command=lambda: click_boton("+"), bg="sky blue")
boton_resta = Button(ventana, text="-", width=5, height=2, command=lambda: click_boton("-"), bg="sky blue")
boton_hexa = Button(ventana,text="hexadecimal", width=5, height=2, command=lambda:operacion(), bg="sky blue")


boton_retroceder = Button(ventana, text="←", width=5, height=2, command=lambda: retroceder(), bg="sky blue")


boton_borrar.grid(row=1, column=0, padx=5, pady=5)
boton_Parentesis1.grid(row=1, column=1, padx=5, pady=5)
boton_Parentesis2.grid(row=1, column=2, padx=5, pady=5)
boton_div.grid(row=1, column=3, padx=5, pady=5)

boton7.grid(row=2, column=0, padx=5, pady=5)
boton8.grid(row=2, column=1, padx=5, pady=5)
boton9.grid(row=2, column=2, padx=5, pady=5)
boton_mult.grid(row=2, column=3, padx=5, pady=5)

boton4.grid(row=3, column=0, padx=5, pady=5)
boton5.grid(row=3, column=1, padx=5, pady=5)
boton6.grid(row=3, column=2, padx=5, pady=5)
boton_suma.grid(row=3, column=3, padx=5, pady=5)

boton1.grid(row=4, column=0, padx=5, pady=5)
boton2.grid(row=4, column=1, padx=5, pady=5)
boton3.grid(row=4, column=2, padx=5, pady=5)
boton_resta.grid(row=4, column=3, padx=5, pady=5)

boton0.grid(row=5, column=0, padx=5, pady=5)
boton_Punto.grid(row=5, column=1, padx=5, pady=5)
boton_igual.grid(row=5, column=2, padx=5, pady=5)
boton_retroceder.grid(row=5, column=3, padx=5, pady=5)

botonA.grid(row=6, column=0, padx=5, pady=5)
botonB.grid(row=6, column=1, padx=5, pady=5)
boton_hexa.grid(row=5, column=6, padx=5, pady=5)

ventana.mainloop()