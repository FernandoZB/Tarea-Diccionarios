# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 12:32:46 2023

@author: fzapber
"""

precios_frutas = {
    'Platano': 1.35,
    'Manzana': 0.80,
    'Pera': 0.85,
    'Naranja': 0.70
}
fruta = input("Ingresa una fruta: ")
if fruta in precios_frutas:
    kilos = float(input(f"Ingresa el número de kilos de {fruta}: "))
    precio_total = precios_frutas[fruta] * kilos
    print(f"El precio de {kilos} kilos de {fruta} es {precio_total} €")
else:
    print("La fruta no está en el diccionario.")
