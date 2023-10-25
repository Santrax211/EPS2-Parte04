# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 09:24:45 2023

@author: ADMIM
"""

#Creación de la base de datos
import sqlite3
conexion = sqlite3.connect("Urbisagastegui_Almacen.db")

#Creación de la tabla producto
producto = """Create table producto(
           idproducto INTEGER PRIMARY KEY,
           codigo TEXT,
           nombre TEXT,
           precio FLOAT
    )
"""
cursor = conexion.cursor()
cursor.execute(producto)
conexion.close()

"""Funcion para listar productos"""
def listar_productos():
    conexion = sqlite3.connect('Urbisagastegui_Almacen.db')
    cursor = conexion.cursor()
    
    cursor.execute("Select *from producto")
    productos = cursor.fetchall()

    conexion.close()
    
    if productos:
        print("Listado de productos:")
        for producto in productos:
            print(f"ID: {producto[0]}, codigo: {producto[1]}, nombre:{producto[2]}, precio: {producto[3]}")
        else:
            print("NO HAY PRODUCTOS REGISTRADOS")
            
"""Funcion para registrar productos"""
def registrar_producto():
    conn = sqlite3.connect('Urbisagastegui_Almacen.db')
    cursor = conn.cursor()
    
    codigo = input("Ingrese el codigo del producto:")
    nombre = input("Ingrese el nombre del producto:")
    precio = input("Ingrese el precio del producto:")
    
    cursor.execute("Insert into producto(codigo, nombre, precio) values (?,?,?)", (codigo, nombre, precio))
    
    conn.commit()
    conn.close()
    print("PRODUCTO REGISTRADO EXITOSAMENTE")
    
"""Funcion para eliminar productos"""
def eliminar_productos():
    print("Eliminar productos por codigo")
    codigo = input("Ingrese el codigo del producto a eliminar: ")
    
    conexion = sqlite3.connect("Urbisagastegui_almacen.db")
    cursor = conexion.cursor()
    
    consulta_select = """ SELECT codigo
                        FROM producto
                        WHERE codigo = ?
                      """
    cursor.execute(consulta_select, (codigo,))
    producto = cursor.fetchone()
    
    # verificar que el producto existe
    if producto:
        consulta_delete = """
                            DELETE FROM producto
                            WHERE codigo = ?
                          """
        cursor.execute(consulta_delete, (codigo,))
        conexion.commit()
        print("-"*25 + "\nProducto eliminado\n" + "-"*25 + "\n\n")
    else:
        print("No existe ese producto en la bd")
    
    conexion.close()
    
"""Funcion para editar prodcutos"""
def editar_productos():
    print("Editar Producto")
    codigo = input("Ingrese el código del producto a editar: ")

    conexion = sqlite3.connect("BarzolaCamanCuro_almacen.db")
    cursor = conexion.cursor()

    # verificar que el producto existe
    consulta_select = """SELECT codigo, nombre, precio
                        FROM producto
                        WHERE codigo = ?
                      """
    cursor.execute(consulta_select, (codigo,))
    producto = cursor.fetchone()

    if producto:
        print("\nProducto encontrado\n")
        print("Información del producto:")
        codigo, nombre, precio = producto
        print(f"Código: {codigo}")
        print(f"Nombre: {nombre}")
        print(f"Precio: {precio:.2f}")

        nombre_nuevo = input("\nNuevo nombre: ")
        precio_nuevo = input("Nuevo precio: ")
        
        #modificar nombre
        if nombre_nuevo:
            consulta_update_nombre = """UPDATE producto
                                    SET nombre = ?
                                    WHERE codigo = ?
                                    """
            cursor.execute(consulta_update_nombre, (nombre_nuevo, codigo))
            
        #modificar precio
        if precio_nuevo:
            try:
                nuevo_precio = float(precio_nuevo)
                consulta_update_precio = """ UPDATE producto
                                        SET precio = ?
                                        WHERE codigo = ?
                                        """
                cursor.execute(consulta_update_precio, (precio_nuevo, codigo))
            except ValueError:
                print("El precio debe ser un número que sea válido")

        conexion.commit()
        print("-"*25 + "\nProducto editado\n" + "-"*25 + "\n\n")
    else:
        print("No existe ese producto en la bd")

    conexion.close()


print("\nMenú Opciones")
print("1. Registrar")
print("2. Eliminar")
print("3. Editar")
print("4. Listar")
print("5. Salir")
while True:
    opcion=input("Seleccione una opcion: ")
    if opcion =="1":
        registrar_producto()
    elif opcion =="2":
        print("Seleccionaste Eliminar.")
    elif opcion=="3":
        print("Seleccionaste Editar.")
    elif opcion=="4":
        listar_productos()
    elif opcion=="5":
        print("Seleccionaste Salir")
        break
    else:
        print("Opcion no validada")
        


