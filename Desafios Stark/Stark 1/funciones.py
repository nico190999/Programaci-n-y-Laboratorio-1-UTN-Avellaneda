from data_stark import lista_personajes
'''
Nicolas Sanchez 
42155002
1H
'''
'''
A - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
'''

def imprimir_nombre_genero_m(lista_heroes: list) -> str:
    '''
    Iterar, determinar e imprimir los nombres de los heroes de genero masculino de la lista de diciconarios
    Recibe: Lista de diccionarios
    Devuelve: str, nombre de los heroes de genero masculino
    '''
    for heroe in lista_heroes:
        valor_de_clave_genero = heroe.get("genero")
        if valor_de_clave_genero == "M":
            nombre = heroe.get("nombre")
            print(nombre)


'''
B - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
'''
def imprimir_nombre_genero_f (lista_heroes: list) -> str:
    '''
    Iterar, determinar e imprimir los nombres de los heroes de genero femenino de la lista de diciconarios
    Recibe: Lista de diccionarios
    Devuelve: str, nombre de los heroes de genero femenino
    '''
    for heroe in lista_heroes:
        valor_de_clave_genero = heroe.get("genero")
        if valor_de_clave_genero == "F":
            nombre = heroe.get("nombre")
            print(nombre)


'''
C - Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
'''
def determinar_heroe_alto_genero_m (lista_heroes: list) -> str:
    '''
    Iterar y determinar cual es el heroe más alto de genero masculino
    Recibe: Lista de diccionarios
    Devuelve: str, nombre del heroe más alto de genero masculino
    '''
    flag_altura = True
    for heroe in lista_heroes:
        valor_nombre = heroe.get("nombre")
        valor_genero = heroe.get("genero")
        valor_altura = heroe.get("altura")
        if valor_genero == "M":
            if flag_altura == True:
                altura_max = valor_altura
                nombre_max_altura = valor_nombre
                flag_altura = False
            else:
                if valor_altura > altura_max:
                    altura_max = valor_altura
                    nombre_max_altura = valor_nombre
    return nombre_max_altura

'''
D - Recorrer la lista y determinar cuál es el superhéroe más alto de género F
'''
def determinar_heroe_alto_genero_f (lista_heroes: list):
    '''
    Iterar y determinar cual es el heroe más alto de genero femenino
    Recibe: Lista de diccionarios
    Devuelve: str, nombre del heroe más alto de genero femenino
    '''
    flag_altura = True
    for heroe in lista_heroes:
        valor_nombre = heroe.get("nombre")
        valor_genero = heroe.get("genero")
        valor_altura = heroe.get("altura")
        if valor_genero == "F":
            if flag_altura == True:
                altura_max = valor_altura
                nombre_max_altura = valor_nombre
                flag_altura = False
            else:
                if valor_altura > altura_max:
                    altura_max = valor_altura
                    nombre_max_altura = valor_nombre
    return nombre_max_altura

'''
E - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M
'''
def determinar_heroe_bajo_genero_m (lista_heroes: list) -> str:
    '''
    Iterar y determinar cual es el heroe más bajo de genero masculino
    Recibe: Lista de diccionarios
    Devuelve: str, nombre del heroe más bajo de genero masculino
    '''
    flag_altura = True
    for heroe in lista_heroes:
        valor_nombre = heroe.get("nombre")
        valor_genero = heroe.get("genero")
        valor_altura = heroe.get("altura")
        if valor_genero == "M":
            if flag_altura == True:
                altura_min = valor_altura
                nombre_min_altura = valor_nombre
                flag_altura = False
            else:
                if valor_altura < altura_min:
                    altura_min = valor_altura
                    nombre_min_altura = valor_nombre
    return nombre_min_altura

'''
F - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F
'''
def determinar_heroe_bajo_genero_f (lista_heroes: list) -> str:
    '''
    Iterar y determinar cual es el heroe más bajo de genero femenino
    Recibe: Lista de diccionarios
    Devuelve: str, nombre del heroe más bajo de genero femenino
    '''
    flag_altura = True
    for heroe in lista_heroes:
        valor_nombre = heroe.get("nombre")
        valor_genero = heroe.get("genero")
        valor_altura = heroe.get("altura")
        if valor_genero == "F":
            if flag_altura == True:
                altura_min = valor_altura
                nombre_min_altura = valor_nombre
                flag_altura = False
            else:
                if valor_altura < altura_min:
                    altura_min = valor_altura
                    nombre_min_altura = valor_nombre
    return nombre_min_altura

'''
G - Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
'''
def determinar_promedio_genero_m (lista_heroes:list) -> float:
    '''
    Iterar los valores de altura de los heroes de genero masculino de la lista de diccionarios, sumarlos y calcular promedio
    Recibe: Lista de diccionarios
    Devuelve: float, el promedio de la altura de los heroes de genero masculino
    '''
    acumulador_altura_genero_m = 0
    for heroe in lista_heroes:
        valor_genero = heroe.get("genero")
        valor_altura = heroe.get("altura")
        if valor_genero == "M":
            acumulador_altura_genero_m += valor_altura
    promedio = acumulador_altura_genero_m / len(lista_heroes)
    return promedio

