class Estadisticas:
    def __init__(self, diccionario_estadisticas:dict):
        self.__temporadas = diccionario_estadisticas.get("temporadas")
        self.__puntos_totales = diccionario_estadisticas.get("puntos_totales")
        self.__promedio_puntos_por_partido = diccionario_estadisticas.get("promedio_puntos_por_partido")
        self.__rebotes_totales = diccionario_estadisticas.get("rebotes_totales")
        self.__promedio_rebotes_por_partido = diccionario_estadisticas.get("promedio_rebotes_por_partido")
        self.__asistencias_totales = diccionario_estadisticas.get("asistencias_totales")
        self.__promedio_asistencias_por_partido = diccionario_estadisticas.get("promedio_asistencias_por_partido")
        self.__robos_totales = diccionario_estadisticas.get("robos_totales")
        self.__bloqueos_totales = diccionario_estadisticas.get("bloqueos_totales")
        self.__porcentaje_tiros_de_campo = diccionario_estadisticas.get("porcentaje_tiros_de_campo")
        self.__porcentaje_tiros_libres = diccionario_estadisticas.get("porcentaje_tiros_libres")
        self.__porcentaje_tiros_triples = diccionario_estadisticas.get("porcentaje_tiros_triples")
        self.__keys_estadisticas = list(diccionario_estadisticas.keys())
        self.__valores_estadisticas = list(diccionario_estadisticas.values())
    
    @property
    def texto_estadisticas(self):
        contenido = f"""Temporadas: {self.__temporadas}
Puntos totales: {self.__puntos_totales}
Promedio puntos por partido: {self.__promedio_puntos_por_partido}
Rebotes totales: {self.__rebotes_totales}
Promedio rebotes por partido: {self.__promedio_rebotes_por_partido}
Asistencias totales: {self.__asistencias_totales}
Promedio asistencias por partido: {self.__promedio_asistencias_por_partido}
Robos totales: {self.__robos_totales}
Bloqueos totales: {self.__bloqueos_totales}
Porcentaje tiros de campo: {self.__porcentaje_tiros_de_campo}
Porcentaje tiros libres: {self.__porcentaje_tiros_libres}
Porcentaje tiros triples: {self.__porcentaje_tiros_triples}"""
        return contenido

    def get_temporadas(self):
        return self.__temporadas
    
    def get_puntos_totales(self):
        return self.__puntos_totales
    
    def get_promedio_puntos_por_partido(self):
        return self.__promedio_puntos_por_partido

    def get_rebotes_totales(self):
        return self.__rebotes_totales
    
    def get_promedio_rebotes_por_partido(self):
        return self.__promedio_rebotes_por_partido
    
    def get_asistencias_totales(self):
        return self.__asistencias_totales
    
    def get_promedio_asistencias_por_partido(self):
        return self.__promedio_asistencias_por_partido
    
    def get_robos_totales(self):
        return self.__robos_totales
    
    def get_bloqueos_totales(self):
        return self.__bloqueos_totales
    
    def get_porcentaje_tiros_de_campo(self):
        return self.__porcentaje_tiros_de_campo
    
    def get_porcentaje_tiros_libres(self):
        return self.__porcentaje_tiros_libres
    
    def get_porcentaje_tiros_triples(self):
        return self.__porcentaje_tiros_triples
        
    def get_keys_estadisticas(self):
        return self.__keys_estadisticas
        
    def get_values_estadisticas(self):
        return self.__valores_estadisticas