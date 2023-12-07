import json
import re
import os
"""
Nicolas Sanchez
42155002
1H
"""

def limpiar_consola ():
    '''
    Imprimir msj que al presionar tecla limpia la consola.
    Recibe: nada
    Devuelve: nada
    '''
    _ = input("Presiona una letra para continuar")
    if os.name in ["ce", "nt", "dos"]:
        os.system("cls")
    else:
        os.system("clear")


####################################### Funciones extraidas del desafio 2 #############################

#funcion solicitada en el punto 0.0
def imprimir_dato (parametro_string: str):
    '''
    Tiene como función imprimir el str que se le asigne
    Recibe: str
    Devuelve: nada
    '''
    print(parametro_string)

#función solicitada en el punto 5.2
def dividir (dividendo: float, divisor: int) -> float:
    '''
    La función consta en verificar que el divisor asignado no sea 0 y una vez cumplido esto, hacer la división de los 2 números asigandos como parametro. 
    Recibe: float corresponde al dividendo; int corresponde a la cantidad de elementos que tiene una lista.
    Devuelve: float, corresponde a la división de lso 2 números asigandos.
    '''
    if divisor == 0:
        resultado = 0
    else:
        resultado = dividendo / divisor
    return resultado
####################################### Funciones extraidas del desafio 2 #############################

###################################### INCIO PRIMERA PARTE ################################

#1.1
def imprimir_menu_desafio_5 ():
    '''
    La función consta en imprimir el menu de enunciados
    Recibe: Nada
    Devuelve: Nada
    '''
    menu = \
        """
        A/1 - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
        B/2 - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
        C/3 - Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
        D/4 - Recorrer la lista y determinar cuál es el superhéroe más alto de género F
        E/5 - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M
        F/6 - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F
        G/7 - Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
        H/8 - Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
        I/9 - Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
        J/10 - Determinar cuántos superhéroes tienen cada tipo de color de ojos.
        K/11 - Determinar cuántos superhéroes tienen cada tipo de color de pelo. 
        L/12 - Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).
        M/13 - Listar todos los superhéroes agrupados por color de ojos.
        N/14 - Listar todos los superhéroes agrupados por color de pelo.
        O/15 - Listar todos los superhéroes agrupados por tipo de inteligencia        
        """
    imprimir_dato(menu)

#1.2
def stark_menu_principal_desafio_5():
    """
    La función se encarga de la impresión del menu de enunciados y solicitar que se ingrese una letra que coincida con el patron de regex
    Recibe: Nada
    Devuelve: str la letra que se pasa por parametro o int -1 en caso no coincida
    """
    imprimir_menu_desafio_5 ()
    letra_ingresada = input("Ingresar una letra:   ")
    patronregex = "([a-zA-Z])"
    if re.match(patronregex, letra_ingresada):
        return letra_ingresada
    else:
        return -1

#1.3
def stark_marvel_app_5(lista_heroes: list[dict]):
    """
    Se encarga de la ejecución principal de nuestro programa
    Recibe: list[dict] una lista de heroes
    Devuelve: Nada
    """
    while True:

        opcion_elegida = stark_menu_principal_desafio_5()

        match opcion_elegida:
            case "a":
                stark_guardar_heroe_genero(lista_heroes, "M")
            case "b":
                stark_guardar_heroe_genero(lista_heroes, "F")
            case "c":
                stark_calcular_imprimir_guardar_heroe_genero(lista_heroes, "maximo", "altura", "M")
            case "d":
                stark_calcular_imprimir_guardar_heroe_genero(lista_heroes, "maximo", "altura", "F")
            case "e":
                stark_calcular_imprimir_guardar_heroe_genero(lista_heroes, "minimo", "altura", "M")
            case "f":
                stark_calcular_imprimir_guardar_heroe_genero(lista_heroes, "minimo", "altura", "F")
            case "g":
                stark_calcular_imprimir_guardar_promedio_altura_genero (lista_heroes, "altura", "M")
            case "h":
                stark_calcular_imprimir_guardar_promedio_altura_genero (lista_heroes, "altura", "F")
            case "i":
                pass
            case "j":
                stark_calcular_cantidad_por_tipo(lista_heroes, "color_ojos")
            case "k":
                stark_calcular_cantidad_por_tipo(lista_heroes, "color_pelo")
            case "l":
                stark_calcular_cantidad_por_tipo(lista_heroes, "inteligencia")
            case "m":
                stark_listar_heroes_por_dato(lista_heroes, "color_ojos")
            case "n":
                stark_listar_heroes_por_dato(lista_heroes, "color_pelo")
            case "o":
                stark_listar_heroes_por_dato(lista_heroes, "inteligencia")
            case _:
                print("opción incorrecta, elegir una letra entre 'a' y 'o'")
        limpiar_consola ()



