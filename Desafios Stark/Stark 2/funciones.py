from data_stark import lista_personajes
import os

def limpiar_consola ():
    '''
    Imprimir msj que al presionar tecla limpia la consola.
    Recibe: nada
    Devuelve: nada
    '''
    _ = input("presiona una letra para continuar")
    if os.name in ["ce", "nt", "dos"]:
        os.system("cls")
    else:
        os.system("clear")

#0
def stark_normalizar_datos (lista_heroes: list) -> str:
    if len(lista_heroes) == 0:
        mensaje = "Error: Lista de héroes vacía"
    else:
        cantidad_datos_modificados = 0
        for heroe in lista_heroes:
            valor_altura = heroe.get("altura")
            valor_peso = heroe.get("peso")
            valor_fuerza = heroe.get("fuerza")

            if valor_altura != float:
                float(valor_altura)
                heroe["altura"] = valor_altura
                cantidad_datos_modificados += 1
            
            if valor_peso != float:
                float(valor_peso)
                heroe["peso"] = valor_peso
                cantidad_datos_modificados += 1

            if valor_fuerza != int:
                int(valor_fuerza)
                heroe["fuerza"] = valor_fuerza
                cantidad_datos_modificados += 1

    if cantidad_datos_modificados > 0:
        mensaje = "Datos normalizados"
    return mensaje
print(stark_normalizar_datos(lista_personajes))

'''
B/1 - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
'''
#1.1
def obtener_nombre (heroe: dict) -> str: 
    '''
    Obtiene el valor de la clave nombre del heroe y le agrega un texto con el valor ya obtenido
    Recibe: dict
    Devuelve: str
    '''
    valor_nombre = heroe.get("nombre")
    nombre = f"Nombre: {valor_nombre}"
    return nombre

#1.2
def imprimir_dato (parametro_string: str):
    '''
    Tiene como función imprimir el str que se le asigne
    Recibe: str
    Devuelve: nada
    '''
    print(parametro_string)

#1.3
def stark_imprimir_nombres_heroes (lista_heroes: list[dict]):
    '''
    A partir de una lista de diccionarios, obtiene e imprime el valor de la clave nombre de la lista con texto agregado
    Recibe: Lista de dicionarios(esta lista contiene la información de los heroes a forma de diccionario)
    Devuelve: nada
    '''
    if len(lista_heroes) == 0:
        return -1
    else:
        for heroe in lista_heroes:
            nombre = obtener_nombre(heroe)
            imprimir_dato(nombre)



'''
C/2 - Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
'''
#2
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

#3
def stark_imprimir_nombres_alturas (lista_heroes: list[dict]):
    '''
    Imprimir los datos correspondientes haciendo uso de la función anterior desde una lista de diccionarios
    Recibe: Lista de dicionarios(esta lista contiene la información de los heroes a forma de diccionario)
    Devuelve: Nada
    '''
    for heroe in lista_heroes:
        resultado = obtener_nombre_y_dato(heroe, "altura")
        print(resultado)


'''
D/3 - Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
'''
#4.1
def calcular_max (lista_heroes: list[dict], key: str) -> dict:
    '''
    La función consta en analizar la lista de diccionarios brindada y a partir de esta hacer la selección del diccionario (elemento de la lista) que mayor valor de clave otorgada tenga.
    Recibe: Lista de dicionarios(esta lista contiene la información de los heroes a forma de diccionario)
    Devuelve: dict
    '''
    flag_max = True
    for heroe in lista_heroes:
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

#4.2
def calcular_min (lista_heroes: list[dict], key: str) -> dict:
    '''
    La función consta en analizar la lista de diccionarios brindada y a partir de esta hacer la selección del diccionario (elemento de la lista) que menor valor de clave otorgada tenga.
    Recibe: Lista de dicionarios(esta lista contiene la información de los heroes a forma de diccionario)
    Devuelve: dict
    '''
    flag_min = True
    for heroe in lista_heroes:
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


