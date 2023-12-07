"""
Nicolas Sanchez
1H
42155002
"""

from funciones import *

while True:
    imprimir_menu()
    numero_ingresado = input("Ingresar un numero:  ")
    try:
        numero_ingresado_convertido = int(numero_ingresado)
    except Exception:
        print("Opcion incorrecta")
        limpiar_consola()
    else: 
        match numero_ingresado_convertido:
            case 1:
                nombre_y_posicion_jugadores()
            case 2:
                estadisticas_jugador_y_guardar_csv()
            case 4:
                mostrar_logros_jugador()
            case 5:
                promedio_y_ordenamiento_puntos_por_partido()
            case 6:
                salon_fama_jugadores()
            case 7:
                jugador_con_mas_rebotes()
            case 8:
                mostrar_nombre_y_promedio_descendente()
            case 9:
                porcentaje_jugadores_robos_y_bloqueos_totales()
            case 10:
                columna_posiciones()
            case 11:
                ("Fin del programa")
                break
            case _:
                print("Opción incorrecta")
        limpiar_consola()

