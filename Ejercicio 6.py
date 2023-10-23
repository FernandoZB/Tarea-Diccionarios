# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 12:36:59 2023

@author: fzapber
"""

persona = {}
while True:
    clave = input("Ingresa un dato (o 'fin' para terminar): ")
    if clave == 'fin':
        break
    valor = input(f"Ingresa el valor para {clave}: ")
    persona[clave] = valor
    print(persona)
