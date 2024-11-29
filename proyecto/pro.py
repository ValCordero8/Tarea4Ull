import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector



def conectar_bd():
    return mysql.connector.connect(host="localhost", user="root", password="", database="gestion")


#   iniciar ses
def login():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT rol FROM usuarios WHERE usuario=%s AND contraseña=%s", (usuario, contraseña))
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        rol = resultado[0]
        if rol == "administrador":
            abrir_admin()
        elif rol == "empleado":
            abrir_empleado()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")


# (Solo para adm)
def gestionar_empleados():
    def mostrar_empleados():
        """Carga todos los empleados en la tabla."""
        for item in tree_empleados.get_children():
            tree_empleados.delete(item)
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE rol!='administrador'")
        for empleado in cursor.fetchall():
            tree_empleados.insert("", tk.END, values=empleado)
        conn.close()

    def agregar_empleado():
        """Agrega un nuevo empleado con el rol seleccionado."""
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        usuario = entry_usuario_empleado.get()
        contraseña = entry_contraseña_empleado.get()
        rol = combo_rol.get()
        if not rol:
            messagebox.showwarning("Advertencia", "Debe seleccionar un rol para el empleado.")
            return
        conn = conectar_bd()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO usuarios (nombre, apellido, usuario, contraseña, rol) VALUES (%s, %s, %s, %s, %s)",
                (nombre, apellido, usuario, contraseña, rol),
            )
            conn.commit()
            mostrar_empleados()
            messagebox.showinfo("Bien", "Empleado agregado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            conn.close()

    def actualizar_empleado():
        """Actualiza los datos del empleado seleccionado."""
        seleccionado = tree_empleados.focus()
        if seleccionado:
            empleado_id = tree_empleados.item(seleccionado)["values"][0]
            nombre = entry_nombre.get()
            apellido = entry_apellido.get()
            usuario = entry_usuario_empleado.get()
            contraseña = entry_contraseña_empleado.get()
            rol = combo_rol.get()
            if not rol:
                messagebox.showwarning("Advertencia", "Debe seleccionar un rol para el empleado.")
                return
            conn = conectar_bd()
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "UPDATE usuarios SET nombre=%s, apellido=%s, usuario=%s, contraseña=%s, rol=%s WHERE id=%s",
                    (nombre, apellido, usuario, contraseña, rol, empleado_id),
                )
                conn.commit()
                mostrar_empleados()
                messagebox.showinfo("Bien", "Empleado actualizado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", str(e))
            finally:
                conn.close()
        else:
            messagebox.showwarning("Advertencia", "Seleccione un empleado para actualizar.")

    def eliminar_empleado():
        """Elimina un empleado seleccionado."""
        seleccionado = tree_empleados.focus()
        if seleccionado:
            empleado_id = tree_empleados.item(seleccionado)["values"][0]
            conn = conectar_bd()
            cursor = conn.cursor()
            try:
                cursor.execute("DELETE FROM usuarios WHERE id=%s", (empleado_id,))
                conn.commit()
                mostrar_empleados()
                messagebox.showinfo("Bien", "Empleado eliminado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", str(e))
            finally:
                conn.close()
        else:
            messagebox.showwarning("Advertencia", "Seleccione un empleado para eliminar")

    ventana_empleados = tk.Toplevel()
    ventana_empleados.title("Gestión de Empleados")

    # Formulario de empleado
    tk.Label(ventana_empleados, text="Nombre").grid(row=0, column=0, padx=5, pady=5)
    entry_nombre = tk.Entry(ventana_empleados)
    entry_nombre.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(ventana_empleados, text="Apellido").grid(row=1, column=0, padx=5, pady=5)
    entry_apellido = tk.Entry(ventana_empleados)
    entry_apellido.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(ventana_empleados, text="Usuario").grid(row=2, column=0, padx=5, pady=5)
    entry_usuario_empleado = tk.Entry(ventana_empleados)
    entry_usuario_empleado.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(ventana_empleados, text="Contraseña").grid(row=3, column=0, padx=5, pady=5)
    entry_contraseña_empleado = tk.Entry(ventana_empleados, show="*")
    entry_contraseña_empleado.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(ventana_empleados, text="Rol").grid(row=4, column=0, padx=5, pady=5)
    combo_rol = ttk.Combobox(ventana_empleados, values=["empleado", "bibliotecario", "vendedor"], state="readonly")
    combo_rol.grid(row=4, column=1, padx=5, pady=5)

    # Botones
    tk.Button(ventana_empleados, text="Agregar", command=agregar_empleado).grid(row=5, column=0, pady=5)
    tk.Button(ventana_empleados, text="Actualizar", command=actualizar_empleado).grid(row=5, column=1, pady=5)

    # Tabla
    columnas = ("ID", "Nombre", "Apellido", "Usuario", "Rol")
    tree_empleados = ttk.Treeview(ventana_empleados, columns=columnas, show="headings")
    for col in columnas:
        tree_empleados.heading(col, text=col)
    tree_empleados.grid(row=6, column=0, columnspan=2, pady=10)

    tk.Button(ventana_empleados, text="Eliminar", command=eliminar_empleado).grid(row=7, column=0, columnspan=2, pady=5)

    mostrar_empleados()


#  libros 
def gestionar_libros():
    def mostrar_libros():
        """Carga todos los libros en la tabla."""
        for item in tree_libros.get_children():
            tree_libros.delete(item)
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM libros")
        for libro in cursor.fetchall():
            tree_libros.insert("", tk.END, values=libro)
        conn.close()