#4.3
def calcular_max_min_dato (lista_heroes: list[dict], calculo_a_realizar: str, valor_a_evaluar: str) -> dict:
    '''
    La función consta en devolver el diccionario de la lista con mayor o menor, según asignemos, valor de clave también asignada.
    Recibe: list[dict] esta lista contiene la información de los heroes a forma de diccionario; calculo a realizar(str) corresponde al tipo de calculo a realizar, este puede ser maximo o minimo; valor a evaluar (str) corresponde a la clave del diccionario, a través de esta se obtriene el valor de la misma
    Devuelve: dict
    '''
    if calculo_a_realizar == "maximo":
        resultado = calcular_max(lista_heroes, valor_a_evaluar)
    else:
        if calculo_a_realizar == "minimo":
            resultado = calcular_min(lista_heroes, valor_a_evaluar)
    return resultado

#4.4
def stark_calcular_imprimir_heroe (lista_heroes: list[dict], calculo_a_realizar: str, valor_a_evaluar: str):
    '''
    Consta en la impresón de los datos correspondientes del heroe a partir de la lista de los heroes asignados a modo de diccionario, el tipo de calculo a realizar y la el vlaor de la clave a evaluar.
    Recibe: list[dict] esta lista contiene la información de los heroes a forma de diccionario; calculo a realizar(str) corresponde al tipo de calculo a realizar, este puede ser maximo o minimo; valor a evaluar (str) corresponde a la clave del diccionario, a través de esta se obtriene el valor de la misma.
    Devuelve: nada
    '''
    dict_heroe = calcular_max_min_dato(lista_heroes, calculo_a_realizar, valor_a_evaluar)
    dato = obtener_nombre_y_dato(dict_heroe, valor_a_evaluar)
    if calculo_a_realizar == "maximo":
        imprimir_dato(f"Mayor {valor_a_evaluar}: {dato}")
    else:
        if calculo_a_realizar == "minimo":
            imprimir_dato(f"Menor {valor_a_evaluar}: {dato}")

'''
E/4 - Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
'''
#4.4
def stark_calcular_imprimir_heroe (lista_heroes: list[dict], calculo_a_realizar: str, valor_a_evaluar: str):
    '''
    Consta en la impresón de los datos correspondientes del heroe a partir de la lista de los heroes asignados a modo de diccionario, el tipo de calculo a realizar y la el vlaor de la clave a evaluar.
    Recibe: list[dict] esta lista contiene la información de los heroes a forma de diccionario; calculo a realizar(str) corresponde al tipo de calculo a realizar, este puede ser maximo o minimo; valor a evaluar (str) corresponde a la clave del diccionario, a través de esta se obtriene el valor de la misma.
    Devuelve: nada
    '''
    dict_heroe = calcular_max_min_dato(lista_heroes, calculo_a_realizar, valor_a_evaluar)
    dato = obtener_nombre_y_dato(dict_heroe, valor_a_evaluar)
    if calculo_a_realizar == "maximo":
        imprimir_dato(f"Mayor {valor_a_evaluar}: {dato}")
    else:
        if calculo_a_realizar == "minimo":
            imprimir_dato(f"Menor {valor_a_evaluar}: {dato}")

'''
F/5 - Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
'''
#5.1
def sumar_dato_heroe (lista_heroes: list, valor_a_evaluar:str) -> float:
    '''
    La función consta en verificar que la lista asignada contenga diccionarios, que no este vacia y sumar los valores de las claves asignadas a una variable.
    Recibe: list[dict] esta lista contiene la información de los heroes a forma de diccionario; el valor a evaluar es la clave que le vamos a asignar y a partir de esta obtener su valor.
    Devuelve: float la suma de los valores de la clave asignada
    '''
    acumulador = 0
    for heroe in lista_heroes:
        if isinstance(heroe, dict) and len(heroe) != 0:
            acumulador += heroe.get(valor_a_evaluar)
    return acumulador

#5.2
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

