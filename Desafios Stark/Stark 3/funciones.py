from data_stark import lista_personajes
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


#funcion solicitada en el punto 1.2
def obtener_nombre (heroe: dict) -> str: 
    '''
    Obtiene el valor de la clave nombre del heroe y le agrega un texto con el valor ya obtenido
    Recibe: dict
    Devuelve: str
    '''
    valor_nombre = heroe.get("nombre")
    nombre = f"Nombre: {valor_nombre}"
    return nombre

#Función solicitada en el punto 2.4
def obtener_nombre_y_dato (heroe: dict, key:str) -> str:
    '''
    Tiene como función la obtención de los valores de las claves nombre y otra que asignemos de un diccionario
    Recibe: dict, este representa a la información del heroe
    Devuelve: str, información en relación a claves/valores del heroe
    '''
    valor_nombre = heroe.get("nombre")
    valor = heroe.get(key)
    mensaje = f"Nombre: {valor_nombre} | {key}: {valor}"
    return mensaje

#Función solicitada en el punto 3.3
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

# ##################################### Desafio 3 ################################

#0.0
def imprimir_menu_2 ():
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

#0.1
def stark_menu_principal_2 () -> int:
    '''
    Muestra el menu principal , pide ingresar un número a forma de str, si este contiene solo digitos, retornara el mismo número transformado a int. Caso contrario, retornara -1.
    Recibe: Nada
    Devuelve: int, el número transformado.
    '''
    imprimir_menu_2()
    numero_ingresado = input("Ingresar un numero: ")

    if numero_ingresado.isdigit():
        verificar_digito = True
    else:
        verificar_digito = False
    
    if verificar_digito == True:
        resultado = int(numero_ingresado)
    else:
        resultado = -1
    return resultado


#0.2
def stark_marvel_app (lista_heroes:list[dict]):
    '''
    Se encarga de la ejecución principal del programa.
    Recibe: list[dict] esta lista contiene la información de los heroes a forma de diccionario
    '''

    while True:

        opcion_elegida = stark_menu_principal_2()

        match opcion_elegida:
            case 1:
                stark_imprimir_heroe_genero(lista_personajes, "M")
            case 2:
                stark_imprimir_heroe_genero(lista_personajes, "F")
            case 3:
                stark_calcular_imprimir_heroe_genero(lista_personajes, "maximo", "altura", "M")
            case 4:
                stark_calcular_imprimir_heroe_genero(lista_personajes, "maximo", "altura", "F")
            case 5:
                stark_calcular_imprimir_heroe_genero(lista_personajes, "minimo", "altura", "M")
            case 6:
                stark_calcular_imprimir_heroe_genero(lista_personajes, "minimo", "altura", "F")
            case 7:
                stark_calcular_imprimir_promedio_altura_genero (lista_personajes, "altura", "M")
            case 8:
                stark_calcular_imprimir_promedio_altura_genero (lista_personajes, "altura", "F")
            case 10:
                stark_calcular_cantidad_por_tipo(lista_personajes, "color_ojos")
            case 11:
                stark_calcular_cantidad_por_tipo(lista_personajes, "color_pelo")
            case 12:
                stark_calcular_cantidad_por_tipo(lista_personajes, "inteligencia")
            case 13:
                stark_listar_heroes_por_dato(lista_personajes, "color_ojos")
            case 14:
                stark_listar_heroes_por_dato(lista_personajes, "color_pelo")
            case 15:
                stark_listar_heroes_por_dato(lista_personajes, "inteligencia")
            case _:
                print("opción incorrecta, elegir entre 1 y 15")
        limpiar_consola ()

##################################### Punto A Y B ##################################

#1.1
def es_genero (diccionario_heroe:dict, genero:str) -> bool:
    """
    La función se encarga de verificar que el valor de la clave obtenida coincida con el que le pasamos por parametro, y en caso que si, devolver True, caso contrario False
    Parametro: dict que representa al heroe, y st que representa el valor a validar
    Devuelve: bool
    """
    valor_genero = diccionario_heroe.get("genero")
    if valor_genero == genero:
        resultado = True
    else:
        resultado = False
    return resultado

