zonas = {
    "Zona1" : ["Urnieta","Donosti","Pasaia","Irun", "Errenteria", "Antxo"],
    "Zona2" : ["Bilbao", "Vitoria", "Azkoitia", "Azpeitia", "Hondarribia", "Pamplona"],
    "Zona3" : ["Gijón", "Vigo", "Orense", "León", "Burgos", "Oviedo"]
    }

precios = {
    "ida" : [1.70, 1.90, 2.00, 3.35, 3.80, 5.0],
    "ida/vuelta" : [2.00, 2.75, 4.10, 5.50, 6.40, 7.20],
    "mensual" : [10, 20, 30, 40, 50, 60]
    }

#Zonas en inglés

zones = {
    "Zone1" : ["Urnieta","Donosti","Pasaia","Irun", "Errenteria", "Antxo"],
    "Zone2" : ["Bilbao", "Vitoria", "Azkoitia", "Azpeitia", "Hondarribia", "Pamplona"],
    "Zone3" : ["Gijón", "Vigo", "Orense", "León", "Burgos", "Oviedo"]
    }

def print_poblaciones(zona):
    return zonas["zona"]
    
def estaciones():
    return["Bilbao","Orense"]

""" 
def print_poblacionesZona1():
        return zonas["Zona1"]

def print_poblacionesZona2():
        return zonas["Zona2"]

def print_poblacionesZona3():
        return zonas["Zona3"] 
""" 

def print_preciosIda():
        return precios["ida"]

def print_preciosVuelta():
        return precios["ida/vuelta"]
        
def print_preciosMensual():
        return precios["mensual"]

def destino_precios(opcion,zona,destino):
    zonaSel=zonas.get(zona)
    indPobZona=zonaSel.index(destino)
    preciosOpcion=precios.get(opcion)
    return "El viaje a "+destino+ " cuesta "+str(preciosOpcion[indPobZona])+" Euros"

def destino_preciosIngles(opcion,zona,destino):
    zonaSel=zonas.get(zona)
    indPobZona=zonaSel.index(destino)
    preciosOpcion=precios.get(opcion)
    return "The trip to "+destino+ " costs "+str(preciosOpcion[indPobZona])+" Euros"
    
def destino_preciosFrances(opcion,zona,destino):
    zonaSel=zonas.get(zona)
    indPobZona=zonaSel.index(destino)
    preciosOpcion=precios.get(opcion)
    return "Le voyage à"+destino+ " vaut "+str(preciosOpcion[indPobZona])+" Euros"

































""" 
def ejecutarMenu(destinos):
    #Comentario#
    opc = 0
    print("1. Ida")
    print("2. Ida y vuelta")
    print("3. Bono mensual") 


    

indPobZona=
 if destino == "Urnieta":
        Urnieta_precio = precios.get["ida"]
        print ("El viaje a "+destino+"cuesta "+Urnieta_precio)
    print("El viaje a "+destino+" cuesta "+str(preciosOpcion[indPobZona])+" Euros")
"""

    #print(zonas)
    #print(zonaSel)
    #print(indPobZona)
    #print(preciosOpcion)
    #kk3=preciosOpcion.get(opcion)
    #print(preciosOpcion[indPobZona])

    #for z in zonas.values():
        #print(zonas["Zona(Numero de zona))"])
        #print(str(z))

    #for p in precios.values():
        #print (precios["(Tipo de viaje))"])
        #print(str(p))