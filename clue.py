from ast import Global
import random 
import os

personajes = ["Juan","Jose","Ximena","Raul","Claudia"]
habitaciones = ["salon de eventos", "baños", "sala de estar","terraza", "jardin"]
armas = ["Pistola", "Cuchillo", "Tuberia","Navaja","Motosierra"]

def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux
    else:
        _ = os.system('clear')

def intro():
    u"""Introduccion a la hisotira del clue"""
    introinfo = """
    En el recinto de eventos el 'Latinoamericano' se cometio el homicidio de uno de los participantes del evento:
    Rodrigo: un joven universitario de 20 años.
    Tu has sido seleccionado por tu gran hisotrial como detective como el encargado de realizar la investigacion en el lugar de los echos y atrapar al asesino
    Se han detenido temporalmnete a las 5 personas que se encontraban en el lugar (Juan, Jose, Ximena, Raul y Claudia)
    para poder preguntarles a cada uno en donde se encontraban en el momento del siniestro
    El recintro cuenta con las siguientes locaciones
        -Salon de eventos
        -Baños
        -Sala de estar
        -Terraza
        -Jardin
    Y se han reportado los siguientes elementos:
        -Pistola
        -Cuchillo
        -Tuberia
        -Navaja
        -Motosierra
    
    Tu trabajo como detective consiste en averiguar quien fue el responsable, en que lugar donde fue y con que arma
    Pierdes si no logras descubrir las tres variables del homicidio
    """
    print(introinfo)
    opc = input("Aceptas la mision? (Yes or No)")

    answer_player = False
    while not answer_player:
        if opc.upper() == "YES" or opc.upper() == "NO":
            answer_player = True
        else:
            clear()
            print(introinfo)
            opc = input("Aceptas la mision? (Yes or No)")

    if opc.upper() == "YES":
        print("Has aceptado la mision, hora de trabajar")
        return True
    else:
        print("Has declinado la mision, deshonra como detective")
        return False      

def menu(acciones):
    u"""Menu para seleccionar que hacer"""

    menuinfo = f"""
    Te quedan de realizar {acciones} acciones en total
    donde de las siguientes posibilidades podras recuperar informacion para la deduccion
    1) - Interrogar a un sospechoso 
    2) - Ver las camaras de vigilancia de una locacion
    3) - Hacer un cateo para encontrar un objeto
    """
    print(menuinfo)        
    wtd = input("Que deseas hacer? (1,2 o 3)")

    answer_player = False
    while not answer_player:
        if wtd in ["1","2","3"]:
            answer_player = True
        else:
            clear()
            print(menuinfo)
            wtd = input("Que deseas hacer? (1,2 o 3)")

    return wtd

def generaCrimen():
    global personajes,habitaciones,armas
    u"""Acomodar de forma aleatoria a las diferentes opciones, 
    y seleccionar la informacion del crimen"""

    crimen = []
    crimen.append(random.choice(personajes))
    crimen.append(random.choice(habitaciones))
    crimen.append(random.choice(armas))

    personajes = [personaje for personaje in set(personajes)]
    habitaciones = [habitacion for habitacion in set(habitaciones)]
    armas = [arma for arma in set(armas)]

    return crimen


def informacionPersoneje():
    u"""Preguntas informacion sobre un personaje"""
    personInfo = """
    De que personaje deseas saber informacion:
    1) Juan
    2) Jose
    3) Ximena
    4) Raul
    5) Claudia
    """
    print(personInfo)        
    wtd = input("Selecciona personaje (1,2,3,4 o 5)")

    answer_player = False
    while not answer_player:
        if wtd in ["1","2","3","4","5"]:
            answer_player = True
        else:
            clear()
            print(personInfo)
            wtd = input("Selecciona personaje (1,2,3,4 o 5)")

    things = ["Juan","Jose","Ximena","Raul","Claudia"]
    return things[int(wtd)-1]

def informacionLocacion():
    u"""Preguntas informacion sobre una locacion"""
    locacionInfo = """
    De que locacion deseas saber informacion:
    1) Salon de Eventos
    2) Baños
    3) Salon de estar
    4) Terraza
    5) Jardin
    """

    print(locacionInfo)        
    wtd = input("Selecciona locacion (1,2,3,4 o 5)")

    answer_player = False
    while not answer_player:
        if wtd in ["1","2","3","4","5"]:
            answer_player = True
        else:
            clear()
            print(locacionInfo)
            wtd = input("Selecciona locacion (1,2,3,4 o 5)")
    things = ["salon de eventos", "baños", "sala de estar","terraza", "jardin"]
    return things[int(wtd)-1]