#1.2
def stark_imprimir_heroe_genero (lista_heroes: list[dict], genero:str):
    """
    La función se encarga de iterar la lista de heroes, verificar si concide con el genero por parametro y en caso que si, obtener el nombre e imprimirlo
    Parametro: list[dict] lista de diccionarios de los heroes y str que representa el valor a validar
    """
    for heroe in lista_heroes:
        if es_genero(heroe, genero) == True:
            nombre = obtener_nombre(heroe)
            imprimir_dato(nombre)

##################################### Punto A Y B ##################################



##################################### Punto C, D, E y F ##################################
#2.1
def calcular_min_genero (lista_heroes: list[dict], clave_a_evaluar: str, genero: str) -> dict:
    """
    La función tiene como objetivo el héroe que cumpla la condición de tener el mínimo del género especificado
    Parametro: list[dict] que representa la lista de heroes, str que representa el dato a evaluar, str que representa el genero
    Devuelve: dict que representa el diccionario del heroe con el menor valor de la clave evaluada
    """
    lista_heroes_por_genero = []
    for heroe in lista_heroes:
        valor_genero = heroe.get("genero")
        if valor_genero == genero:
            lista_heroes_por_genero.append(heroe)

    flag_min = True
    for heroe in lista_heroes_por_genero:
        valor_a_evaluar = heroe.get(clave_a_evaluar)
        if flag_min == True:
            valor_min = valor_a_evaluar
            dict_heroe_min = heroe
            flag_min = False
        else:
            if valor_a_evaluar < valor_min:
                dict_heroe_min = heroe
    return dict_heroe_min

#2.2
def calcular_max_genero (lista_heroes: list[dict], clave_a_evaluar: str, genero: str) -> dict:
    """
    La función tiene como objetivo el héroe que cumpla la condición de tener el maximo del género especificado
    Parametro: list[dict] que representa la lista de heroes, str que representa el dato a evaluar, str que representa el genero
    Devuelve: dict que representa el diccionario del heroe con el mayor valor de la clave evaluada
    """
    lista_heroes_por_genero = []
    for heroe in lista_heroes:
        valor_genero = heroe.get("genero")
        if valor_genero == genero:
            lista_heroes_por_genero.append(heroe)

    flag_max = True
    for heroe in lista_heroes_por_genero:
        valor_a_evaluar = heroe.get(clave_a_evaluar)
        if flag_max == True:
            valor_min = valor_a_evaluar
            dict_heroe_max = heroe
            flag_max = False
        else:
            if valor_a_evaluar > valor_min:
                dict_heroe_max = heroe
    return dict_heroe_max

#2.3
def calcular_max_min_dato_genero (lista_heroes: list[dict], max_o_min: str, clave_a_evaluar: str, genero: str) -> dict:
    """
    La función deberá retornar el héroe que cumpla con la condición pedida actuando en función a si se solicita minimo o maximo
    Parametro: list[dict] que representa la lista de heroes, str que representa a como actuar si se escribe max o min, str que representa el dato a evaluar, str que representa el genero.
    Devuelve: dict el diccionario solicitado
    """
    if max_o_min == "maximo":
        resultado = calcular_max_genero(lista_heroes, clave_a_evaluar, genero)
    else:
        if max_o_min == "minimo":
            resultado = calcular_min_genero(lista_heroes, clave_a_evaluar, genero)
    return resultado

#2.4
def stark_calcular_imprimir_heroe_genero (lista_heroes: list[dict], max_o_min: str, clave_a_evaluar: str, genero: str):
    """
    La función imprimira el nombre y dato del héroe que cumpla con la condición pedida actuando en función a si se solicita minimo o maximo
    Parametro: list[dict] que representa la lista de heroes, str que representa a como actuar si se escribe max o min, str que representa el dato a evaluar, str que representa el genero.
    Devuelve: str
    """
    diccionario_heroe_correspondiente = calcular_max_min_dato_genero(lista_heroes, max_o_min, clave_a_evaluar, genero)
    resultado = obtener_nombre_y_dato(diccionario_heroe_correspondiente, clave_a_evaluar)
    imprimir_dato(resultado)

##################################### Punto C, D, E y F ##################################


