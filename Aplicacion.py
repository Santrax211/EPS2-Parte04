# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 09:24:45 2023

@author: ADMIM
"""

print("\nMenú Opciones")
print("1. Registrar")
print("2. Eliminar")
print("3. Editar")
print("4. Listar")
print("5. Salir")
while True:
    opcion=input("Seleccione una opcion: ")
    if opcion =="1":
        print("Seleccionaste Registar.")
    elif opcion =="2":
        print("Seleccionaste Eliminar.")
    elif opcion=="3":
        print("Seleccionaste Editar.")
    elif opcion=="4":
        print("Seleccionaste Listar.")
    elif opcion=="5":
        print("Seleccionaste Salir.")
        break
    else:
        print("Opcion no validad.")
        
        
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