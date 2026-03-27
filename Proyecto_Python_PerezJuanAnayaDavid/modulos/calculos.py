import json
from datetime import datetime
from config import ruta

        
        
def calcular_total():
    print("""=============================================
          Calcular Total de Gastos
=============================================
Seleccione el período de cálculo:

1. Calcular total diario
2. Calculadora total semanal
3. Calculadora total mensual
4. Regresar al menú principal
=============================================""")
    try:
        opcion= int(input("ingresa una opcion: "))
    except ValueError:
        print("el valor no es valido")
        return
    
    if opcion == 1:
        fechass= input("ingresa la fecha que quieras ver: (%Y-%m-%d)")
        
        try:
            datetime.strptime(fechass, "%Y-%m-%d")
        except ValueError:
            print("fecha no valida")
            return

        try:
          with open(ruta, "r") as f:
            datos = json.load(f)
        except:
         print("no hay datos")
         return

        total = 0

        for g in datos:
            if g.get("fecha") == fechass:
                total += g["cantidad"]
        print("el total de gasto de ese dia es:", total)
    
    elif opcion==2:
        inicio= input("ingresa la fecha de inicio de la semana: (%Y-%m-%d)")
        final= input("ingresa el final de la semana: (%Y-%m-%d) ")  
    
        try:
            fecha_inicio= datetime.strptime(inicio, "%Y-%m-%d")
            fecha_final= datetime.strptime(final, "%Y-%m-%d")
        except ValueError:
            print("fecha no valida")
            return
    
        try: 
            with open (ruta, "r") as f:
             datos= json.load(f)
        except FileNotFoundError:
            print("no hay datos")
            return
    
        total1= 0
    
        for g in datos:
            try:
                fecha_gasto = datetime.strptime(g["fecha"], "%Y-%m-%d")
            except:
                continue
        
            if fecha_inicio <= fecha_gasto <= fecha_final:
                total1+= g["cantidad"]
        print("el total de la semana es de: ", total1)
    
    elif opcion==3:
        mes= input("ingresa el mes que quieras poner en numero: (2026-03) ")
        try:
            fecha_mes= datetime.strptime(mes, "%Y-%m")
        except ValueError:
            print("esta mal escrito vuelve a intentar...")
            return
            
        try:
            with open (ruta, "r") as f:
                datos= json.load(f)
        except FileNotFoundError:
            print("no encontrado")
            return
        
        total_mes= 0
        
        for g in datos:
            try:
                fecha_gasto = datetime.strptime(g["fecha"], "%Y-%m-%d")
            except:
                continue
            
            
            
            if (fecha_gasto.year == fecha_mes.year and 
                fecha_gasto.month == fecha_mes.month):
                total_mes += g["cantidad"]

        print("el total del mes es:", total_mes)
     
    elif opcion==4:
        print("regresando al menu principal...")
        return
    else:
        print("opcion no valida...")