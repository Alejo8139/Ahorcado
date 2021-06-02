from texto import obtener_texto
from random import randrange

def minimo_5(texto):
    """
    evalua si contiene minimo 5 letras
    """
    min_5 = []
    for i in range(len(texto)):
        if len(texto[i]) >= 5:
            min_5 += [texto[i]]
    return min_5


def ordenado_alfa(texto):
    """
    ordena alfabeticamente un diccionario
    """
    return sorted(texto)


def cant_aparecidas(candidatas, texto):
    """
    Retorna la cantidad de veces que una palabra aparece en un texto
    """
    texto_final = {}
    for i in range(len(candidatas)):
        texto_final[candidatas[i]] = texto.count(candidatas[i])
    return texto_final


def maxima_longitud(texto):
    """
    Retorna la longitud maxima de una palabra a utilzar
    """
    acumulador = []
    for palabra in texto:
        acumulador.append(len(palabra))
    return max(acumulador)


def palabra_repetida(texto):
    """
    Retorna palabras que no se repiten
    """
    palabras = []
    for i in range(len(texto)):
        if texto[i] not in palabras:
            palabras += [texto[i]]
    return palabras


def separar(texto, palabra):
    """
    Auxiliar, convierte las cadenas es listas [Utilizada en desmembrar()]
    """
    return texto.split(palabra)


def desmembrar(texto):
    """
    Desmembra el texto devolviendo solamente palabras
    """
    caracteres_posibles = [",", ".", "?", "¿", "!", "¡", ";", ".", "_", "-", ":", "\n", "«", "»"]
    for i in range(len(caracteres_posibles)):
        texto = separar(texto, caracteres_posibles[i])
        texto = " ".join(texto)
    texto = texto.split()
    return texto


def quiero_palabra(maximo):
    """
    Pide el ingreso de una longitud deseada para su palabra
    """
    long_deseada = input("Ingrese la longitud deseada para su palabra (Mayor o igual a 5): ")
    while int(long_deseada) < 5 and long_deseada != "" or int(long_deseada) > maximo:
        long_deseada = int(input("Por favor, que sea entre 5 y {}: ".format(maximo)))
    return long_deseada


def selector_palabra(long_deseada, texto):
    """
    Selecciona la palabra deseada y arma una lista con ella
    """
    lista_deseada = []
    if int(long_deseada) >= 5:
        for palabra in texto:
            if len(palabra) == int(long_deseada):
                lista_deseada += [palabra]
    elif len(lista_deseada) == 0:
        list
    else:
        lista_deseada = texto
    return lista_deseada


def palabra_aleatoria(texto):
    """
    Retorna una palabra aleatoria
    """
    posicion = randrange(0, len(texto))
    palabra = texto[posicion]
    return palabra

def candidata():
    texto = obtener_texto()
    texto = desmembrar(texto)
    texto = minimo_5(texto)
    maximo = maxima_longitud(texto)
    long_deseada = quiero_palabra(maximo)
    texto = selector_palabra(long_deseada, texto)
    texto = ordenado_alfa(texto)
    candidatas = palabra_repetida(texto)
    palabra = palabra_aleatoria(texto)
    return palabra