'''
H - Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
'''
def determinar_promedio_genero_f (lista_heroes:list) -> float:
    '''
    Iterar los valores de altura de los heroes de genero femenino de la lista de diccionarios, sumarlos y calcular promedio
    Recibe: Lista de diccionarios
    Devuelve: float, el promedio de la altura de los heroes de genero femenino
    '''
    acumulador_altura_genero_f = 0
    for heroe in lista_heroes:
        valor_genero = heroe.get("genero")
        valor_altura = heroe.get("altura")
        if valor_genero == "F":
            acumulador_altura_genero_f += valor_altura
    promedio = acumulador_altura_genero_f / len(lista_heroes)
    return promedio

'''
I - Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
'''
def informar_nombre_heroe_y_valor (lista_heroes: list) -> dict:
    '''
    Misma funciones que los puntos desde el C a F con la diferencia que el resultado es la clave y se le suma el valor correspondiente quedando a forma de diccionario
    Recibe: Lista de diccionarios
    Devuelve: dict, las claves son los resultados de los puntos anteriores junto con su altura correspondiente a forma de valo
    '''
    mi_diccionario = {}
    flag_altura_genero_m = True
    flag_altura_genero_f = True
    for heroe in lista_heroes:
        valor_nombre = heroe.get("nombre")
        valor_genero = heroe.get("genero")
        valor_altura = heroe.get("altura")
        match valor_genero:
            case "M":
                if flag_altura_genero_m == True:
                    altura_max_genero_m = valor_altura
                    nombre_max_altura_genero_m = valor_nombre
                    altura_min_genero_m = valor_altura
                    nombre_min_altura_genero_m = valor_nombre
                    flag_altura_genero_m = False
                else:
                    if valor_altura > altura_max_genero_m:
                        altura_max_genero_m = valor_altura
                        nombre_max_altura_genero_m = valor_nombre
                    else:
                        if valor_altura < altura_min_genero_m:
                            altura_min_genero_m = valor_altura
                            nombre_min_altura_genero_m = valor_nombre
            case "F":
                if flag_altura_genero_f == True:
                    altura_max_genero_f = valor_altura
                    nombre_max_altura_genero_f = valor_nombre
                    altura_min_genero_f = valor_altura
                    nombre_min_altura_genero_f = valor_nombre
                    flag_altura_genero_f = False
                else:
                    if valor_altura > altura_max_genero_f:
                        altura_max_genero_f = valor_altura
                        nombre_max_altura_genero_f = valor_nombre
                    else:
                        if valor_altura < altura_min_genero_f:
                            altura_min_genero_f = valor_altura
                            nombre_min_altura_genero_f = valor_nombre

    mi_diccionario[nombre_max_altura_genero_m] = altura_max_genero_m
    mi_diccionario[nombre_max_altura_genero_f] = altura_max_genero_f
    mi_diccionario[nombre_min_altura_genero_m] = altura_min_genero_m
    mi_diccionario[nombre_min_altura_genero_f] = altura_min_genero_f

    return mi_diccionario

'''
J - Determinar cuántos superhéroes tienen cada tipo de color de ojos.
'''
def informar_cantidad_heroes_color_ojos (lista_heroes: list) -> dict:
    '''
    Itarar los valores de la clave de color de ojos en la lista e ir sumando la cantidad de superheroes que tengan dicho color
    Recibe: Lista de diccionarios
    Devuele: dict[valor de la clave "color_ojos": int] Devuelve la cantidad de superheroes que tengan el color de ojos de la clave
    '''
    mi_diccionario = {}
    for heroe in lista_heroes:
        valor_color_ojos = heroe.get("color_ojos", "no especifica")
        if valor_color_ojos not in mi_diccionario:
            mi_diccionario[valor_color_ojos] = 1
        else:
            mi_diccionario[valor_color_ojos] += 1
    return mi_diccionario

'''
K - Determinar cuántos superhéroes tienen cada tipo de color de pelo.
'''
def informar_cantidad_heroes_color_pelo (lista_heroes: list) -> dict:
    '''
    Itarar los valores de la clave de color de pelo en la lista e ir sumando la cantidad de superheroes que tengan dicho color
    Recibe: Lista de diccionarios
    Devuele: dict[valor de la clave "color_pelo": int] Devuelve la cantidad de superheroes que tengan el color de ojos de la clave
    '''
    mi_diccionario = {}
    for heroe in lista_heroes:
        valor_color_pelo = heroe.get("color_pelo", "no especifica")
        if valor_color_pelo not in mi_diccionario:
            mi_diccionario[valor_color_pelo] = 1
        else:
            mi_diccionario[valor_color_pelo] += 1
    return mi_diccionario

