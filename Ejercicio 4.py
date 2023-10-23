# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 12:34:20 2023

@author: fzapber
"""

meses = {
    '01': 'enero', '02': 'febrero', '03': 'marzo', '04': 'abril',
    '05': 'mayo', '06': 'junio', '07': 'julio', '08': 'agosto',
    '09': 'septiembre', '10': 'octubre', '11': 'noviembre', '12': 'diciembre'
}
fecha = input("Ingresa una fecha en formato dd/mm/aaaa: ")
dia, mes, anio = fecha.split('/')
print(f"{dia} de {meses[mes]} de {anio}")
