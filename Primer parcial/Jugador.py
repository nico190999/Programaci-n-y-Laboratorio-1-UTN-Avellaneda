from Estadisticas import *

class Jugador:
    def __init__(self, 
        diccionario_datos_jugador:dict):
        self.__logros = diccionario_datos_jugador.get("logros")
        self.__nombre = diccionario_datos_jugador.get("nombre")
        self.__posicion = diccionario_datos_jugador.get("posicion")
        self.__estadisticas = Estadisticas(diccionario_datos_jugador.get("estadisticas"))

    @property
    def get_nombre(self):
        return self.__nombre
    
    @property
    def get_nombre_y_puntos_por_partido(self):
        return f"{self.__nombre}, {self.__estadisticas.get_promedio_puntos_por_partido()}"

    @property
    def get_posicion(self):
        return self.__posicion

    @property
    def get_nombre_y_posicion_en_texto(self):
        return f"{self.__nombre} - {self.__posicion}"

    
    def get_estadisticas(self):
        return self.__estadisticas

    @property
    def get_estadisticas_en_texto(self):
        return self.__estadisticas.texto_estadisticas

    @property
    def get_logros(self):
        return self.__logros
    
    def get_logros_en_texto(self):
        contenido = ""
        bandera = True
        for logro in self.__logros:
            if bandera == True:
                contenido += f"{logro}"
                bandera = False
            else:
                contenido +=f"\n{logro}"
        return contenido
    
    def get_estadistica_temporadas(self):
        return self.__estadisticas.get_temporadas()
    
    def get_estadistica_puntos_totales(self):
        return self.__estadisticas.get_puntos_totales()

    def get_estadistica_puntos_por_partido(self):
        return self.__estadisticas.get_promedio_puntos_por_partido()
    
    def get_estadistica_rebotes_totales(self):
        return self.__estadisticas.get_rebotes_totales()
    
    def get_estadistica_promedio_rebotes_por_partido(self):
        return self.__estadisticas.get_promedio_rebotes_por_partido()
    
    def get_estadistica_asistencias_totales(self):
        return self.__estadisticas.get_asistencias_totales()
    
    def get_estadistica_promedio_asistencias_por_partido(self):
        return self.__estadisticas.get_promedio_asistencias_por_partido()
    
    def get_estadistica_robos_totales(self):
        return self.__estadisticas.get_robos_totales()
    
    def get_estadistica_bloqueos_totales(self):
        return self.__estadisticas.get_bloqueos_totales()
    
    def get_estadistica_get_porcentaje_tiros_de_campo(self):
        return self.__estadisticas.get_porcentaje_tiros_de_campo()
    
    def get_estadistica_porcentaje_tiros_libres(self):
        return self.__estadisticas.get_porcentaje_tiros_libres()
    
    def get_estadistica_porcentaje_tiros_triples(self):
        return self.__estadisticas.get_porcentaje_tiros_triples()
    
    def get_estadistica_diccionario_estadisticas(self):
        return self.__estadisticas.get_diccionario_estadisticas()