'''
L - Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).
'''
def informar_cantidad_heroes_inteligencia (lista_heroes: list) -> dict:
    '''
    Iterar la lista de heroes, obtener el valor de inteligencia como clave, y asignar como valor a esas claves la cantidad de heroes en la que se repita como diccionario

    Recibe: Lista de diccionarios

    Devuelve: dict
    '''
    mi_diccionario = {}
    for heroe in lista_heroes:
        valor_inteligencia = heroe.get("inteligencia").capitalize()
        if valor_inteligencia == "":
            valor_inteligencia = "No tiene"
        if valor_inteligencia not in mi_diccionario:
            mi_diccionario[valor_inteligencia] = 1
        else:
            mi_diccionario[valor_inteligencia] += 1 
                    
    return mi_diccionario

'''
M - Listar todos los superhéroes agrupados por color de ojos.
'''
def imprimir_lista_heroes_por_color_ojos (lista_heroes: list) -> dict:
    '''
    Iterar la lista de heroes, obtener el valor de la clave color de ojos de la lista, establecerlo como clave de un nuevo diccionario y añadir los nombres de los heroes como valor a forma de las claves del nuevo diccionario ya establecido

    Recibe: Lista de diccionarios

    Devuelve: dict
    '''
    diccionario_heroes_por_color_ojos = {}
    for heroes in lista_heroes:
        valor_color_ojos = heroes.get("color_ojos").capitalize()
        valor_nombre = heroes.get("nombre")
        if valor_color_ojos not in diccionario_heroes_por_color_ojos.keys():
            diccionario_heroes_por_color_ojos[valor_color_ojos] = [valor_nombre]
        else:
            diccionario_heroes_por_color_ojos[valor_color_ojos].append(valor_nombre)
    return diccionario_heroes_por_color_ojos

'''
N - Listar todos los superhéroes agrupados por color de pelo.
'''
def imprimir_lista_heroes_por_color_pelo (lista_heroes: list) -> dict:
    '''
    Iterar la lista de heroes, obtener el valor de la clave color de pelo de la lista, establecerlo como clave de un nuevo diccionario y añadir los nombres de los heroes como valor a forma de las claves del nuevo diccionario ya establecido

    Recibe: Lista de diccionarios

    Devuelve: dict
    '''
    diccionario_heroes_por_color_pelo = {}
    for heroes in lista_heroes:
        valor_color_pelo = heroes.get("color_pelo").capitalize()
        valor_nombre = heroes.get("nombre")
        if valor_color_pelo not in diccionario_heroes_por_color_pelo.keys():
            diccionario_heroes_por_color_pelo[valor_color_pelo] = [valor_nombre]
        else:
            diccionario_heroes_por_color_pelo[valor_color_pelo].append(valor_nombre)
    return diccionario_heroes_por_color_pelo

'''
O - Listar todos los superhéroes agrupados por tipo de inteligencia
'''
def imprimir_lista_heroes_por_inteligencia (lista_heroes: list) -> dict:
    '''
    Iterar la lista de heroes, obtener el valor de la clave inteligencia de la lista, establecerlo como clave de un nuevo diccionario y añadir los nombres de los heroes como valor a forma de las claves del nuevo diccionario ya establecido

    Recibe: Lista de diccionarios

    Devuelve: dict'''
    diccionario_heroes_por_inteligencia = {}
    for heroes in lista_heroes:
        valor_inteligencia = heroes.get("inteligencia").capitalize()
        valor_nombre = heroes.get("nombre")
        if valor_inteligencia == "":
            valor_inteligencia = "No tiene"
        if valor_inteligencia not in diccionario_heroes_por_inteligencia.keys():
            diccionario_heroes_por_inteligencia[valor_inteligencia] = [valor_nombre]
        else:
            diccionario_heroes_por_inteligencia[valor_inteligencia].append(valor_nombre)
    return diccionario_heroes_por_inteligencia

#Punto M
def determinar_diccionarios_con_listas_vacias (lista_heroes: list) -> dict:
    diccionario_valor_color_ojos = {}
    for heroes in lista_heroes:
        valor_color_ojos = heroes.get("color_ojos")
        if valor_color_ojos not in diccionario_valor_color_ojos.keys():
            diccionario_valor_color_ojos[valor_color_ojos] = []
    return diccionario_valor_color_ojos
resultado = determinar_diccionarios_con_listas_vacias(lista_personajes)
print(resultado)

def sumar_nombre_heroes_en_dict_vacio (lista_heroes: list) -> dict:
    mi_diccionario = determinar_diccionarios_con_listas_vacias(lista_personajes)

    for heroes in lista_heroes:
        valor_nombre = heroes.get("nombre")
        valor_color_ojos = heroes.get("color_ojos")
        mi_diccionario[valor_color_ojos].append(valor_nombre)
    return mi_diccionario
print(sumar_nombre_heroes_en_dict_vacio(lista_personajes))


