# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 12:39:06 2023

@author: fzapber
"""

cesta_compra = {}
while True:
    articulo = input("Ingresa el artículo (o 'fin' para terminar): ")
    if articulo == 'fin':
        break
    precio = float(input(f"Ingresa el precio de {articulo}: "))
    cesta_compra[articulo] = precio

total = sum(cesta_compra.values())
print("Lista de la compra:")
for articulo, precio in cesta_compra.items():
    print(f"{articulo} {precio}")
print(f"Total {total}")