##################################### Punto G y H ##################################
#3.1
def sumar_dato_heroe_genero (lista_heroes: list[dict], clave_a_evaluar: str, genero: str) -> float:
    """
    La función tiene como objetivo devolver el acumulador de valor de la clave solicitada
    Parametro: list[dict] que representa la lista de heroes, str que representa el dato a evaluar, str que representa el genero. 
    Devuelve: float que representa el acumulador de la clave solicitada
    """
    for heroe in lista_heroes:
        if len(heroe) == 0:
            imprimir_dato("Uno de los diccionarios se encuentra vacio o no pertenece a tipo diccionario")
            break

    acumulador_clave_correspondiente = 0
    lista_heroe_por_genero = []
    for heroe in lista_heroes:
        valor_genero = heroe.get("genero")
        if genero == valor_genero:
            lista_heroe_por_genero.append(heroe)
    
    for heroe in lista_heroe_por_genero:
        valor_clave = heroe.get(clave_a_evaluar)
        acumulador_clave_correspondiente += valor_clave
    
    return acumulador_clave_correspondiente


#3.2
def cantidad_heroes_genero (lista_heroes: list[dict], genero: str) -> int:
    """
    La función tiene como objetivo contabilizar los heroes según tipo de genero solicitado y retornar ese número.
    Parametro: list[dict] que representa la lista de heroes, str que representa el genero. 
    Devuelve: int que representa la cantidad de heroes según el genero solicitado
    """
    contador_heroes_por_genero = 0
    for heroe in lista_heroes:
        valor_genero = heroe.get("genero")
        if genero == valor_genero:
            contador_heroes_por_genero += 1
    return contador_heroes_por_genero


#3.3
def calcular_promedio_genero (lista_heroes: list[dict], clave_a_evaluar: str, genero: str) -> float:
    """
    La función tiene como objetivo devolver el promedio entre la cantidad de heroes de un genero con el acumulador de valor de ese mismo genero según la clave a evaluiar solicitada.
    Parametro: Parametro: list[dict] que representa la lista de heroes, str que representa el dato a evaluar, str que representa el genero. 
    Devuelve: float que representa el resultado del promedio entre la cantidad de heroes de un genero con el acumulador de valor de ese mismo genero según la clave a evaluiar solicitada
    """
    if len(lista_heroes) == 0:
        imprimir_dato( "Error: Lista de héroes vacía")
    else:
        promedio = dividir((sumar_dato_heroe_genero(lista_heroes, clave_a_evaluar, genero)), cantidad_heroes_genero(lista_heroes, genero))
    return promedio

#3.1
def stark_calcular_imprimir_promedio_altura_genero (lista_heroes: list[dict], clave_a_evaluar: str, genero: str):
    """
    La función consta en verificar que la lista no este vacia, una vez validado esto imprimir el promedio según los parametros ingresados
    Parametro: Parametro: list[dict] que representa la lista de heroes, str que representa el dato a evaluar, str que representa el genero.
    """
    if len(lista_heroes) == 0:
        imprimir_dato("Error: Lista de héroes vacía")
    else:
        imprimir_dato (calcular_promedio_genero(lista_heroes, clave_a_evaluar, genero))

##################################### Punto G y H ##################################


##################################### Punto J, K y L ##################################

#4.1
def calcular_cantidad_tipo (lista_heroes: list[dict], key:str) -> dict:
    """
    La función tiene como objetivo retornar un diccionario con los distintos valores del tipo de dato recibido por parámetro y la cantidad de cada uno.
    Recibe: list[dict] que representa la lista de heroes, str que representa la clave del diccionario.
    Devuelve: dict con los valore de las claves y com oresultado de estas, la cantidad de veces que se repite en la lista

    """
    diccionario_cantidad_claves = {}
    if len(lista_heroes) != 0:
        for heroe in lista_heroes:
            valor_clave = heroe.get(key)
            if valor_clave == "":
                valor_clave = "No tiene"
            if valor_clave not in diccionario_cantidad_claves.keys():
                diccionario_cantidad_claves[valor_clave] = 1
            else: 
                diccionario_cantidad_claves[valor_clave] += 1
        return diccionario_cantidad_claves

