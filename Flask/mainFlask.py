from flask import Flask
from flask import render_template
import gui

app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
    
    nombre = "Sergio"
    apellido = "Chávez"
    gui.print_preciosIda
    #y = gt.guiTest(2, 5)
    return render_template("index.html", name = nombre, apellido = apellido)
    
    #return "Tu nombre es "+nombre+" y tu apellio es "+apellido

"""
@app.route("/suma/<x>/<y>")
def sumaxy(x, y):
    return gt.guiTest(x, y)
"""
    
@app.route("/")
def get_name(nombre):
    return render_template("index.html", name = nombre)


@app.route("/estaciones")
def estaciones():
    estaciones = gui.for_estaciones()
    #return render_template("estaciones.html", estaciones = estaciones)
    return str(estaciones)

if __name__ == "__main__":
    app.run()

@app.route("/estacionesV")
def estaciones():
    estaciones = gui.for_estaciones()
    #return render_template("estaciones.html", estaciones = estaciones)
    return str(estaciones)

if __name__ == "__main__":
    app.run()

@app.route("/estacionesM")
def estaciones():
    estaciones = gui.for_estaciones()
    #return render_template("estaciones.html", estaciones = estaciones)
    return str(estaciones)

if __name__ == "__main__":
    app.run()
