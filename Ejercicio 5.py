# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 12:35:41 2023

@author: fzapber
"""

creditos_asignaturas = {}
total_creditos = 0
while True:
    clave = input("Ingresa una asignatura (o 'fin' para terminar): ")
    if clave == 'fin':
        break
    valor = int(input(f"Ingresa el numero de creditos para {clave}: "))
    creditos_asignaturas[clave] = valor
    
for asignatura, creditos in creditos_asignaturas.items():
    print(f"{asignatura} tiene {creditos} créditos.")
    total_creditos += creditos
print(f"El número total de créditos del curso es {total_creditos}.")