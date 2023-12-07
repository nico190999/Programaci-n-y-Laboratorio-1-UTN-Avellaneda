import os
from Equipo import *
import re
import sqlite3

equipo = Equipo("dream_team.json")

def guardar_archivo_csv(nombre_archivo: str, contenido_a_guardar) -> bool:
    """
    La función se encarga de guardar nueva información en un archivo csv y/o crear uno a partir del contenido que le pasemos
    Recibe: str que corresponde al nombre del archivo, y como segundo parametro el contenido que se quiera guardar dentro de este
    Devuelve: bool True si se pudo guardar y caso contrario, False
    """
    try:
        nombre_archivo = f"{nombre_archivo}.csv"
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(contenido_a_guardar)
            print(f"Se creo el archivo: {nombre_archivo}")
            return True
    except Exception:
        print(f"Error al crear el archivo: {nombre_archivo}")
        return False

def guardar_archivo_json (nombre_archivo:str, contenido:dict):
    """
    La función se encarga de guardar nueva información en un archivo json y/o crear uno a partir del contenido que le pasemos
    Recibe: str que corresponde al nombre del archivo, y como segundo parametro el contenido que se quiera guardar dentro de este
    """
    try:
        with open (f"{nombre_archivo}.json", "w", encoding="utf-8") as archivo:
            json.dump(contenido, archivo, indent=2, ensure_ascii=False)
    except Exception:
        print("Error al guardar archivo json")
    else:
        print(f"Se creo el archivo {nombre_archivo}.json")

