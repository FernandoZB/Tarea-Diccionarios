# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 12:40:27 2023

@author: fzapber
"""

diccionario_traduccion = {}
entrada = input("Ingresa las palabras en español e inglés separadas por dos puntos y coma (ejemplo: perro:dog, gato:cat): ")
palabras = entrada.split(',')
for par in palabras:
    palabra, traduccion = par.split(':')
    diccionario_traduccion[palabra] = traduccion

frase_espanol = input("Ingresa una frase en español: ")
palabras = frase_espanol.split()
frase_traducida = " ".join(diccionario_traduccion.get(palabra, palabra) for palabra in palabras)
print(f"Frase traducida: {frase_traducida}")