#5.3
def calcular_promedio (lista_heroes: list, valor_a_evaluar: str) -> float:
    '''
    La función consta en la division de la suma de los valores de las claves ya asignadas en funciones anteriores y dividirla por la cnatidad de elementos que tenga la lista para obtener el promedio.
    Recibe: list[dict] esta lista contiene la información de los heroes a forma de diccionario; el valor a evaluar(str) es la clave que le vamos a asignar y a partir de esta obtener su valor.
    Devuelve: float correposnde a el promedio
    '''
    suma_total_dato_heroes = sumar_dato_heroe(lista_heroes, valor_a_evaluar)
    promedio = dividir (suma_total_dato_heroes, (len(lista_heroes)))
    return promedio

#5.4
def stark_calcular_imprimir_promedio_altura (lista_heroes: list, valor_a_evaluar: str):
    '''
    La función consta en verificar que la lista asignada no este vacia, en caso lo este retornará 0, caso contrario llevara a cabo la impresión del promedio.
    Recibe: list[dict] esta lista contiene la información de los heroes a forma de diccionario; el valor a evaluar(str) es la clave que le vamos a asignar y a partir de esta obtener su valor.
    Devuelve: float corresponde solo si la lista se encuentra vacia. 
    '''
    if (sumar_dato_heroe(lista_heroes, valor_a_evaluar)) != 0:
        promedio = calcular_promedio(lista_heroes, valor_a_evaluar)
        imprimir_dato(f"El promedio de altura de los heroes es {promedio:.2f}")
    else:
        return -1

'''
G/6 - Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
'''
def obtener_nombre_y_dato_identidad (heroe: dict, key:str) -> str:
    '''
    Tiene como función la obtención de los valores de las claves identidad y otra que asignemos de un diccionario
    Recibe: dict, representa al heroe de una lista no asignada a esta función
    Devuelve: str
    '''
    valor_identidad = heroe.get("identidad")
    valor = heroe.get(key)
    mensaje = f"Identidad: {valor_identidad} | {key}: {valor}"
    return mensaje

def stark_calcular_imprimir_heroe_identidad (lista_heroes: list[dict], calculo_a_realizar: str, valor_a_evaluar: str) -> str:
    '''
    La función consta de la impresión de un mensaje a partir de una lista de diccionarios con información de heroes; tipo de calculo a realizar que puede ser minimo o maximo, valor a evaluar corresponde a el nombre de una clave, cuya cual queremos obtener su valor.
    Recibe: list[dict] esta lista contiene la información de los heroes a forma de diccionario; calculo a realizar(str) corresponde al tipo de calculo a realizar, este puede ser maximo o minimo; valor a evaluar (str) corresponde a la clave del diccionario, a través de esta se obtriene el valor de la misma.
    Devuelve: str corresponde a la impresión de los datos solicitados.
    '''
    dict_heroe = calcular_max_min_dato(lista_heroes, calculo_a_realizar, valor_a_evaluar)
    dato = obtener_nombre_y_dato_identidad(dict_heroe, valor_a_evaluar)
    if calculo_a_realizar == "maximo":
        imprimir_dato(f"Mayor {valor_a_evaluar}: {dato}")
    else:
        if calculo_a_realizar == "minimo":
            imprimir_dato(f"Menor {valor_a_evaluar}: {dato}")

def stark_calcular_imprimir_heroe_identidad (lista_heroes: list[dict], calculo_a_realizar: str, valor_a_evaluar: str) -> str:
    '''
    La función consta de la impresión de un mensaje a partir de una lista de diccionarios con información de heroes; tipo de calculo a realizar que puede ser minimo o maximo, valor a evaluar corresponde a el nombre de una clave, cuya cual queremos obtener su valor.
    Recibe: list[dict] esta lista contiene la información de los heroes a forma de diccionario; calculo a realizar(str) corresponde al tipo de calculo a realizar, este puede ser maximo o minimo; valor a evaluar (str) corresponde a la clave del diccionario, a través de esta se obtriene el valor de la misma.
    Devuelve: str corresponde a la impresión de los datos solicitados.
    '''
    dict_heroe = calcular_max_min_dato(lista_heroes, calculo_a_realizar, valor_a_evaluar)
    dato = obtener_nombre_y_dato_identidad(dict_heroe, valor_a_evaluar)
    if calculo_a_realizar == "maximo":
        imprimir_dato(f"Mayor {valor_a_evaluar}: {dato}")
    else:
        if calculo_a_realizar == "minimo":
            imprimir_dato(f"Menor {valor_a_evaluar}: {dato}")

