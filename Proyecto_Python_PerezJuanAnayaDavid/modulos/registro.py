import json
from datetime import datetime
from config import ruta

 
def registrar_gastos():
    print(""" =============================================
            Registrar Nuevo Gasto
=============================================
Ingrese la información del gasto:

- Monto del gasto:
- Categoría (ej. comida, transporte, entretenimiento, otros):
- Descripción (opcional):

Ingrese ' S ' para guardar o ' C ' para cancelar.
=============================================""")
    
    opcion1= input("ingresa S o C: ")
    
    if opcion1.lower()== "s":
        try:
            cantidad= int(input("ingresa la cantidad: "))
        except ValueError:
            print("solo acepta numeros en su valor. ")
            return
        
        if cantidad <0:
            print("valor no aceptado la cantidad debe ser mayor a 0 y numeros positivos")
            

        print(""" =============================================
           registrar Categoria
=============================================
seleccione la categoria de su gasto:
1. transporte
2. comida 
3. entretenimiento
4. otros
""")
        
        categoria =["transporte", "comida", "entretenimiento","otros" ]
        try:
            opcion2= int(input("ingresa una categoria: "))
        except ValueError:
            print("el valor debe ser numerica: ")
            return
        
        if opcion2==1:
            categoria_elegida= categoria[0]
        elif opcion2==2:
            categoria_elegida= categoria[1]
        elif opcion2==3:
            categoria_elegida= categoria[2]
        elif opcion2==4:
             categoria_elegida= input("ingresa la categoria").strip().lower()
             if categoria_elegida=="":
                 print("eleccion no valida")
                 return
        else:
             print("accion no valida")
             return
        print("categoria elegida: ", categoria_elegida)
        
        print("""=============================================
           ¿desea ingresar alguna descripcion a su gasto? S/N
================================================""")
        
        opcion3= input("ingresa S o N")
        
        
        if opcion3.lower()=="s":
            descripcion= input("ingresa la descripcion")
            print("descripcion registrada")
            
        elif opcion3.lower()=="n":
            print("guardando datos...")
            descripcion=""
        else:
             print("opcion no valida")
             return
        fecha=datetime.now().strftime("%Y-%m-%d")
        gastos={
            "cantidad": cantidad,        
            "categoria": categoria_elegida,
            "descripcion": descripcion,
            "fecha": fecha
        }
        try:
         with open (ruta, "r") as f:
          datos=json.load(f)
        except:
         datos=[]
        datos.append(gastos)
        
        with open (ruta,"w") as f:
            json.dump(datos,f)
        
    elif opcion1.lower()== "c":
        print("regresando al menu...")
        return
    else:
        print("opcion no valida")