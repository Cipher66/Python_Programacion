#import gui as em
import gui as em

print("Bienvenido a la estación de compra de billetes de RENFE")
print("Welcome to RENFE ticket buying station")
print("Bienvenue à la station d'achat de billets RENFE")
print("Ongi etorri RENFEko billete erosketako makinara")

idioma = input("Su idioma/Your language/Sa langue/Zure hizkuntza:")

"""Idioma Castellano"""
if idioma == "Español":
    print("Elija una opción:")
    print("1. Ida")
    print("2. Ida/Vuelta")
    print("3. Mensual")

    opcion = input("su opción: ")

    """ Opción de Ida """
    if opcion == "1":
        opcionTexto="ida"
        zona = input("Escriba su zona: ")
        if zona == "Zona1":
            print("Destinos: ")
            print(em.print_poblaciones(zona))
            print("Precios: ")
            print(em.print_preciosIda())
            destino = input("¿Cual es su destino? ")
            print(em.destino_precios(opcionTexto,zona,destino))
    
        if zona == "Zona2":
                print("Destinos: ")
                print(em.print_poblaciones(zona))
                print("Precios: ")
                print(em.print_preciosIda())
                destino = input("¿Cual es su destino? ")
                print(em.destino_precios(opcionTexto,zona,destino))
    
        if zona == "Zona3":
            print("Destinos: ")
            print(em.print_poblaciones(zona))
            print("Precios: ")
            print(em.print_preciosIda())
            destino = input("¿Cual es su destino? ")
            print(em.destino_precios(opcionTexto,zona,destino))


    """ Opción de Vuelta """
    if opcion == "2":
        opcionTexto="ida/vuelta"
        zona = input("Escriba su zona: ")
        if zona == "Zona1":
            print("Destinos: ")
            print(em.print_poblaciones(zona))
            print("Precios: ")
            print(em.print_preciosVuelta())
            destino = input("¿Cual es su destino? ")
            print(em.destino_precios(opcionTexto,zona,destino))
    
        if zona == "Zona2":
            print("Destinos: ")
            print(em.print_poblaciones(zona))
            print("Precios: ")
            print(em.print_preciosVuelta())
            destino = input("¿Cual es su destino? ")
            print(em.destino_precios(opcionTexto,zona,destino))
    
        if zona == "Zona3":
            print("Destinos: ")
            print(em.print_poblaciones(zona))
            print("Precios: ")
            print(em.print_preciosVuelta())
            destino = input("¿Cual es su destino? ")
            print(em.destino_precios(opcionTexto,zona,destino))

        
    """ Opción Mensual """
    if opcion == "3":
        opcionTexto="mensual"
        zona = input("Escriba su zona: ")
        if zona == "Zona1":
            print("Destinos: ")
            print(em.print_poblaciones(zona))
            print("Precios: ")
            print(em.print_preciosMensual())
            destino = input("¿Cual es su destino? ")
            print(em.destino_precios(opcionTexto,zona,destino))
    
        if zona == "Zona2":
            print("Destinos: ")
            print(em.print_poblaciones(zona))
            print("Precios: ")
            print(em.print_preciosMensual())
            destino = input("¿Cual es su destino? ")
            print(em.destino_precios(opcionTexto,zona,destino))
    
        if zona == "Zona3":
            print("Destinos: ")
            print(em.print_poblaciones(zona))
            print("Precios: ")
            print(em.print_preciosMensual())
            destino = input("¿Cual es su destino? ")
            print(em.destino_precios(opcionTexto,zona,destino))

