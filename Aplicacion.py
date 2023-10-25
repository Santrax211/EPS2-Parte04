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
        


