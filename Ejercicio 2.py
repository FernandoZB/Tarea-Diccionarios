# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 12:28:47 2023

@author: fzapber
"""

datos = {}
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
direccion = input("Ingresa tu dirección: ")
telefono = input("Ingresa tu número de teléfono: ")
datos['nombre'] = nombre
datos['edad'] = edad
datos['direccion'] = direccion
datos['telefono'] = telefono
print(f"{nombre} tiene {edad} años, vive en {direccion} y su número de teléfono es {telefono}.")