"""Idioma Inglés"""
if idioma == "English":
    print("Select your option:")
    print("1. Departure")
    print("2. Trip ticket")
    print("3. Monthly")

    opcion = input("Your option: ")

    """ Departure option """
    if opcion == "1":
        opcionTexto="ida"
        zona = input("Select your zone: ")
        if zona == "Zone1": 
            print("Destinations: ")
            print(em.print_poblacionesZona1())
            print(em.print_preciosIda())
            destino = input("What's your destination? ")
            print(em.destino_preciosIngles(opcionTexto,zona,destino))

        if zona == "Zone2":
            print("Destinations: ")
            print(em.print_poblacionesZona2())
            print(em.print_preciosIda())
            destino = input("What's your destination? ")
            print(em.destino_preciosIngles(opcionTexto,zona,destino))

        if zona == "Zone3":
            print("Destinations: ")
            print(em.print_poblacionesZona3())
            print(em.print_preciosIda())
            destino = input("What's your destination? ")
            print(em.destino_preciosIngles(opcionTexto,zona,destino))  

    """ Trip ticket option """
    if opcion == "2":
        opcionTexto = "ida/vuelta"
        zona = input("Select your zone: ")
        if zona == "Zone1": 
            print("Destinations: ")
            print(em.print_poblacionesZona1())
            print(em.print_preciosVuelta())
            destino = input("What's your destination? ")
            print(em.destino_preciosIngles(opcionTexto,zona,destino))
        
        if zona == "Zone2": 
            print("Destinations: ")
            print(em.print_poblacionesZona2())
            print(em.print_preciosVuelta())
            destino = input("What's your destination? ")
            print(em.destino_preciosIngles(opcionTexto,zona,destino))
        
        if zona == "Zone3": 
            print("Destinations: ")
            print(em.print_poblacionesZona3())
            print(em.print_preciosVuelta())
            destino = input("What's your destination? ")
            print(em.destino_preciosIngles(opcionTexto,zona,destino))

    """ Monthly option """
    if opcion == "3":
        opcionTexto = "mensual"
        zona = input("Select your zone: ")
        if zona == "Zone1":
            print("Destinations: ")
            print(em.print_poblacionesZona1())
            print(em.print_preciosMensual())
            destino = input("What's your destination? ")
            print(em.destino_preciosIngles(opcionTexto,zona,destino))

        if zona == "Zone2":
            print("Destinations: ")
            print(em.print_poblacionesZona2())
            print(em.print_preciosMensual())
            destino = input("What's your destination? ")
            print(em.destino_preciosIngles(opcionTexto,zona,destino))

        if zona == "Zone3":
            print("Destinations: ")
            print(em.print_poblacionesZona3())
            print(em.print_preciosMensual())
            destino = input("What's your destination? ")
            print(em.destino_preciosIngles(opcionTexto,zona,destino))

""""Idioma Francés"""
if idioma == "Français":
    print("Choisissez: ")
    print("1. Aller ")
    print("2. Aller-retour ")
    print("3. Mensuel ")

    opcion = input("votre choix: ")

    """Opcion de ida"""
    if opcion == "1":
        opcionTexto="aller"
        zona = input("Entrez votre région: ")
        if zona == "Zone1":
            print("Destinations: ")
            print(em.print_poblacionesZona1())
            print("Prix: ")
            print(em.print_preciosIda())
            destino = input("Quelle est votre destination?")
            print(em.destino_preciosFrances(opcionTexto,zona,destino))

        if zona == "Zone2":
            print("Destinations: ")
            print(em.print_poblacionesZona2())
            print("Prix: ")
            print(em.print_preciosIda())
            destino = input("Quelle est votre destination?")
            print(em.destino_preciosFrances(opcionTexto,zona,destino))

        if zona == "Zone3":
            print("Destinations: ")
            print(em.print_poblacionesZona3())
            print("Prix: ")
            print(em.print_preciosIda())
            destino = input("Quelle est votre destination?")
            print(em.destino_preciosFrances(opcionTexto,zona,destino))


    """Opcion de vuelta"""
    if opcion == "2":
        opcionTexto="aller-retour"
        zona = input("Entrez votre région: ")
        if zona == "Zone1":
            print("Destinations: ")
            print(em.print_poblacionesZona1())
            print("Prix: ")
            print(em.print_preciosVuelta())
            destino = input("Quelle est votre destination?")
            print(em.destino_preciosFrances(opcionTexto,zona,destino))

        if zona == "Zone2":
            print("Destinations: ")
            print(em.print_poblacionesZona2())
            print("Prix: ")
            print(em.print_preciosVuelta())
            destino = input("Quelle est votre destination?")
            print(em.destino_preciosFrances(opcionTexto,zona,destino))

        if zona == "Zone3":
            print("Destinations: ")
            print(em.print_poblacionesZona3())
            print("Prix: ")
            print(em.print_preciosVuelta())
            destino = input("Quelle est votre destination?")
            print(em.destino_preciosFrances(opcionTexto,zona,destino))

    """Opcion mensual"""
    if opcion == "3":
        opcionTexto="mensuel"
        zona = input("Entrez votre région: ")
        if zona == "Zone1":
            print("Destinations: ")
            print(em.print_poblacionesZona1())
            print("Prix: ")
            print(em.print_preciosMensual())
            destino = input("Quelle est votre destination?")
            print(em.destino_preciosFrances(opcionTexto,zona,destino))

        if zona == "Zone2":
            print("Destinations: ")
            print(em.print_poblacionesZona2())
            print("Prix: ")
            print(em.print_preciosMensual())
            destino = input("Quelle est votre destination?")
            print(em.destino_preciosFrances(opcionTexto,zona,destino))
        
        if zona == "Zone3":
            print("Destinations: ")
            print(em.print_poblacionesZona3())
            print("Prix: ")
            print(em.print_preciosMensual())
            destino = input("Quelle est votre destination?")
            print(em.destino_preciosFrances(opcionTexto,zona,destino))

"""
def print_zonas():
    for z, v in zonas.items():
        print(z)
        print(v['destinos'])

def mi_zona(destino):
    for z, v in zonas.items():
        if destino in v["destinos"]:
            return z
    return "No zona"
# print_zonas()

"""
