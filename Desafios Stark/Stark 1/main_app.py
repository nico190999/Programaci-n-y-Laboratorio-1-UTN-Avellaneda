from funciones import *

'''
Nicolas Sanchez
42155002
1H
'''

def main_app (lista_heroes: list):
    while True:

        menu = "A - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M\nB - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F\nC - Recorrer la lista y determinar cuál es el superhéroe más alto de género M\nD - Recorrer la lista y determinar cuál es el superhéroe más alto de género F\nE - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M\nF - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F\nG - Recorrer la lista y determinar la altura promedio de los  superhéroes de género M\nH - Recorrer la lista y determinar la altura promedio de los  superhéroes de género F\nI - Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)\nJ - Determinar cuántos superhéroes tienen cada tipo de color de ojos.\nK - Determinar cuántos superhéroes tienen cada tipo de color de pelo\nL - Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).\nM - Listar todos los superhéroes agrupados por color de ojos.\nN - Listar todos los superhéroes agrupados por color de pelo.\nO - Listar todos los superhéroes agrupados por tipo de inteligencia"

        print(menu)

        opcion_ingresada = input("Ingrese una letra:  ")
        opcion_ingresada = opcion_ingresada.upper()

        match opcion_ingresada:
            case "A":
                resultado = imprimir_nombre_genero_m(lista_personajes)
            case "B":
                resultado = imprimir_nombre_genero_f(lista_personajes)
            case "C":
                resultado = determinar_heroe_alto_genero_m(lista_personajes)
                print(f"C - El heroe más alto del genero másculino es {resultado}")
            case "D":
                resultado = determinar_heroe_alto_genero_f(lista_personajes)
                print(f"D - El heroe más alto del genero femenino es {resultado}")
            case "D":
                resultado = determinar_heroe_alto_genero_f(lista_personajes)
                print(f"D - El heroe más alto del genero femenino es {resultado}")
            case "E":
                resultado = determinar_heroe_bajo_genero_m(lista_personajes)
                print(f"E - El heroe más bajo del genero másculino es {resultado}")
            case "F":
                resultado = determinar_heroe_bajo_genero_f(lista_personajes)
                print(f"F - El heroe más bajo del genero femenino es {resultado}")
            case "G":
                resultado = determinar_promedio_genero_m(lista_personajes)
                print(f"G - El promedio de altura de los heroes del genero masculino es de {resultado}")
            case "H":
                resultado = determinar_promedio_genero_f(lista_personajes)
                print(f"H - El promedio de altura de los heroes del genero femenino es de {resultado}")
            case "I":
                resultado = informar_nombre_heroe_y_valor(lista_personajes)
                print(resultado)
            case "J":
                resultado = informar_cantidad_heroes_color_ojos(lista_personajes)
                print(resultado)
            case "K":
                resultado = informar_cantidad_heroes_color_pelo(lista_personajes)
                print(resultado)
            case "L":
                resultado = informar_cantidad_heroes_inteligencia(lista_personajes)
                print(resultado)
            case "M":
                resultado = imprimir_lista_heroes_por_color_ojos (lista_personajes)
                print(resultado)
            case "N":
                resultado = imprimir_lista_heroes_por_color_pelo (lista_personajes)
                print(resultado)
            case "O":
                resultado = imprimir_lista_heroes_por_inteligencia (lista_personajes)
                print(resultado)
            case _:
                print("Opcion incorrecta, ingresar letra nuevamente")

main_app(lista_personajes)