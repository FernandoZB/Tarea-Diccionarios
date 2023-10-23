# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 10:16:45 2023

@author: fzapber
"""

facturas = {}
total_cobrado = 0
while True:
    opcion = input("¿Qué deseas hacer? (añadir/pagar/terminar): ")
    if opcion == "terminar":
        break
    elif opcion == "añadir":
        num_factura = input("Número de factura: ")
        costo = float(input("Coste de la factura: "))
        facturas[num_factura] = costo
    elif opcion == "pagar":
        num_factura = input("Número de factura a pagar: ")
        if num_factura in facturas:
            total_cobrado += facturas[num_factura]
            del facturas[num_factura]
        else:
            print("La factura no existe.")
    print(f"Total cobrado: {total_cobrado}")
    print(f"Facturas pendientes: {facturas}")
