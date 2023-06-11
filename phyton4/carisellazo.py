from random import randint, random
apuesta=0 
saldo=4000
moneda = randint(1, 2)
def lanzarMoneda():

    nombre = input("Ingrese su nombre: ")
    print(f"¡Bienvenido al super  juego {nombre}")
    moneda = randint(1, 2)
    return moneda

jugador = lanzarMoneda()



def jugar():
    moneda=lanzarMoneda()
    eleccion = int(input("digite 1 para escoger cara y 2 para escoger sello"))

    if moneda == 1 and eleccion == 1:
        print("salio cara, usted escogio cara ganaste!...")
    elif moneda == 1 and eleccion == 2:
        print("salio cara, usted escogio sello perdiste!...")
    elif moneda == 2 and eleccion == 2:
        print("salio sello, usted escogio sello ganaste!...")
    elif moneda == 2 and eleccion == 1:
        print("salio sello, usted escogiocara perdiste!..")
    elif eleccion != 1 or eleccion != 2:
        print("digitaste una opcion incorrecta")
    else:
        print("datos incorrectos")
    print(f"la moneda cayo {moneda}")

    return ganar
def ganar ():
    apuesta=ganar()


