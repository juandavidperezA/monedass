from modulos.registro import registrar_gastos
from modulos.lista import lista_gasto
from modulos.calculos import calcular_total
from modulos.reportes import generar_reporte
from modulos.monedas import recalcular_multimoneda
def menu():
    while True:
        try:
         print("""=============================================
         Simulador de Gasto Diario
=============================================
Seleccione una opción:

1. Registrar nuevo gasto
2. Listar gastos
3. Calcular total de gastos
4. Generar reporte de gastos
5. recalcular multimoneda
5. Salir
=============================================""")
         opcion= int(input("ingresa un opcion: "))
         if opcion== 1:
            registrar_gastos()
         elif opcion== 2:
            lista_gasto()
         elif opcion==3:
            calcular_total()
         elif opcion==4:
             generar_reporte()
         elif opcion== 5:
            recalcular_multimoneda()
         elif opcion== 6:
            opcion1= input("¿quieres salir del programa? S/N")
            if opcion1.lower()== "s":
                print("saliendo del programa...")
                break
            elif opcion1.lower()=="n":
                print("continuando...")
            else:
                print("accion no valida")
         else:
             print("accion no valida")       
    
        except ValueError as e:
            print(f"OCURRIO UN ERROR DE TIPO {e}") 
            
menu()