#4.2
def imprimir_cantidad_heroes_tipo (diccionario: dict, clave_del_nuevo_diccionario: str):
    """
    La función tiene como objetivo imprimir a forma de mensaje la clave evaluada, el vlaor de la misma y la cantidad de veces que se repite en la lista de los heroes 
    Recibe: list[dict] que representa la lista de heroes, str que representa la clave del diccionario
    """
    for clave, valor in diccionario.items():
        imprimir_dato(f"Característica: {clave_del_nuevo_diccionario} {clave} - Cantidad de héroes: {valor} ")

#4.3
def stark_calcular_cantidad_por_tipo (lista_heroes: list[dict], key: str):
    """
    La función tiene como objetivo imprimir el mensaje de la función anterior según los parametros ingresados.
    Recibe: list[dict] que representa la lista de heroes, str que representa la clave del diccionario
    """
    diccionario_corespondiente = calcular_cantidad_tipo(lista_heroes, key)
    imprimir_cantidad_heroes_tipo(diccionario_corespondiente, key)

##################################### Punto J, K y L ##################################


##################################### Punto M, N y O ##################################

#5.1
def obtener_lista_de_tipos (lista_heroes: list[dict], key: str) -> list:
    """
    La función tiene como objetivo iterar la lista de héroes guardando en una nueva lista las variedades del tipo de dato pasado por parámetro.
    Recibe: list[dict] que representa la lista de heroes, str que representa la clave del diccionario
    Devuelve: list que representa la lista de valores de las lista de heroes por parametro
    """
    lista_valores_de_clave_asignada = []
    for heroe in lista_heroes:
        valor_clave = heroe.get(key)
        if valor_clave not in lista_valores_de_clave_asignada:
            lista_valores_de_clave_asignada.append(valor_clave)
    return lista_valores_de_clave_asignada

#5.2
def normalizar_dato (valor_key: str, valor_por_defecto_vacio: str) -> str:
    """
    La función tiene como objetivo reemplazar el valor si el mismo se encuentra vacio por un segundo pasado por parametro.
    Recibe: str que representa el valor de la clave, str que representa el string por el cuakl reemplazariamos el primer parametro si este se encontrará vacio
    Devuelve: str 
    """
    if valor_key == "":
        valor_key = valor_por_defecto_vacio
        return valor_key
    else:
        return valor_key

#5.3
def obtener_heroes_por_tipo (lista_heroes: list[dict], lista_claves: list, key: str) -> dict:
    """
    La función tiene como objetivo devolver un diccionario con los valores de la clave solicitada y junto a esta slos nombres de los heroes correposndinetes. 
    Recibe: list[dict] lista de heroes, list lista de las claves, str clave a evaluar
    Devuelve: dict con los valores de las claves por parametro y jusnto a esta slos nombres correspondientes que conincidan con el valor
    """
    nuevo_diccionario = {}
    for clave in lista_claves:
        if clave not in nuevo_diccionario.keys():
            nuevo_diccionario[clave] = []
        for heroe in lista_heroes:
            valor_nombre = heroe.get("nombre")
            normalizar_dato(valor_nombre, "No tiene")
            if heroe[key] == clave:
                nuevo_diccionario[clave].append(valor_nombre)
    return nuevo_diccionario

#5.4 
def imprimir_heroes_por_tipo (diccionario: dict, key: str):
    """
    La función tiene como objetivo imprimir a forma de mensaje la clave junto con su valor y los nombres que coincidan con el valor
    Recibe: list[dict] lista de heroes, list lista de las claves, str clave a evaluar
    """
    for clave, valor in diccionario.items():
        separador = " | "
        mensaje = f"{key} {clave}: {separador.join(valor)}"
        imprimir_dato(mensaje)

#5.4
def stark_listar_heroes_por_dato (lista_heroes: list[dict], key: str):
    """
    La función tiene como objetivo imprimir el mensjae de la funcion anterior dependiendo de los parametros ingresados
    Recibe: list[dict] lista de heroes, list lista de las claves, str clave a evaluar
    """
    lista_tipos = obtener_lista_de_tipos(lista_heroes, key)
    diccionario_tipos = obtener_heroes_por_tipo(lista_heroes, lista_tipos, key)
    imprimir_heroes_por_tipo(diccionario_tipos, key)


##################################### Punto M, N y O ##################################