#1.4
def leer_archivo(nombre_archivo: str) -> list[dict]:
    """
    La función se encarga de la lectura del archivo que pasemos por parametro y extraer el valor de la clave "lista_personajes"
    Recibe: str que correponde al nombre del archivo
    Devuelve: list[dict]
    """
    with open(nombre_archivo, "r") as archivo_json:
        heroes_diccionario = json.load(archivo_json)
        lista_diccionario = heroes_diccionario.get("lista_personajes")
        return lista_diccionario


#1.5
def guardar_archivo(nombre_archivo: str, contenido_a_guardar) -> bool:
    """
    La función se encarga de guardar nueva información en un archivo y/o crear uno a partir del contenido que le pasemos
    Recibe: str que corresponde al nombre del archivo, y como segundo parametro el contenido que se quiera guardar dentro de este
    Devuelve: bool True si se pudo guardar y caso contrario, False
    """
    try:
        with open(nombre_archivo, "w") as archivo:
            archivo.write(contenido_a_guardar)
            print(f"Se creo el archivo: {nombre_archivo}")
            return True
    except Exception:
        print(f"Error al crear el archivo: {nombre_archivo}")
        return False
    

#1.6
def capitalizar_palabras(palabra: str) -> str:
    """
    Se encarga de capitalizar todas las palabras que se pasen por parametro
    Recibe: str el contenido que se quiera capitalizar
    Devuelve: str el mismo contenido que se paso por parametro capitalizado
    """
    palabra_o_palabras_capitalizadas = palabra.title()
    return palabra_o_palabras_capitalizadas

#1.7
def obtener_nombre_capitalizado(heroe: dict) -> str:
    """
    Se encarga de capitalizar el valor de la clave nombre del diccionario que se pasa por parametro
    Recibe: dict
    Devuelve: str
    """
    nombre_heroe = heroe.get("nombre")
    nombre_heroe_capitalizado = capitalizar_palabras(nombre_heroe)
    return f"Nombre: {nombre_heroe_capitalizado}"

#1.8
def obtener_nombre_y_dato(heroe: dict, key: str) -> str:
    """
    Se encarga de obtener los valor de nombre y la key que le pasemos por parametro de un diccionario (que también pasamos por parametro) y lo transforma en un texto
    Recibe: dict que corresponde a un heroe, str key que sería el dato a evaluar
    Devuelve: str un texto
    """
    nombre = obtener_nombre_capitalizado(heroe)
    dato = heroe.get(key)
    key_capitalizada = capitalizar_palabras(key)
    return f"{nombre} | {key_capitalizada}: {dato}"

###################################### FINALIZACIÓN PRIMERA PARTE ################################

###################################### INCIO SEGUNDA PARTE ################################

#2.1
def es_genero(heroe: dict, genero: str):
    """
    Obtiene el valor de genero del diccionario que se pasa por parametro y si coincide con el 2do parametro, devuelve True, caso contrario False.
    Recibe: dict que representa los datos de un heroe, y str que representa el genero
    Devuelve: bool
    """
    genero_heroe = heroe.get("genero")
    if genero_heroe == genero:
        return True
    else:
        return False