def guardar_sql(lista_jugadores:list[dict]):
    """
    La función se encarga de iterar la lista que le pasemos por parametro y obtenemos el valor correspondiente para añadirlo al SQL que posteriormente guardara en nuestro sistema. 
    Recibe: list[dict] que representa el diccionario de heroes
    """
    try:
        conn = sqlite3.connect('base_de_datos.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Jugadores (
                        id INTEGER PRIMARY KEY,
                        Nombre TEXT,
                        Posición TEXT,
                        Temporadas INTEGER,
                        Puntos_totales INTEGER,
                        Promedio_puntos_por_partido REAL,
                        Rebotes_totales REAL,
                        Promedio_rebotes_por_partido REAL,
                        Asistencias_totales REAL,
                        Promedio_asistencias_por_partido REAL,
                        Robos_totales REAL,
                        Bloqueos_totales REAL,
                        Porcentaje_tiros_de_campo REAL,
                        Porcentaje_tiros_libres REAL,
                        Porcentaje_tiros_triples REAL
                        )''')
        for jugador in lista_jugadores:
            cursor.execute('INSERT INTO Jugadores (Nombre, Posición, Temporadas, Puntos_totales, Promedio_puntos_por_partido, Rebotes_totales, Promedio_rebotes_por_partido, Asistencias_totales, Promedio_asistencias_por_partido, Robos_totales, Bloqueos_totales, Porcentaje_tiros_de_campo, Porcentaje_tiros_libres, Porcentaje_tiros_triples) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (jugador.get_nombre,jugador.get_posicion, jugador.get_estadistica_temporadas(), jugador.get_estadistica_puntos_totales(),jugador.get_estadistica_puntos_por_partido(), jugador.get_estadistica_rebotes_totales(), jugador.get_estadistica_promedio_rebotes_por_partido(), jugador.get_estadistica_asistencias_totales(), jugador.get_estadistica_promedio_asistencias_por_partido(), jugador.get_estadistica_robos_totales(), jugador.get_estadistica_bloqueos_totales(), jugador.get_estadistica_get_porcentaje_tiros_de_campo(), jugador.get_estadistica_porcentaje_tiros_libres(), jugador.get_estadistica_porcentaje_tiros_triples()))
        conn.commit()
        conn.close()
    except Exception:
        print("Error al crear el archivo SQL")
    else:
        print("Se creo el archivo")

def imprimir_menu ():
    """
    La función se encarga de la impresión del menu de enunciados.
    """
    menu = \
    """
1 -  Mostrar la lista de todos los jugadores del Dream Team. Con el formato:
Nombre Jugador - Posición. Ejemplo:
Michael Jordan - Escolta
2 - Permitir al usuario seleccionar un jugador por su índice (validar con regex) y mostrar sus estadísticas completas, incluyendo temporadas jugadas, puntos totales, promedio de puntos por partido, rebotes totales, promedio de rebotes por partido, asistencias totales, promedio de asistencias por partido, robos totales, bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.
3 - Después de mostrar las estadísticas de un jugador seleccionado por el usuario, permite al usuario guardar las estadísticas de ese jugador en un archivo CSV. El archivo CSV debe contener los siguientes campos: nombre, posición, temporadas, puntos totales, promedio de puntos por partido, rebotes totales, promedio de rebotes por partido, asistencias totales, promedio de asistencias por partido, robos totales, bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.
4 - Permitir al usuario buscar un jugador por su nombre (validar con regex) y mostrar sus logros, como campeonatos de la NBA, participaciones en el All-Star y pertenencia al Salón de la Fama del Baloncesto, etc.
5 - Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente.
6 - Permitir al usuario ingresar el nombre de un jugador (validar con regex) y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto.
7 - Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.
8 - A) Ordenar el listado de manera descendente(el mayor arriba) y mostrar el
listado.
B) Permitir guardar este listado ordenado en un archivo CSV con su
apellido.csv
C) Permitir guardar este listado ordenado en un archivo JSON y permitir al
usuario ingresar el nombre del archivo a guardar (validar con regex)
9 - Ordenar los datos por el jugador que sumando los robos totales más
los bloqueos totales ("robos_totales" + "bloqueos_totales").
A) ordenar los jugadores por el valor sumado.
B)listar todos los jugadores ordenados y mostrar el porcentaje de este valor
sumado tomando como 100% el valor máximo
C) crear un filtro que permita ingresar un valor y que solo muestre esa
cantidad de jugadores ordenados por la suma de los dos campos
10 - Crear la tabla posiciones, (solo contenga las posiciones válidas)
que se deben cargar con las posiciones que aparecen en el listado de jugadores en
una función desarrollada por ustedes
11 - Salir
    """
    print(menu)


def limpiar_consola():
    '''
    Imprimir msj que al presionar tecla limpia la consola.
    Recibe: nada
    Devuelve: nada
    '''
    _ = input("Presiona una tecla para continuar")
    if os.name in ["ce", "nt", "dos"]:
        os.system("cls")
    else:
        os.system("clear")


def validacion_regex_numero(numero:int) -> bool:
    """
    La función se encarga de validar que lo que se ingreso por parametro son caracteres numericos
    Recibe: numero int
    Devuelve: bool True si se ingresaron caracteres números, caso contrario False
    """
    patron_regex = "^[0-9]+$"
    if re.match(patron_regex, numero):
        return True
    else:
        return False


def validacion_regex_nombre(nombre:str) -> bool:
    """
    La función se encarga de validar que los caracteres que se ingresaron sean letras y contenga espacios
    Recibe: str que se sometera a la evaluación por regex
    Devuelve: bool True si se ingresaron caracteres letras y espacios, caso contrario False 
    """
    patron_regex = r"^[a-zA-Z\s]+$"
    if re.match(patron_regex, nombre):
        return True
    else:
        return False


def crear_lista_formato_json(lista_jugadores:list[dict]) -> dict:
    """
    La función se encarga de transformar la lista que se pase como parametro en un json, tomando todos los datos correspondientes. 
    Recibe: list[dict] que representa la lista de heroes
    Devuelve: dict la lista tranformada en json
    """
    data = {"equipo": "Dream Team"}
    data["jugadores"] = []
    for jugador in lista_jugadores:
        diccionario_jugador = {}
        diccionario_jugador["nombre"] = jugador.get_nombre
        diccionario_jugador["posicion"] = jugador.get_posicion
        diccionario_jugador["estadisticas"] = {}
        diccionario_jugador["estadisticas"]["temporadas"] = jugador.get_estadistica_temporadas()
        diccionario_jugador["estadisticas"]["puntos_totales"] = jugador.get_estadistica_puntos_totales()
        diccionario_jugador["estadisticas"]["promedio_puntos_por_partido"] = jugador.get_estadistica_puntos_por_partido()
        diccionario_jugador["estadisticas"]["rebotes_totales"] = jugador.get_estadistica_rebotes_totales()
        diccionario_jugador["estadisticas"]["promedio_rebotes_por_partido"] = jugador.get_estadistica_promedio_rebotes_por_partido()
        diccionario_jugador["estadisticas"]["asistencias_totales"] = jugador.get_estadistica_asistencias_totales()
        diccionario_jugador["estadisticas"]["promedio_asistencias_por_partido"] = jugador.get_estadistica_promedio_asistencias_por_partido()
        diccionario_jugador["estadisticas"]["robos_totales"] = jugador.get_estadistica_robos_totales()
        diccionario_jugador["estadisticas"]["bloqueos_totales"] = jugador.get_estadistica_bloqueos_totales()
        diccionario_jugador["estadisticas"]["porcentaje_tiros_de_campo"] = jugador.get_estadistica_get_porcentaje_tiros_de_campo()
        diccionario_jugador["estadisticas"]["porcentaje_tiros_libres"] = jugador.get_estadistica_porcentaje_tiros_libres()
        diccionario_jugador["estadisticas"]["porcentaje_tiros_triples"] = jugador.get_estadistica_porcentaje_tiros_triples()
        diccionario_jugador["logros"] = jugador.get_logros
        data["jugadores"].append(diccionario_jugador)
    return data


#Punto 1
def nombre_y_posicion_jugadores():
    """
    Se encarga de iterar la lista de jugadores e imprimir por pantalla su nombre y posición
    """
    equipo.get_nombre_y_posicion_()

#Punto 2 y 3
def estadisticas_jugador_y_guardar_csv():
    """
    La función se encarga de solicitar al usuario que escriba el número del indice de uno de los jugadores, posterior a esto, mostrara sus estadisticas y preguntara al usuario si quiere guardar dichas estadisticas en un archivo CSV con su formato correspondiente
    """
    indice = input("Ingresar indice de jugador:  ")
    if validacion_regex_numero(indice) == True:
        indice_entero = int(indice)
        if indice_entero >= 0 and indice_entero < equipo.cantidad_jugadores():
            texto_jugador_y_posicion = equipo.obtener_nombre_jugador_y_posicion(indice_entero)
            texto_estadisticas = equipo.datos_estadistica_por_indice(indice_entero)
            texto_logros = equipo.mostrar_logros_por_indice(indice_entero)
            texto_concatenado = f"{texto_jugador_y_posicion}\n{texto_estadisticas}\n{texto_logros}"
            print(texto_concatenado)
            respuesta_guardar_archivo = input("¿Queres guardar el archivo en CSV? s/n:  ")
            if respuesta_guardar_archivo == "s":
                contenido = equipo.obtener_datos_jugador_en_texto_csv_por_indice(indice_entero)
                guardar_archivo_csv(f"datos_jugador_del_indice_{indice_entero}", contenido)
        else:
            print("Numero ingresado fuera de rango, intente nuevamente")
    else:
        print("Opción incorrecta, ingresa solo caracteres númericos")

#Punto 4
def mostrar_logros_jugador():
    """
    La función se encarga de solicitar al usuario que ingrese el nombre de un jugador, si este coincide con uno de los jugadores del equipo, se mostraran los logros de ese por pantalla.
    """
    nombre_ingresado = input("Ingresar nombre del jugador:  ")
    if validacion_regex_nombre(nombre_ingresado) == True:
        print(equipo.mostrar_logros_por_nombre(nombre_ingresado))

#Punto 5
def promedio_y_ordenamiento_puntos_por_partido ():
    """
    La función se encarga de calcular el promedio de puntos por partido del equipo, una vez hecho esto ordena a los jugadores por nombre de manera ascendente (a-z) y también puntaje. Junto al nombre de cada jugador, estará su promedio de puntos por partido.
    """
    print(f"El promedio de puntos por partido del equipo dream team es de {equipo.promedio_puntos_por_partido():.2f}")
    print("Orden por nombre de manera ascendente (a-z):")
    for jugador in equipo.quick_sort_nombre_ascendente(equipo.jugadores):
        print(jugador.get_nombre_y_puntos_por_partido)
    print("\nOrden por promedio puntos por partido de manera ascendente:")
    for jugador in equipo.quick_sort(equipo.jugadores, "ascendente", "promedio_puntos_por_partido"):
        print(jugador.get_nombre_y_puntos_por_partido)

#Punto 6
def salon_fama_jugadores():
    """
    La función se encargará de solicitar al usuario que ingrese el nombre de uno de los jugadores e informara si este pertene al Salón de la fama del baloncesto
    """
    nombre_ingresado = input("Ingresar nombre del heroe:  ")
    if nombre_ingresado in equipo.lista_de_nombres():
        print(equipo.validacion_salon_fama(nombre_ingresado))
    else:
        print(f"El nombre ingresado no pertenece a uno de los miembros del equipo")

#Punto 7
def jugador_con_mas_rebotes():
    """
    La función muestra el nombre del jugador con mayor cantidad de rebotes del equipo
    """
    print(f"El jugador que realizo más rebotes es {equipo.mayor_cantidad_rebotes_totales().get_nombre}")

#Punto 8
def mostrar_nombre_y_promedio_descendente():
    """
    La función se encarga de ordenar a los jugadores por promedio de puntos de manera descendente e imprimir el nombre del jugador junto a su puntaje correspondiente. Una vez hecho esto consulta al usuario si desdea guardar el archivo completo de los jugadores en un json y csv. En caso escriba 's', se guardaran los archivos con su formato correspondiente
    """
    contenido = "Jugador, Promedio puntos por partido\n"
    bandera = True
    lista_jugadores_descendente = equipo.quick_sort(equipo.jugadores, "descendente", "promedio_puntos_por_partido")
    for jugador in lista_jugadores_descendente:
        if bandera == True:
            contenido += f"{jugador.get_nombre_y_puntos_por_partido}"
            bandera = False
        else:
            contenido += f"\n{jugador.get_nombre_y_puntos_por_partido}"
    print(contenido)
    respuesta_guardar_archivo_sql = input("¿Queres guardar el archivo en SQL? s/n:  ")
    if respuesta_guardar_archivo_sql == "s":
        guardar_sql(lista_jugadores_descendente)
    respuesta_guardar_archivo_csv = input("¿Queres guardar el archivo en CSV? s/n:  ")
    if respuesta_guardar_archivo_csv == "s":
        datos_formato_csv = equipo.obtener_datos_jugador_en_texto_csv_por_lista(lista_jugadores_descendente)
        guardar_archivo_csv("Sanchez", datos_formato_csv)
    respuesta_guardar_archivo_json = input("¿Queres guardar el archivo en Json? s/n:  ")
    if respuesta_guardar_archivo_json == "s":
        nombre_ingresado_archivo = input("Ingresar nombre del archivo Json:  ")
        if validacion_regex_nombre(nombre_ingresado_archivo) == True:
            lista_formato_json = crear_lista_formato_json(lista_jugadores_descendente)
            guardar_archivo_json(nombre_ingresado_archivo, lista_formato_json)
    

#Punto 9
def porcentaje_jugadores_robos_y_bloqueos_totales():
    """
    La función se encarga de ordenar los jugadores de menor a mayor por la suma de sus robos y bloqueos totales, mostrar el porcentaje que tienen a comparación del valor máximo y mostrar por pantalla la cantidad de jugadores que el usuario ingrese
    """
    lista_ordenada_robos_y_bloqueos_totales = equipo.quick_sort(equipo.jugadores, "ascendente", "robos_totales_y_bloqueos_totales")
    valor_maximo_suma_bloqueos_y_robos = (lista_ordenada_robos_y_bloqueos_totales[-1].get_estadistica_robos_totales() + lista_ordenada_robos_y_bloqueos_totales[-1].get_estadistica_bloqueos_totales())
    contenido_lista =[]
    for jugador in lista_ordenada_robos_y_bloqueos_totales:
        valor_robos_totales = jugador.get_estadistica_robos_totales()
        valor_bloqueos_totales = jugador.get_estadistica_bloqueos_totales()
        suma_robos_bloqueos_totales = valor_robos_totales + valor_bloqueos_totales
        porcentaje = (suma_robos_bloqueos_totales / valor_maximo_suma_bloqueos_y_robos) * 100
        valor_nombre = jugador.get_nombre
        contenido_lista.append(f"{valor_nombre}, {porcentaje:.2f}%")
    numero_jugadores_a_imprimir = int(input(f"Ingresar la cantidad de jugadores que quieres imprimir entre 1 y {len(contenido_lista)}:  "))
    for jugador in contenido_lista[:numero_jugadores_a_imprimir]:
        print(jugador)

#Punto 10
def columna_posiciones():
    """
    La función se encarga de almacenar en una columna la lista de posiciones en forma de str, como función extra, se muestra por pantalla
    """
    contenido = "nombre_posicion"
    lista_posiciones = []
    for jugador in equipo.jugadores:
        valor_posicion = jugador.get_posicion
        if valor_posicion not in lista_posiciones:
            lista_posiciones.append(valor_posicion)
    for posicion in lista_posiciones:
        contenido += f"\n{posicion}"
    print(contenido)