def informacionArma():
    u"""Preguntas informacion sobre un arma"""
    armaInfo = """
    De que arma deseas saber informacion:
    1) Pistola
    2) Cuchillo
    3) Tuberia
    4) Navaja
    5) Motosierra
    """
    print(armaInfo)        
    wtd = input("Selecciona arma (1,2,3,4 o 5)")

    answer_player = False
    while not answer_player:
        if wtd in ["1","2","3","4","5"]:
            answer_player = True
        else:
            clear()
            print(armaInfo)
            wtd = input("Selecciona arma (1,2,3,4 o 5)")
    things = ["Pistola", "Cuchillo", "Tuberia","Navaja","Motosierra"]
    return things[int(wtd)-1]

def clue():
    u"""Implentacion de un juego tipo clue"""
    pass

def descubirInformacion(requestInf):
    global infocrimen

    allInfo = personajes + habitaciones + armas
    ind = allInfo.index(requestInf)


    if ind > 9:
        ind = ind - 10
    elif ind > 4:
        ind = ind - 5

    nextind = int()
    if ind == 4:
        nextind = 0
    else:
        nextind = ind + 1

    if personajes[ind-1] == infocrimen[0]:
        print(f"{personajes[ind]} dijo que estaba en {habitaciones[ind]} y que no vio llegar a nadie, para luego el trasladarse a {habitaciones[nextind]} y que vio el objeto {armas[ind]}")
    else:
        print(f"{personajes[ind]} dijo que estaba en {habitaciones[ind]} y que vio llegar a {personajes[ind-1]}, para luego el trasladarse a {habitaciones[nextind]} y que vio el objeto {armas[ind]}")
    
    if habitaciones[ind] == infocrimen[1]:
        
        print(f"Las camaras de {habitaciones[ind]} no se encuentran operativas")
    else:
        print(f"Las camaras se encuentran operativas en {habitaciones[ind]}")
        
    if armas[ind] == infocrimen[2]:
        print(f"Al hacer el cateo en {habitaciones[ind]} no se encontro en ninguna parte el objeto {armas[ind]}")
    else:
        print(f"Al hacer el cateo en {habitaciones[ind]} se encontro el siguiente objeto: {armas[ind]}")
    

def chooseCriminal():
    u"""Determina la informacion del homicida"""
    resultado = []
    Info1 = """
    Segun su investigacion quien fue el homicida?:
    1) Juan
    2) Jose
    3) Ximena
    4) Raul
    5) Claudia
    """
    print(Info1)        
    wtd = input("quien fue? (1,2,3,4 o 5)")

    answer_player = False
    while not answer_player:
        if wtd in ["1","2","3","4","5"]:
            answer_player = True
        else:
            clear()
            print(Info1)
            wtd = input("quien fue? (1,2,3,4 o 5)")
    
    p = ["Juan","Jose","Ximena","Raul","Claudia"]
    resultado.append(p[int(wtd)-1])

    Info2 =  """
    Segun su investigacion en que locacion fue?:
    1) Salon de Eventos
    2) Baños
    3) Salon de estar
    4) Terraza
    5) Jardin
    """
    print(Info2)        
    wtd = input("donde fue? (1,2,3,4 o 5)")

    answer_player = False
    while not answer_player:
        if wtd in ["1","2","3","4","5"]:
            answer_player = True
        else:
            clear()
            print(Info2)
            wtd = input("donde fue? (1,2,3,4 o 5)")
    
    p = ["salon de eventos", "baños", "sala de estar","terraza", "jardin"]
    resultado.append(p[int(wtd)-1])

    Info3 =  """
    Segun su investigacion con que arma fue?:
    1) Pistola
    2) Cuchillo
    3) Tuberia
    4) Navaja
    5) Motosierra
    """
    print(Info3)        
    wtd = input("donde fue? (1,2,3,4 o 5)")

    answer_player = False
    while not answer_player:
        if wtd in ["1","2","3","4","5"]:
            answer_player = True
        else:
            clear()
            print(Info3)
            wtd = input("donde fue? (1,2,3,4 o 5)")
    
    p = ["Pistola", "Cuchillo", "Tuberia","Navaja","Motosierra"]
    resultado.append(p[int(wtd)-1])

    return resultado

def main():
    global infocrimen
    infocrimen = generaCrimen()
    if intro():
        for i in range(5):
            op = menu(str(5-i))
            if op == "1":
                descubirInformacion(informacionPersoneje())
            elif op == "2":
                descubirInformacion(informacionLocacion())
            elif op == "3":
                descubirInformacion(informacionArma())
        res = chooseCriminal()
        if infocrimen == res:
            print("Felicidades lograste descubir quien fue el que hizo el homiciodio, el lugar y el arma")
        else:
            print("No lograste encontrar toda la informacion")
    else:
        pass
    

if __name__ == "__main__":
    main()