#2.2
def stark_guardar_heroe_genero(lista_heroes: list[dict], genero: str) -> bool:
    """
    La función se encarga de imprimir solamente los héroes o heroínas que coincidan con el género pasado por parámetro y además, guardar todos los datos de los héroes en un archivo con extensión csv
    Recibe: list[dict] de heroes
    Devuelve: bool
    """
    heroes_genero = []
    for heroe in lista_heroes:
        coincidencia_genero = es_genero(heroe, genero)
        if coincidencia_genero == True:
            nombre_heroe = obtener_nombre_capitalizado(heroe)
            imprimir_dato(nombre_heroe)
            heroes_genero.append(nombre_heroe)
    texto = ", ".join(heroes_genero)
    try:
        guardar_archivo(f"heroes_{genero}.csv", texto)
    except Exception:
        return False
    else:
        return True
###################################### FINALIZACIÓN SEGUNDA PARTE ################################

###################################### INCIO TERCERA PARTE ################################

#3.1
def calcular_min_genero(lista_heroes: list[dict], key: str, genero: str):
    """
    La función tiene como objetivo el héroe que cumpla la condición de tener el mínimo del género especificado
    Parametro: list[dict] que representa la lista de heroes, str que representa el dato a evaluar, str que representa el genero
    Devuelve: dict que representa el diccionario del heroe con el menor valor de la clave evaluada
    """
    lista_heroes_por_genero = []
    flag_min = True
    for heroe in lista_heroes:
        if heroe.get("genero") == genero:
            lista_heroes_por_genero.append(heroe)
    for heroe in lista_heroes_por_genero:
        valor_a_evaluar = heroe.get(key)
        if flag_min == True:
            valor_min = valor_a_evaluar
            dict_heroe_min = heroe
            flag_min = False
        else:
            if valor_a_evaluar < valor_min:
                valor_min = valor_a_evaluar
                dict_heroe_min = heroe
    return dict_heroe_min 

#3.2
def calcular_max_genero(lista_heroes: list[dict], key: str, genero: str):
    """
    La función tiene como objetivo el héroe que cumpla la condición de tener el maximo del género especificado
    Parametro: list[dict] que representa la lista de heroes, str que representa el dato a evaluar, str que representa el genero
    Devuelve: dict que representa el diccionario del heroe con el mayor valor de la clave evaluada
    """
    lista_heroes_por_genero = []
    flag_max = True
    for heroe in lista_heroes:
        if heroe.get("genero") == genero:
            lista_heroes_por_genero.append(heroe)
    for heroe in lista_heroes_por_genero:
        valor_a_evaluar = heroe.get(key)
        if flag_max == True:
            valor_maximo = valor_a_evaluar
            dict_heroe_max = heroe
            flag_max = False
        else:
            if valor_a_evaluar > valor_maximo:
                valor_maximo = valor_a_evaluar
                dict_heroe_max = heroe
    return dict_heroe_max

#3.3
def calcular_max_min_dato_genero(lista_heroes: list[dict], calculo_a_realizar: str, valor_a_evaluar: str, genero: str) -> dict:
    '''
    La función consta en devolver el diccionario de la lista con mayor o menor, según asignemos, valor de clave también asignada.
    Recibe: list[dict] esta lista contiene la información de los heroes a forma de diccionario; calculo a realizar(str) corresponde al tipo de calculo a realizar, este puede ser maximo o minimo; valor a evaluar (str) corresponde a la clave del diccionario, a través de esta se obtriene el valor de la misma
    Devuelve: dict
    '''
    if calculo_a_realizar == "maximo":
        resultado = calcular_max_genero(lista_heroes, valor_a_evaluar, genero)
    else:
        if calculo_a_realizar == "minimo":
            resultado = calcular_min_genero(lista_heroes, valor_a_evaluar, genero)
    return resultado

