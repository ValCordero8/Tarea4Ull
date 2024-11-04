import tkinter as tk
from tkinter import messagebox



def sumar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        suma = num1 + num2
        messagebox.showinfo("Resultado", f"La suma es: {suma}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
def restar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resta = num1 - num2
        messagebox.showinfo("Resultado", f"La resta es: {resta}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
def dividir():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        divicion = num1 / num2
        messagebox.showinfo("Resultado", f"El resultado es: {divicion}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
def multiplicar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        multiplicacion = num1  * num2
        messagebox.showinfo("Resultado", f"El resultado: {multiplicacion}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

         
         
ventana = tk.Tk()
ventana.title("Calculadora de Suma")
ventana.geometry("800x5cle00")
 
label_num1 = tk.Label(ventana, text="Número 1:")
label_num1.pack(pady=5)
entry_num1 = tk.Entry(ventana)
entry_num1.pack(pady=5)
 
label_num2 = tk.Label(ventana, text="Número 2:")
label_num2.pack(pady=5)
entry_num2 = tk.Entry(ventana)
entry_num2.pack(pady=5)
 
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack(pady=20)
boton_restar = tk.Button(ventana, text="Restar", command=restar)
boton_restar.pack(pady=20)
boton_dividir = tk.Button(ventana, text="Dividir", command=dividir)
boton_dividir.pack(pady=20)
boton_multiplicar = tk.Button(ventana, text="Mutiplicar", command=multiplicar)
boton_multiplicar.pack(pady=20)
 
ventana.mainloop()