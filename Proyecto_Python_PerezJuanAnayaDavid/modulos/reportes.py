import json
import os
from datetime import datetime
from config import ruta, ruta2, base_dir

    
def generar_reporte():
    print("""=============================================
           Generar Reporte de Gastos
=============================================
Seleccione el tipo de informe:

1. Reporte diario
2. Reporte semanal
3. Informe mensual
4. Regresar al menú principal
=============================================""")
    
    try:
        opcion7= int(input("ingresa alguna de las opciones"))
    except ValueError:
        print("solo se acepta numeros")
        return
        
        
    if opcion7==1:
        print("""=========================================
reporte de gastos diario
=================================""")
        
        fechare=input("ingresa la fecha de que quieras ver el reporte: (YYYY-MM-DD)")
        
        try:
            datetime.strptime(fechare, "%Y-%m-%d")
        except ValueError:
            print("la fecha esta mal escrita")
            return
        try:
            with open (ruta, "r") as f:
                datos= json.load(f)
        except FileNotFoundError:
            print("dato no encontrado")
            return
            
        reportees= []
        
        for g in datos:
            if g.get("fecha")== fechare:
                reportees.append(g)
        if not reportees:
            print("no se encuentra gastos en esa fecha ")
            return
            
        #momento de sumar gastos
        total=0 
        for g in reportees:
            total+= g["cantidad"]
            
        cantidad = len(reportees)
        
        
        print("\n Fecha:", fechare)
        print(" Total gastado:", total)
        print(" Número de gastos:", cantidad)

        print("\n Detalle:")
        for g in reportees:
            print("----------------")
            print("Cantidad:", g["cantidad"])
            print("Categoría:", g["categoria"])
            print("Descripción:", g["descripcion"])
            
        # RESUMEN POR CATEGORIAS
        categorias = {}
        for g in reportees:
            cat = g["categoria"]
            categorias[cat] = categorias.get(cat, 0) + g["cantidad"]

        print("\nResumen por categorías:")
        for cat, monto in categorias.items():
                print(f"{cat}: {monto}")


        guardar = input("¿Desea guardar el reporte en JSON? S/N: ")

        if guardar.lower() == "s":
            reporte_json = {
                "tipo": "diario",
                "fecha": fechare,
                "total": total,
                "cantidad_gastos": cantidad,
                "categorias": categorias
            }

            ruta_diario = os.path.join(base_dir, "reporte_diario.json")

            with open(ruta_diario, "w") as f:
                json.dump(reporte_json, f, indent=4)

            print("Reporte diario guardado correctamente")
            
            
        elif guardar.lower()=="n":
            print("entendido") 
        else:
            print("accion no valida")
            
               
    elif opcion7==2:
        print("""======================================================================
REPORTE DE GASTOS SEMANALES
=================================================================""")
        inicio=input("ingresa el inicio de la semana que quieras saber: (YYYY-MM-DD)")
        final = input("ingresa el final de la semana que quieras saber: (YYYY-MM-DD)")
        try:
            fecha_inicio= datetime.strptime(inicio, "%Y-%m-%d")
            fecha_final= datetime.strptime(final, "%Y-%m-%d")
        except ValueError:
            print("fecha no valida")
            return
        try:
            with open (ruta,"r") as f:
                datos= json.load(f)
        except FileNotFoundError:
            print("datos no encontrados")
            return
        
        reportes_semana= []
        
        for g in datos:
            try:
                fecha_gasto= datetime.strptime(g["fecha"], "%Y-%m-%d")
            except:
                continue
            
            if fecha_inicio<= fecha_gasto<=fecha_final:
                reportes_semana.append(g)
        if not reportes_semana:
                print("no hay gastos en ese rango")
                return
            
        totall=0
            
        for g in reportes_semana:
                totall+= g["cantidad"]
                
        cantidad= len(reportes_semana)
            
        print(f"desde {inicio} hasta {final}")
        print(f"el total gastado fue de {totall}")
        print(f"el numero de gasto es: {cantidad}")
            
        print("\nDetalles:")
        for g in reportes_semana:
            print("-------------------------------")
            print("cantidad: ", g["cantidad"])  
            print("categoria ", g["categoria"])
            print("descripcion: ", g["descripcion"] )
            
            
        categorias = {}
        for g in reportes_semana:
            cat = g["categoria"]
            categorias[cat] = categorias.get(cat, 0) + g["cantidad"]

        print("\nResumen    por categorías:")
        for cat, monto in categorias.items():
                print(f"{cat}: {monto}")


        guardar = input("¿Desea guardar el reporte en JSON? S/N: ")

        if guardar.lower() == "s":
                reporte_json = {
                "tipo": "semanal",
                "inicio": inicio,
                "final": final,
                "total": totall,
                "cantidad_gastos": cantidad,
                "categorias": categorias
                }

                ruta_semanal = os.path.join(base_dir, "reporte_semanal.json")

                with open(ruta_semanal, "w") as f:
                        json.dump(reporte_json, f, indent=4)

                print("Reporte semanal guardado correctamente")
        elif guardar.lower() == "n":
            print("entendido")
        else:
            print("accion no valida")
                
                
    
    elif opcion7==3:
        print("""=====================================================
REPORTE DE GASTOS MENSUALES
=========================================================""")
        mes= input("ingresa el mes de gasto (2026-03)")
        
        try:
            fecha_mes= datetime.strptime(mes, "%Y-%m")
        except ValueError:
            print("fecha mal colocada")
            return
        
        try:
            with open (ruta, "r") as f:
                datos= json.load(f)
        except FileNotFoundError:
            print("no encontrado")
            return
        
        reportes_mes=[]
        
        for g in datos:
            try:
                fecha_gasto2=datetime.strptime(g["fecha"], "%Y-%m-%d")
            except:
                continue
            if (fecha_gasto2.year == fecha_mes.year and 
                fecha_gasto2.month == fecha_mes.month):
                reportes_mes.append(g)
        
        if not reportes_mes:
            print("no hay gastos en ese mes")
            return
        total2=0
        
        for g in reportes_mes:
            total2+=g["cantidad"]
            
        cantidad=len(reportes_mes)
        
        
        print(f"\nMes: {mes}")
        print(f"Total gastado: {total2}")
        print(f"Número de gastos: {cantidad}")

        print("\nDetalles:")
        for g in reportes_mes:
            print("-------------------------------")
            print("Cantidad:", g["cantidad"])
            print("Categoría:", g["categoria"])
            print("Descripción:", g["descripcion"])
            
        categorias = {}
        for g in reportes_mes:
            cat = g["categoria"]
            categorias[cat] = categorias.get(cat, 0) + g["cantidad"]

        print("\nResumen por categorías:")
        for cat, monto in categorias.items():
            print(f"{cat}: {monto}")

        guardar = input("¿Desea guardar el reporte en JSON? S/N: ")

        if guardar.lower() == "s":
            reporte_json = {
                "mes": mes,
                "total": total2,
                "categorias": categorias
                }

            with open(ruta2, "w") as f:
                json.dump(reporte_json, f, indent=4)

            print("Reporte guardado correctamente")
        
        elif guardar.lower() == "n":
            print("entendido")
        else:
            print("accion no valida")
            

    elif opcion7==4:
        print("regresando al menu...")
        return
    else: 
        print("opcion no valida ")