#3.4
def stark_calcular_imprimir_guardar_heroe_genero(lista_heroes: list[dict], calculo_a_realizar: str, valor_a_evaluar: str, genero: str):
    """
    La función deberá retornar el héroe que cumpla con la condición pedida actuando en función a si se solicita minimo o maximo
    Parametro: list[dict] que representa la lista de heroes, str que representa a como actuar si se escribe max o min, str que representa el dato a evaluar, str que representa el genero.
    Devuelve: dict el diccionario solicitado
    """
    dict_heroe = calcular_max_min_dato_genero(lista_heroes, calculo_a_realizar, valor_a_evaluar, genero)
    dato = obtener_nombre_y_dato(dict_heroe, valor_a_evaluar)
    if calculo_a_realizar == "maximo":
        mensaje = f"Mayor {valor_a_evaluar}: {dato}"
        imprimir_dato(mensaje)
    else:
        if calculo_a_realizar == "minimo":
            mensaje = f"Menor {valor_a_evaluar}: {dato}"
            imprimir_dato(mensaje)
    valor_a_evaluar = valor_a_evaluar.lower()
    try:
        guardar_archivo(f"heroes_{calculo_a_realizar}_{valor_a_evaluar}_{genero}.csv", mensaje)
    except Exception:
        return False
    else:
        return True

###################################### FINALIZACIÓN TERCERA PARTE ################################

###################################### INCIO CUARTA PARTE ################################

#4.1
def sumar_dato_heroe_genero (lista_heroes: list[dict], valor_a_evaluar: str, genero: str) -> float:
    """
    La función tiene como objetivo devolver el acumulador de valor de la clave solicitada
    Parametro: list[dict] que representa la lista de heroes, str que representa el dato a evaluar, str que representa el genero. 
    Devuelve: float que representa el acumulador de la clave solicitada
    """
    acumulador = 0
    for heroe in lista_heroes:
        if isinstance(heroe, dict) and len(heroe) != 0 and heroe.get("genero") == genero:
            acumulador += heroe.get(valor_a_evaluar)
    return acumulador

#4.2
def cantidad_heroes_genero(lista_heroes: list[dict], genero: str):
    """
    La función tiene como objetivo contabilizar los heroes según tipo de genero solicitado y retornar ese número.
    Parametro: list[dict] que representa la lista de heroes, str que representa el genero. 
    Devuelve: int que representa la cantidad de heroes según el genero solicitado
    """
    lista_heroes_filtrada = list(filter(lambda heroe: heroe.get("genero") == genero, lista_heroes))
    contador_heroes_por_genero = len(lista_heroes_filtrada)
    return contador_heroes_por_genero


#4.3
def calcular_promedio_genero (lista_heroes: list, valor_a_evaluar: str, genero: str) -> float:
    """
    La función tiene como objetivo devolver el promedio entre la cantidad de heroes de un genero con el acumulador de valor de ese mismo genero según la clave a evaluiar solicitada.
    Parametro: Parametro: list[dict] que representa la lista de heroes, str que representa el dato a evaluar, str que representa el genero. 
    Devuelve: float que representa el resultado del promedio entre la cantidad de heroes de un genero con el acumulador de valor de ese mismo genero según la clave a evaluiar solicitada
    """
    suma_total_dato_heroes = sumar_dato_heroe_genero(lista_heroes, valor_a_evaluar, genero)
    cantidad_de_heroes_por_genero = cantidad_heroes_genero(lista_heroes, genero)
    promedio = dividir (suma_total_dato_heroes, cantidad_de_heroes_por_genero)
    return promedio

