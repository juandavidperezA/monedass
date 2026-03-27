import json
from datetime import datetime
from config import ruta

       
              
def lista_gasto():
    
    print("""=============================================
                Listar Gastos
=============================================
Seleccione una opción para filtrar los gastos:

1. Ver todos los gastos
2. Filtrar por categoría
3. Filtrar por rango de fechas
4. Regresar al menú principal
=============================================""")
    
    try:
        opcion= int(input("ingresa una opcion: "))
    except ValueError:
        print("solo numeros")
        return 
    if opcion==1:
        try:
            with open (ruta, "r") as f:
                datos=json.load(f)
        except:
            print("no hay gastos registrados.")
            return
        if not datos:
            print("no hay gastos para mostrar. ")
            return
        
        
        print("""=======================
lista de gastos registrados
============================""")
        
        for g in datos:
            print("------------------------------------------------")
            print("fecha", g.get("fecha"))
            print("cantidad", g["cantidad"])
            print ("categoria", g["categoria"])
            print("descripcion", g.get("descripcion"))
            
            
    elif opcion == 2:
        categoria1 = input("escribe la categoria que estas interesada en ver: ")
    
        try:
            with open(ruta, "r") as f:
                datos = json.load(f)
        except:
            print("no hay gastos registrados.")
            return

        encontrados = False

        print("""===============================================
gastos segun su categoria
===============================================""")

        for g in datos:
            if g["categoria"].lower() == categoria1.lower():
                print("------------------------------------------------")
                print("cantidad", g["cantidad"])
                print("categoria", g["categoria"])
                print("descripcion", g.get("descripcion"))
                encontrados = True

        if not encontrados:
            print("no hay datos con esa categoria")
            
    elif opcion==3:
        fechas= input("ingresa la fecha del gasto registrado (YYYY-MM-DD)")
        
        try:
            datetime.strptime(fechas, "%Y-%m-%d")
        except ValueError:
            print("la fecha esta mal escrita... vuelva a intentar")
            return
        try:
            with open (ruta, "r") as f:
                datos= json.load(f)
        except FileNotFoundError:
            print("no hay datos")
            return
            
        encontrados=False
        
        print("gastos con esa fecha:")
        for g in datos:
            if g.get("fecha") == fechas:
                print("------------------------------------------------")
                print("cantidad", g["cantidad"])
                print("categoria", g["categoria"])
                print("descripcion", g.get("descripcion"))
                print ("fecha" , g.get("fecha"))
                encontrados = True

        if not encontrados:
            print("no hay datos con esa fecha")

    elif opcion==4:
        print("regresando al menu...")
        return 
    else:
        print("accion invalida")