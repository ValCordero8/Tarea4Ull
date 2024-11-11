import tkinter as tk
from tkinter import messagebox

class ProductoInvalidoException(Exception):
    pass

class PrecioInvalidoException(Exception):
    pass

class CantidadInvalidaException(Exception):
    pass

class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int):
        if not nombre:
            raise ProductoInvalidoException("Ingresa el nombre del producto")
        if precio <= 0:
            raise PrecioInvalidoException("El precio debe ser mayor a cero")
        if cantidad < 0:
            raise CantidadInvalidaException("La cantidad debe ser positiva")
        
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_valor_total(self) -> float:
        return self.precio * self.cantidad

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion de Productos")

        self.productos = {}  
        self.total_inventario = 0  

        tk.Label(root, text="Nombre del Producto:").grid(row=0, column=0, pady=5)
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.grid(row=0, column=1, pady=5)

        tk.Label(root, text="Precio:").grid(row=1, column=0, pady=5)
        self.entry_precio = tk.Entry(root)
        self.entry_precio.grid(row=1, column=1, pady=5)

        tk.Label(root, text="Cantidad:").grid(row=2, column=0, pady=5)
        self.entry_cantidad = tk.Entry(root)
        self.entry_cantidad.grid(row=2, column=1, pady=5)

        
        self.btn_agregar = tk.Button(
            root,
            text="Agregar Producto",
            bg="#AEC6CF",
            fg="#4B4B4B",
            font=("Arial", 12, "italic"),
            width=15,
            height=2,
            relief="groove",
            bd=3,
            activebackground="#CFCFCF",
            activeforeground="#7F7F7F",
            command=self.agregar_producto
        )
        self.btn_agregar.grid(row=3, column=0, columnspan=2, pady=10)

        self.lbl_total_inventario = tk.Label(root, text="Total en Inventario: $0.00", fg="darkblue")
        self.lbl_total_inventario.grid(row=4, column=0, columnspan=2, pady=5)

        
        tk.Label(root, text=" Productos en Inventario:").grid(row=5, column=0, columnspan=2, pady=5)
        self.text_lista_productos = tk.Text(root, height=10, width=50, state='disabled')
        self.text_lista_productos.grid(row=6, column=0, columnspan=2, pady=5)

    def agregar_producto(self):
        nombre = self.entry_nombre.get()
        try:
            precio = float(self.entry_precio.get())
            cantidad = int(self.entry_cantidad.get())

            if nombre in self.productos:
                
                producto_existente = self.productos[nombre]
                producto_existente.cantidad += cantidad
                self.total_inventario += precio * cantidad  
            else:
                
                nuevo_producto = Producto(nombre, precio, cantidad)
                self.productos[nombre] = nuevo_producto
                self.total_inventario += nuevo_producto.calcular_valor_total()

            
            self.lbl_total_inventario.config(text=f"Total en Inventario: ${self.total_inventario:.2f}")
            self.actualizar_lista_productos()

        except ValueError:
            messagebox.showerror("Error de Entrada", "Precio y cantidad deben ser numeros")
        except ProductoInvalidoException as e:
            messagebox.showerror("Error de Producto", str(e))
        except PrecioInvalidoException as e:
            messagebox.showerror("Error de Precio", str(e))
        except CantidadInvalidaException as e:
            messagebox.showerror("Error de Cantidad", str(e))

    def actualizar_lista_productos(self):
        
        self.text_lista_productos.config(state='normal')
        self.text_lista_productos.delete(1.0, tk.END)
        
        for nombre, producto in self.productos.items():
            self.text_lista_productos.insert(
                tk.END, f"{nombre} - Cantidad: {producto.cantidad}\n"
            )
        
       
        self.text_lista_productos.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
