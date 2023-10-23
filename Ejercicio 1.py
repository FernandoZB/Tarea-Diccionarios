# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 12:25:52 2023

@author: fzapber
"""

divisas = {'Euro': '€', 'Dollar': '$', 'Yen': 'Y'}
divisa = input("Ingresa una divisa: ")
if divisa in divisas:
    print(f"El símbolo de {divisa} es {divisas[divisa]}")
else:
    print("La divisa no está en el diccionario.")