'''
H/7 - Calcular e informar cual es el superhéroe más y menos pesado.
'''

#4.4
def stark_calcular_imprimir_heroe (lista_heroes: list[dict], calculo_a_realizar: str, valor_a_evaluar: str) -> str:
    '''
    La función consta de la impresión de un mensaje a partir de una lista de diccionarios con información de heroes; tipo de calculo a realizar que puede ser minimo o maximo, valor a evaluar corresponde a el nombre de una clave, cuya cual queremos obtener su valor.
    Recibe: list[dict] esta lista contiene la información de los heroes a forma de diccionario; calculo a realizar(str) corresponde al tipo de calculo a realizar, este puede ser maximo o minimo; valor a evaluar (str) corresponde a la clave del diccionario, a través de esta se obtriene el valor de la misma.
    Devuelve: str corresponde a la impresión de los datos solicitados.
    '''
    dict_heroe = calcular_max_min_dato(lista_heroes, calculo_a_realizar, valor_a_evaluar)
    dato = obtener_nombre_y_dato(dict_heroe, valor_a_evaluar)
    if calculo_a_realizar == "maximo":
        imprimir_dato(f"Mayor {valor_a_evaluar}: {dato}")
    else:
        if calculo_a_realizar == "minimo":
            imprimir_dato(f"Menor {valor_a_evaluar}: {dato}")


"""
J/8 - Construir un menú que permita elegir qué dato obtener
"""

#6.1
def imprimir_menu () -> str:
    '''
    La función consta en imprimir el menu de enunciados
    Recibe: Nada
    Devuelve: str, la impresión del texto
    '''
    menu = \
        """
        B/1 - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
        C/2 - Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
        D/3 - Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
        E/4 - Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
        F/5 - Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
        G/6 - Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
        H/7 - Calcular e informar cual es el superhéroe más y menos pesado.
        8 - Salir
        """
    imprimir_dato(menu)


#6.2
def validar_entero (numero: str):
    '''
    La función consta en verificar si el str ingresado contiene solo numeros o no
    Recibe: un número en str
    Devuelve: True o False
    '''
    if numero.isdigit():
        resultado = True
    else:
        resultado = False
    return resultado

#6.3
def stark_menu_principal () -> int:
    '''
    Muestra el menu principal , pide ingresar un número a forma de str, si este contiene solo digitos, retornara el mismo número transformado a int. Caso contrario, retornara -1.
    Recibe: Nada
    Devuelve: int, el número transformado.
    '''
    imprimir_menu()
    numero_ingresado = input("Ingresar un numero: ")
    verificar_digito = validar_entero(numero_ingresado)
    if verificar_digito == True:
        resultado = int(numero_ingresado)
    else:
        resultado = -1
    return resultado

#7
def stark_marvel_app (lista_heroes:list[dict]):
    '''
    Se encarga de la ejecución principal del programa.
    Recibe: list[dict] esta lista contiene la información de los heroes a forma de diccionario
    '''

    while True:

        opcion_elegida = stark_menu_principal()

        match opcion_elegida:
            case 1:
                stark_imprimir_nombres_heroes(lista_heroes)
            case 2:
                stark_imprimir_nombres_alturas(lista_personajes)
            case 3:
                stark_calcular_imprimir_heroe(lista_personajes, "maximo", "altura")
            case 4:
                stark_calcular_imprimir_heroe(lista_personajes, "minimo", "altura")
            case 5:
                stark_calcular_imprimir_promedio_altura(lista_personajes, "altura")
            case 6:
                stark_calcular_imprimir_heroe_identidad(lista_personajes, "maximo", "altura")
                stark_calcular_imprimir_heroe_identidad(lista_personajes, "minimo", "altura")
            case 7:
                stark_calcular_imprimir_heroe(lista_personajes, "maximo", "peso")
                stark_calcular_imprimir_heroe(lista_personajes, "minimo", "peso")
            case 8:
                break
            case _:
                print("opción incorrecta, elegir entre 1 y 9")
        limpiar_consola()