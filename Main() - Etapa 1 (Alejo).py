from etapa2_final import*

def Aciertos(caracter, cadena, aciertos, repetido, puntos):
    """
    Retorna la cantidad de aciertos
    """
    if caracter in cadena and not repetido and caracter.isalpha():
        aciertos += 1
        puntos += 5
    return aciertos, puntos


def Acumulador(acumulador, caracter, cadena, repetido):
    """
    Retorna una lista con el caracter ingresado
    """
    if caracter not in cadena and caracter.isalpha() and not repetido:
        acumulador += caracter
    return acumulador


def Contador(aciertos, desaciertos, acumulador):
    """
    Devuelve una cadena con Aciertos: (funcion) Desaciertos: (funcion) (funcion)
    Usa Aciertos(), Desaciertos() y LetrasErradas()
    """
    return " Aciertos: " + str(aciertos) + " Desaciertos: " + str(desaciertos) + "-" + "-".join(acumulador)


def Desaciertos(cadena, desaciertos, caracter, repetido, puntos):
    """
    Recibe la cadena oculta y un caracter. Retorna la cantidad de veces en la que el usuario se equivoco
    tener en cuenta que al principio caracter esta vacio
    """
    if caracter not in cadena and not repetido:
        desaciertos += 1
        puntos -= 5
    return desaciertos, puntos


def EvaluaIngreso(caracter):
    """
    Evalua la longitud de la cadena ingresada
    """
    return len(caracter) == 1


def Ingreso():
    """
    Evalua el ingreso
    """
    caracter_correcto = False
    while not caracter_correcto:
        caracter = input("Ingrese un caracter: ")
        if EvaluaIngreso(caracter) and caracter.isalpha():
            caracter_correcto = True
        elif caracter.upper() == "FIN" or caracter == "0":
            caracter_correcto = True
        else:
            print("Dato invalido, ingrese UN caracter alfabetico")
    return caracter


def Mensaje(caracter, cadena, repetido, aciertos, desaciertos):
    """Retorna 3 tipos de mensajes, para el primer ingreso: "Palabra a adivinar: ", sino "Muy bien!!!:" o "Lo siento!!!"
    (Tener en cuenta que el primer caracter esta vacio)
    """
    if aciertos == 0 and desaciertos == 0:
        mensaje = "Ingrese letra "
    elif caracter.isalpha() and not repetido and caracter in cadena:
        mensaje = "Muy Bien "
    else:
        mensaje = "Lo siento "
    return mensaje


def MensajeFinal(cadena, cadenaoculta):
    """
    Retorna un mensaje final
    """
    return "FELICIDADES!!!" if cadena == "".join(cadenaoculta) else "BUENA SUERTE LA PROXIMA!!!"


def Repetido(caracter, acumulador, cadenaoculta):
    """
    Retorna un Booleano dependiendo si ya fue utilizado
    """
    return caracter in acumulador or caracter in cadenaoculta


def RecuperarCadena(repetido, cadenaoculta, cadena, caracter):
    """
    Desvela la cadena
    """
    if not repetido and caracter.isalpha():
        for i in range(len(cadena)):
            if caracter == cadena[i]:
                cadenaoculta[i] = caracter
    return cadenaoculta


def seguir_jugando():
    """
    Retorna un booleano si quiere seguir jugando
    """
    si = ["y","s","yes","si"]
    no = ["n","no"]
    decision = input("Quiere seguir jugando?: ").lower()
    while decision not in si and decision not in no:
        decision = input("Por favor elija una opcion valida [y/s]: ")
    return decision in si


def OcultarCadena(cadena):
    """
    Retorna la cadena oculta
    """
    cadenaoculta = ("? "*len(cadena)).split(" ")
    cadenaoculta.pop(-1)
    return cadenaoculta


def ValidarIngreso(caracter):
    """
    Retorna un Booleano en base a dos palabras claves
    """
    return caracter.upper() != "FIN" and caracter != "0"


def main():
    decision = True
    puntos = 0
    while decision:
        caracter = "-"
        acumulador = []
        desaciertos = 0
        aciertos = 0
        cadena = candidata()
        cadenaoculta = OcultarCadena(cadena)
        repetido = False
        while desaciertos <= 7 and ValidarIngreso(caracter) and "".join(cadenaoculta) != cadena:
            print(Mensaje(caracter, cadena, repetido, aciertos, desaciertos) + "--> " + "".join(cadenaoculta) + Contador(aciertos, desaciertos, acumulador) + " Puntos: " +str(puntos))
            caracter = Ingreso()
            repetido = Repetido(caracter, acumulador, cadenaoculta)
            cadenaoculta = RecuperarCadena(repetido, cadenaoculta, cadena, caracter)
            desaciertos, puntos = Desaciertos(cadena, desaciertos, caracter, repetido, puntos)
            aciertos, puntos = Aciertos(caracter, cadena, aciertos, repetido, puntos)
            acumulador = Acumulador(acumulador, caracter, cadena, repetido)
        print(MensajeFinal(cadena, cadenaoculta), "La palabra era: " + cadena)
        decision = seguir_jugando()


main()

"""
Errores: 
- Si colocas la palabra completa (en vez de una letra) y los caracteres de la palabra se encuentran en la cadena 
original (de la palahra a adivinar) te la toma como bien pero no revela las letras, se deberia desvelar la palabra 
completa si y solo si la palabra ingresada es = a la cadena original (se puede hacer una funcion mas tranquilamente 
para eso) pero primero se debe pulir aun mas el codigo. Tambien te da un acierto.
"""