#Elegi filtrar por editorial
    def filtrar_libros():
        """Filtra los libros por editorial"""
        editorial = entry_filtro_editorial.get()
        for item in tree_libros.get_children():
            tree_libros.delete(item)
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM libros WHERE editorial=%s", (editorial,))
        for libro in cursor.fetchall():
            tree_libros.insert("", tk.END, values=libro)
        conn.close()

    def agregar_libro():
        """Agrega un nuevo libro"""
        titulo = entry_titulo.get()
        autor = entry_autor.get()
        editorial = entry_editorial.get()
        año = entry_año.get()
        precio = entry_precio.get()
        conn = conectar_bd()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO libros (titulo, autor, editorial, año_publicacion, precio) VALUES (%s, %s, %s, %s, %s)",
                (titulo, autor, editorial, año, precio),
            )
            conn.commit()
            mostrar_libros()
            messagebox.showinfo("Éxito", "Libro agregado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            conn.close()

    def actualizar_libro():
        """Actualiza los datos de un libro seleccionado"""
        seleccionado = tree_libros.focus()
        if seleccionado:
            libro_id = tree_libros.item(seleccionado)["values"][0]
            titulo = entry_titulo.get()
            autor = entry_autor.get()
            editorial = entry_editorial.get()
            año = entry_año.get()
            precio = entry_precio.get()
            conn = conectar_bd()
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "UPDATE libros SET titulo=%s, autor=%s, editorial=%s, año_publicacion=%s, precio=%s WHERE id=%s",
                    (titulo, autor, editorial, año, precio, libro_id),
                )
                conn.commit()
                mostrar_libros()
                messagebox.showinfo("Éxito", "Libro actualizado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", str(e))
            finally:
                conn.close()
        else:
            messagebox.showwarning("Advertencia", "Seleccione un libro para actualizar.")

    def eliminar_libro():
        """Elimina un libro seleccionado"""
        seleccionado = tree_libros.focus()
        if seleccionado:
            libro_id = tree_libros.item(seleccionado)["values"][0]
            conn = conectar_bd()
            cursor = conn.cursor()
            try:
                cursor.execute("DELETE FROM libros WHERE id=%s", (libro_id,))
                conn.commit()
                mostrar_libros()
                messagebox.showinfo("Éxito", "Libro eliminado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", str(e))
            finally:
                conn.close()
        else:
            messagebox.showwarning("Advertencia", "Seleccione un libro para eliminar.")

    ventana_libros = tk.Toplevel()
    ventana_libros.title("Gestión de Libros")

    tk.Label(ventana_libros, text="Filtrar por Editorial").grid(row=0, column=0, padx=5, pady=5)
    entry_filtro_editorial = tk.Entry(ventana_libros)
    entry_filtro_editorial.grid(row=0, column=1, padx=5, pady=5)
    tk.Button(ventana_libros, text="Filtrar", command=filtrar_libros).grid(row=0, column=2, padx=5, pady=5)

    tk.Label(ventana_libros, text="Título").grid(row=1, column=0, padx=5, pady=5)
    entry_titulo = tk.Entry(ventana_libros)
    entry_titulo.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(ventana_libros, text="Autor").grid(row=2, column=0, padx=5, pady=5)
    entry_autor = tk.Entry(ventana_libros)
    entry_autor.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(ventana_libros, text="Editorial").grid(row=3, column=0, padx=5, pady=5)
    entry_editorial = tk.Entry(ventana_libros)
    entry_editorial.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(ventana_libros, text="Año").grid(row=4, column=0, padx=5, pady=5)
    entry_año = tk.Entry(ventana_libros)
    entry_año.grid(row=4, column=1, padx=5, pady=5)

    tk.Label(ventana_libros, text="Precio").grid(row=5, column=0, padx=5, pady=5)
    entry_precio = tk.Entry(ventana_libros)
    entry_precio.grid(row=5, column=1, padx=5, pady=5)

    tk.Button(ventana_libros, text="Agregar", command=agregar_libro).grid(row=6, column=0, padx=5, pady=5)
    tk.Button(ventana_libros, text="Actualizar", command=actualizar_libro).grid(row=6, column=1, padx=5, pady=5)
    tk.Button(ventana_libros, text="Eliminar", command=eliminar_libro).grid(row=6, column=2, padx=5, pady=5)

    # Tabla mostrar libros
    columnas = ("ID", "Título", "Autor", "Editorial", "Año", "Precio")
    tree_libros = ttk.Treeview(ventana_libros, columns=columnas, show="headings")
    for col in columnas:
        tree_libros.heading(col, text=col)
        tree_libros.grid(row=7, column=0, columnspan=3, pady=10)

    mostrar_libros()

    



def abrir_admin():
    ventana_admin = tk.Toplevel()
    ventana_admin.title("Panel de Administrador")
    tk.Button(ventana_admin, text="Gestionar Empleados", command=gestionar_empleados).pack(pady=10)
    tk.Button(ventana_admin, text="Gestionar Libros", command=gestionar_libros).pack(pady=10)


def abrir_empleado():
    ventana_empleado = tk.Toplevel()
    ventana_empleado.title("Panel de Empleado")
    tk.Button(ventana_empleado, text="Gestionar Libros", command=gestionar_libros).pack(pady=10)



ventana_login = tk.Tk()
ventana_login.title("Sistema de Gestión - Login")

tk.Label(ventana_login, text="Usuario").grid(row=0, column=0, padx=10, pady=10)
entry_usuario = tk.Entry(ventana_login)
entry_usuario.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana_login, text="Contraseña").grid(row=1, column=0, padx=10, pady=10)
entry_contraseña = tk.Entry(ventana_login, show="*")
entry_contraseña.grid(row=1, column=1, padx=10, pady=10)

tk.Button(ventana_login, text="Iniciar Sesión", command=login).grid(row=2, column=0, columnspan=2, pady=10)

ventana_login.mainloop()


# ADMINISTRADORES LOS AGREGO EN BASE DE DATOS