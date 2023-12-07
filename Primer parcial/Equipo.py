import json
from Jugador import *

class Equipo:
    def __init__(self, archivo:str):
        self.lista_jugadores_original = self.leer_archivo(archivo)
        self.jugadores = [Jugador(jugador) for jugador in self.lista_jugadores_original]

    #metodos
    def leer_archivo(self, nombre_archivo):
        """
        La función se encarga de la lectura del archivo que pasemos por parametro y extraer el valor de la clave "jugadores"
        Recibe: self, str que correponde al nombre del archivo
        Devuelve: list[dict]
        """
        try:
            with open(nombre_archivo, "r", encoding = "utf-8") as archivo:
                archivo_cargado = json.load(archivo)
                lista_jugadores_uno = archivo_cargado.get("jugadores", "no se obtuvo lista de jugadores")
                return lista_jugadores_uno
        except Exception:
            print(f"Error al intentar leer el archivo {nombre_archivo}")
        
    def lista_de_nombres(self) -> list:
        """
        La función se encarga de almacenar los nosmbres de los jugadores en una lista
        Recibe: self
        Devuelve: list lista de nombres de los jugadores 
        """
        lista_nombres_jugadores = [jugador.get_nombre for jugador in self.jugadores]
        return lista_nombres_jugadores
    
    def get_solo_nombre(self):
        return self.jugadores.get_nombre
    
    def get_solo_estadistica_promedio_puntos_por_partido(self):
        return self.jugador.get_estadisticas().get_promedio_puntos_por_partido()

    def get_nombres(self):
        """
        La función se encarga de imprimir por pantalla los nombres de los jugadores de la lista de jugadores
        Recibe: self
        """
        for jugador in self.jugadores:
            print(jugador.get_nombre())

    def get_nombre_y_posicion_(self):
        """
        La función se encargara de imprimir el nombre y la posición concatenado en un texto especifico de los jugadores a partir de la lista de jugadores
        Recibe: self
        """
        for jugador in self.jugadores:
            print(jugador.get_nombre_y_posicion_en_texto)

    def obtener_nombre_jugador_y_posicion(self, indice:int):
        """
        La funcion se encarga de obtener los valores nombre y posicion de un jugador especifico a través de su indice y retornarlo en forma de un texto especifico
        Recibe: self
        """
        valor_nombre = self.jugadores[indice].get_nombre
        valor_posicion = self.jugadores[indice].get_posicion
        return f"{valor_nombre}\n{valor_posicion}"

    def datos_estadistica_por_indice(self, indice:int):
        """
        La función se encarga de tomar las estadisticas de un jugador a través de su indice y retornarlo
        """
        valor_estadistica = self.jugadores[indice].get_estadisticas_en_texto
        return valor_estadistica

    def mostrar_logros_por_nombre(self, nombre_jugador:str):
        """
        La función se encargara de devolcer los losgros en forma de texto str del nombre del jugador que coincida con el que se pasa por parametro
        """
        for jugador in self.jugadores:
            if nombre_jugador == jugador.get_nombre:
                return jugador.get_logros_en_texto()
            
    def mostrar_logros_por_indice(self, indice:int):
        """
        La función se encargara de devolcer los losgros en forma de texto str del indice que coincida con el que se pasa por parametro
        Recibe: self, int que representa el indice
        """
        logros = self.jugadores[indice].get_logros_en_texto()
        return logros

    def validacion_salon_fama (self, nombre_ingresado:str):
        """
        La función se encarga de verificar si el nombre del jugador ingresado por parametro pertenece a el Salon de la Fama del Baloncesto
        Recibe: self
        """
        lista_de_logros_jugador = []
        for jugador in self.jugadores:
            if nombre_ingresado == jugador.get_nombre:
                lista_de_logros_jugador = jugador.get_logros
        if "Miembro del Salon de la Fama del Baloncesto" in lista_de_logros_jugador:
            return "El jugador es miembro del Salon de la Fama del Baloncesto"
        else:
            return "El jugador NO es miembro del Salon de la Fama del Baloncesto"
        
    def obtener_datos_jugador_en_texto_csv_por_indice(self, indice:int):
        """
        La funcion se encarga de concatenar en forma de texto las estadisticas del jugador, tanto sus keys como valores, en la forma que se solicita para el formato csv. Toma los datos del jugador correpsondiente a partir del indice ingresado
        Recibe: self, int que representa el indice del jugador de la lista
        """
        valor_nombre = self.jugadores[indice].get_nombre
        valor_posicion = self.jugadores[indice].get_posicion
        contenido = "Nombre, Posicion"
        lista_keys_estadisticas = self.jugadores[indice].get_estadisticas().get_keys_estadisticas()
        lista_capitalizada = [key.capitalize() for key in lista_keys_estadisticas]
        for estadistica in lista_capitalizada:
            contenido += f", {estadistica}"
        contenido = contenido.replace("_", " ")
        contenido += f"\n{valor_nombre}, {valor_posicion}"
        lista_values_estadisticas = self.jugadores[indice].get_estadisticas().get_values_estadisticas()
        for valor in lista_values_estadisticas:
            contenido += f", {valor}"
        return contenido
    
    def obtener_datos_jugador_en_texto_csv_por_lista(self, lista_jugadores:list[dict]):
        """
        La función se encarga de 
        """
        contenido = "Nombre, Posición"
        lista_keys_estadisticas = lista_jugadores[0].get_estadisticas().get_keys_estadisticas()
        lista_capitalizada = [key.capitalize() for key in lista_keys_estadisticas]
        for estadistica in lista_capitalizada:
            contenido += f", {estadistica}"
        contenido = contenido.replace("_", " ")
        for jugador in lista_jugadores:
            valor_nombre = jugador.get_nombre
            valor_posicion = jugador.get_posicion
            contenido += f"\n{valor_nombre}, {valor_posicion}"
            lista_values_estadisticas = jugador.get_estadisticas().get_values_estadisticas()
            for valor in lista_values_estadisticas:
                contenido += f", {valor}"
        return contenido


    def mayor_cantidad_rebotes_totales(self):
        """
        La función se encarga de calcular cual es el jugador que tiene mayor cantidad de reobotes totales de la lista de jugadores
        Recibe: self
        """
        flag_max = True
        for jugador in self.jugadores:
            if flag_max == True:
                valor_maximo_rebote = jugador.get_estadistica_rebotes_totales()
                jugador_con_mas_rebotes = jugador
                flag_max = False
            else:
                if jugador.get_estadistica_rebotes_totales() > valor_maximo_rebote:
                    valor_maximo_rebote = jugador.get_estadistica_rebotes_totales()
                    jugador_con_mas_rebotes = jugador
        return jugador_con_mas_rebotes
    
    def cantidad_jugadores(self):
        """
        La función se encarga de calcular y retornar la longitud de la lista de jugadores
        Recibe: self
        """
        return len(self.jugadores)
    
    def promedio_puntos_por_partido (self):
        """
        La función se encarga de calcular el promedio de los puntos por partido de la lista de jugadores
        Recibe: self
        """
        acmulador_puntos_por_partido = 0
        for jugador in self.jugadores:
            acmulador_puntos_por_partido += jugador.get_estadistica_puntos_por_partido()
        promedio_puntos_por_partido = acmulador_puntos_por_partido / len(self.jugadores)
        return promedio_puntos_por_partido

    def quick_sort_nombre_ascendente(self, lista_jugadores:list[dict]):
        """
        La función se encarga de ordenar la lista de manera ascendente (a-z) la lista de jugadores
        Recibe: self, list[dict] que representa la lista de jugadores
        """
        if len(lista_jugadores) < 2:
            return lista_jugadores
        else:
            lista_copia = lista_jugadores.copy()
            pivot = lista_copia.pop()
            mas_grandes = []
            mas_chicos = []
            for jugador in lista_copia:
                if jugador.get_nombre > pivot.get_nombre:
                    mas_grandes.append(jugador)
                elif jugador.get_nombre <= pivot.get_nombre:
                    mas_chicos.append(jugador)
            return self.quick_sort_nombre_ascendente(mas_chicos) + [pivot] + self.quick_sort_nombre_ascendente(mas_grandes)

    def quick_sort(self, lista_jugadores:list[dict], calculo_a_realizar:str, dato_a_evaluar:str):
        """
        La función se encarga de ordenar la lista del modo y dato que se pase por parametro.
        Recibe: self, list[dict] que representa la lista de jugadores, calculo_a_realizar ascendente o descendente
        """
        if len(lista_jugadores) < 2:
            return lista_jugadores
        else:
            lista_copia = lista_jugadores.copy()
            pivot = lista_copia.pop()
            derecha = []
            izquierda = []
            for jugador in lista_copia:
                if calculo_a_realizar == "ascendente":
                    if dato_a_evaluar == "promedio_puntos_por_partido":
                        if jugador.get_estadistica_puntos_por_partido() > pivot.get_estadistica_puntos_por_partido():
                            derecha.append(jugador)
                        elif jugador.get_estadistica_puntos_por_partido() <= pivot.get_estadistica_puntos_por_partido():
                            izquierda.append(jugador)
                    elif dato_a_evaluar == "robos_totales_y_bloqueos_totales":
                        if ((jugador.get_estadistica_robos_totales()) + (jugador.get_estadistica_bloqueos_totales())) > ((pivot.get_estadistica_robos_totales()) + (pivot.get_estadistica_bloqueos_totales())):
                            derecha.append(jugador)
                        elif ((jugador.get_estadistica_robos_totales()) + (jugador.get_estadistica_bloqueos_totales())) <= ((pivot.get_estadistica_robos_totales()) + (pivot.get_estadistica_bloqueos_totales())):
                            izquierda.append(jugador)
                elif calculo_a_realizar == "descendente":
                    if dato_a_evaluar == "promedio_puntos_por_partido":
                        if jugador.get_estadistica_puntos_por_partido() <= pivot.get_estadistica_puntos_por_partido():
                            derecha.append(jugador)
                        elif jugador.get_estadistica_puntos_por_partido() > pivot.get_estadistica_puntos_por_partido():
                            izquierda.append(jugador)
            return self.quick_sort(izquierda, calculo_a_realizar, dato_a_evaluar) + [pivot] + self.quick_sort(derecha, calculo_a_realizar, dato_a_evaluar)