#4.4
def stark_calcular_imprimir_guardar_promedio_altura_genero (lista_heroes: list, valor_a_evaluar: str, genero: str) -> bool:
    """
    La función consta en verificar que la lista no este vacia, una vez validado esto imprimir el promedio según los parametros ingresados y guardar los datos en un archivo
    Recibe: list[dict] que representa la lista de heroes, str que representa el dato a evaluar, str que representa el genero.
    Devuelve: bool será True si se guardo correctamente, y caso contrario False
    """
    if len(lista_heroes) != 0:
        promedio = calcular_promedio_genero(lista_heroes, valor_a_evaluar, genero)
        dato_a_imprimir = f"{valor_a_evaluar.capitalize()} promedio género {genero}: {promedio:.2f}"
        imprimir_dato(dato_a_imprimir)
        try:
            guardar_archivo(f"heroes_promedio_{valor_a_evaluar}_{genero}.csv", dato_a_imprimir)
        except Exception:
            return False
        else:
            return True
    else:
        imprimir_dato("Error: Lista de héroes vacía")

###################################### FINALIZACIÓN CUARTA PARTE ################################


###################################### INCIO QUINTA PARTE ################################

#5.1
def calcular_cantidad_tipo(lista_heroes: list[dict], key: str) -> dict:
    """
    La función tiene como objetivo retornar un diccionario con los distintos valores del tipo de dato recibido por parámetro y la cantidad de cada uno.
    Recibe: list[dict] que representa la lista de heroes, str que representa la clave del diccionario.
    Devuelve: dict con los valores de las claves y com oresultado de estas, la cantidad de veces que se repite en la lista
    """
    if len(lista_heroes) != 0:
        diccionario_keys = {}
        for heroe in lista_heroes:
            nombre_clave = heroe.get(key)
            if nombre_clave == "":
                nombre_clave = "No tiene"
            if nombre_clave not in diccionario_keys.keys():
                diccionario_keys[nombre_clave] = 1
            else:
                diccionario_keys[nombre_clave] += 1            
    else: 
        mensaje = {"Error": "La lista se encuentra vacia"}
        return mensaje
    return diccionario_keys


#5.2
def guardar_cantidad_heroes_tipo (diccionario_por_genero: dict, key: str) -> bool:
    """
    Esta función tiene como objetivo iterar cada key del diccionario y variabilizar dicha key con su valor para luego formatearlos en un mensaje y guardarlo en un archivo
    Recibe: list[dict] que representa la lista de heroes, str que representa la clave del diccionario
    Devuelve: bool será True si se guardo correctamente, y caso contrario False
    """
    lista_heroes_por_genero = []
    for clave, valor in diccionario_por_genero.items():
        mensaje = f"Caracteristica: {key} {clave} - Cantidad de heroes: {valor}"
        lista_heroes_por_genero.append(mensaje)
    try:
        guardar_archivo(f"heroes_cantidad_{key}.csv", ", ".join(lista_heroes_por_genero))
    except Exception:
        return False
    else: 
        return True


#5.3
def stark_calcular_cantidad_por_tipo (lista_heroes: list[dict], key: str):
    """
    La función se encarga de calcular la cantidad de heroes a partir de la key que se pasa como parametro y guardarlo en un archivo
    Recibe: list[dict] lista de heroes, key que representa la clave
    Devuelve: bool será True si se guardo correctamente, y caso contrario False
    """
    diccionario = calcular_cantidad_tipo(lista_heroes, key)
    try:
        guardar_cantidad_heroes_tipo(diccionario, key)
    except Exception:
        return False
    else:
        return True

###################################### FINALIZACIÓN QUINTA PARTE ################################


###################################### INCIO SEXTA PARTE ################################

#6.1
def obtener_lista_de_tipos (lista_heroes: list[dict], key: str) -> set:
    """
    Esta función deberá iterar la lista de héroes guardando en un set las variedades del tipo de dato pasado por parámetro.
    Recibe: list[dict] lista de heroes, str como key a evaluar
    Devuelve: set con los valores de la key que se pasa por parametro
    """
    set_tipos = set()
    for heroe in lista_heroes:
        valor_key = heroe.get(key, "N/A")
        valor_key = capitalizar_palabras(valor_key)
        set_tipos.add(valor_key)
    return set_tipos

