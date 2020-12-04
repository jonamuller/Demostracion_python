#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3




with sqlite3.connect("ventas.sqlite") as con:
    cursor = con.cursor()
    
    try:
        cursor.execute("create table ventas (id integer primary key autoincrement, producto text, precio numeric)")
    except:
        pass



def mostrar():
    with sqlite3.connect("ventas.sqlite") as con:
        cursor = con.cursor()
        cursor.execute("select * from ventas")
        data = cursor.fetchall()
    
    for venta in data:
        print("\t{:3d} {:>15s}: ${:10.2f}".format(*venta))    #format(venta[0], venta[1], venta[2]))
    
    
def ingresar():
    
    while True:
        try:
            producto = input("\tNombre del procucto: ")
            precio =float(input("\tPrecio: "))
        except:
            print("No se pudo ingresar el dato, formato incorrecto. Intente nuevamente")
        else:
            break
    
    
    
    with sqlite3.connect("ventas.sqlite") as con:
        cursor = con.cursor()
        cursor.execute("insert into ventas values (null, ?, ?)", (producto, precio))
        con.commit()
        
    

def total():
    with sqlite3.connect("ventas.sqlite") as con:
        cursor = con.cursor()
        cursor.execute("select sum(precio) from ventas")
        total, = cursor.fetchone()
    
    print("\tTotal de ventas: ${}".format(total))











while True:
    
    opcion = input("""1. Mostrar ventas
2. Ingresar venta
3. Calcular total de ventas
4. Salir
""")
    
    if opcion == "1":
        mostrar()
    
    elif opcion == "2":
        ingresar()


    elif opcion == "3":
        total()

    elif opcion == "4":
        break

    else:
        print(opcion, "no es una opcion valida")












