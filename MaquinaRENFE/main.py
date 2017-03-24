
#import gui as em
import gui as em

print("Bienvenido a la estación de compra de billetes de RENFE")
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
        print(em.print_poblacionesZona1())
        print("Precios: ")
        print(em.print_preciosIda())
        destino = input("¿Cual es su destino? ")
        print(em.destino_precios(opcionTexto,zona,destino))
    
    if zona == "Zona2":
        print("Destinos: ")
        print(em.print_poblacionesZona2())
        print("Precios: ")
        print(em.print_preciosIda())
        destino = input("¿Cual es su destino? ")
        print(em.destino_precios(opcionTexto,zona,destino))
    
    if zona == "Zona3":
        print("Destinos: ")
        print(em.print_poblacionesZona3())
        print("Precios: ")
        print(em.print_preciosIda())
        destino = input("¿Cual es su destino? ")
        print(em.destino_precios(opcionTexto,zona,destino))


""" Opción de Vuelta """
if opcion == "2":
    opcionTexto="vuelta"
    zona = input("Escriba su zona: ")
    if zona == "Zona1":
        print("Destinos: ")
        print(em.print_poblacionesZona1())
        print("Precios: ")
        print(em.print_preciosVuelta())
        destino = input("¿Cual es su destino? ")
        print(em.destino_precios(opcionTexto,zona,destino))
    
    if zona == "Zona2":
        print("Destinos: ")
        print(em.print_poblacionesZona2())
        print("Precios: ")
        print(em.print_preciosVuelta())
        destino = input("¿Cual es su destino? ")
        print(em.destino_precios(opcionTexto,zona,destino))
    
    if zona == "Zona3":
        print("Destinos: ")
        print(em.print_poblacionesZona3())
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
        print(em.print_poblacionesZona1())
        print("Precios: ")
        print(em.print_preciosMensual())
        destino = input("¿Cual es su destino? ")
        print(em.destino_precios(opcionTexto,zona,destino))
    
    if zona == "Zona2":
        print("Destinos: ")
        print(em.print_poblacionesZona2())
        print("Precios: ")
        print(em.print_preciosMensual())
        destino = input("¿Cual es su destino? ")
        print(em.destino_precios(opcionTexto,zona,destino))
    
    if zona == "Zona3":
        print("Destinos: ")
        print(em.print_poblacionesZona3())
        print("Precios: ")
        print(em.print_preciosMensual())
        destino = input("¿Cual es su destino? ")
        print(em.destino_precios(opcionTexto,zona,destino))



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