#6.2
def normalizar_dato (valor_de_clave, valor_por_defecto_a_colocar_si_esta_vacio):
        """
        Si el valor que se pasa como primer parametro viene vacio, se le asigna un valor por defecto como segund parametro.
        Recibe: 1er valor, 2do valor si el primero esta vacio.
        Devuelve: El primer valor o valor por defecto
        """
        if valor_de_clave == "":
            valor_de_clave = valor_por_defecto_a_colocar_si_esta_vacio
            return valor_de_clave
        else:
            return valor_de_clave

#6.3
def normalizar_heroe (diccionario_heroe: dict, key:str) -> dict:
    """
    Se encarga de normalizar los valores de la key del diccionario que pasamos por parametro y capitalizar el valor de la clave nombre.
    Recibe: dict que representa un heroe. key que representa la clave a evaluar
    Devuelve: El diccionario del heroe que se paso por parametro con los datos modificados.
    """
    valor_de_la_clave = diccionario_heroe.get(key)
    valor_nombre = diccionario_heroe.get("nombre")
    diccionario_heroe[key] = normalizar_dato(valor_de_la_clave, "N/A")
    diccionario_heroe["nombre"] = capitalizar_palabras(valor_nombre)
    return diccionario_heroe

#6.4
def obtener_heroes_por_tipo (lista_heroes: list[dict], set_tipos: set, key: str) -> dict:
    """
    La función se encarga de a partir de los elementos de un set, agregarle los nombres de los heroes que coincidan el valor de la key que se pasa por parametro en forma de lista.
    Recibe: Recibe: list[dict] lista de heroes, set tipos, key que representa la clave
    Devuelve: dic del nombre del set con la lista de nombres de los heroes en los que coincida el set con el valor de la key que se pasa por parametro
    """
    diccionario_set_variedades = {}
    for i in set_tipos:
        if i not in diccionario_set_variedades.keys():
            diccionario_set_variedades[i] = []
        for heroe in lista_heroes:
            dato_normalizado = normalizar_dato(heroe[key], "N/A")
            if dato_normalizado.capitalize() == i.capitalize():
                diccionario_set_variedades[i].append(heroe["nombre"])
    return diccionario_set_variedades


#6.5 
def guardar_heroes_por_tipo (diccionario: dict, key: str) -> bool:
    """
    La función tiene como objetivo imprimir y guardar un determinado mensaje a partir del diccionario y key qie se pase por parametro
    Recibe: dict que representa a un heroe, key que representa el valor a evaluar
    Devuelve: bool será True si se guardo correctamente, y caso contrario False 
    """
    contenido = ""
    for clave, valor in diccionario.items():
        signo = " | "
        mensaje_a_imprimir = f"{clave} {key}: {signo.join(valor)}"
        imprimir_dato(mensaje_a_imprimir)
        contenido += mensaje_a_imprimir
    try:
        guardar_archivo(f"heroes_segun_{clave}.csv", contenido)
    except Exception:
        return False
    else:
        return True


#6.6
def stark_listar_heroes_por_dato (lista_heroes: list[dict], key: str) -> bool:
    """
    La función se encarga de guardar el contenido de los nombres junto con el valor de la key de los heroes que se pasa por parametro
    Recibe: list que es la lista de heroes, y key que representa el valor a evaluar
    Devuelve: bool será True si se guardo correctamente, y caso contrario False 
    """
    set_de_tipos = obtener_lista_de_tipos(lista_heroes, key)
    diccionario_de_variedades = obtener_heroes_por_tipo(lista_heroes, set_de_tipos, key)
    try:
        guardar_heroes_por_tipo(diccionario_de_variedades, key)
    except Exception:
        return False
    else: 
        return True
    
###################################### FINALIZACIÓN SEXTA PARTE ################################
