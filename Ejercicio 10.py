# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 10:20:14 2023

@author: fzapber
"""

clientes = {}
while True:
    print("Menú:")
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar todos los clientes")
    print("5. Listar clientes preferentes")
    print("6. Terminar")
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == '1':
        nif = input("NIF del cliente: ")
        nombre = input("Nombre del cliente: ")
        direccion = input("Dirección del cliente: ")
        telefono = input("Teléfono del cliente: ")
        preferente = input("¿Es cliente preferente? (Sí o No): ").lower() == "si"
        
        clientes[nif] = {'nombre': nombre, 'direccion': direccion, 'telefono': telefono, 'preferente': preferente}
        print("Cliente añadido.")
        
    elif opcion == '2':
        nif = input("NIF del cliente a eliminar: ")
        if nif in clientes:
            del clientes[nif]
            print("Cliente eliminado.")
        else:
            print("Cliente no encontrado.")
        
    elif opcion == '3':
        nif = input("NIF del cliente a mostrar: ")
        if nif in clientes:
            cliente = clientes[nif]
            print(f"Datos del cliente {nif}:")
            print(f"Nombre: {cliente['nombre']}")
            print(f"Dirección: {cliente['direccion']}")
            print(f"Teléfono: {cliente['telefono']}")
            print(f"Preferente: {'Sí' if cliente['preferente'] else 'No'}")
        else:
            print("Cliente no encontrado.")
        
    elif opcion == '4':
        print("Lista de todos los clientes:")
        for nif, cliente in clientes.items():
            print(f"{nif}: {cliente['nombre']}")
        
    elif opcion == '5':
        print("Clientes preferentes:")
        for nif, cliente in clientes.items():
            if cliente['preferente']:
                print(f"{nif}: {cliente['nombre']}")
        
    elif opcion == '6':
        break
