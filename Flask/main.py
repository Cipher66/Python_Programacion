from flask import Flask
from flask import render_template
import guiTest as gt

app = Flask(__name__)
app.debug = True

@app.route("/test")
def hello():
    
    nombre = "Sergio"
    apellido = "Chávez"
    #y = gt.guiTest(2, 5)
    return render_template("index.html", name = nombre, apellido = apellido)
    
    #return "Tu nombre es "+nombre+" y tu apellio es "+apellido

"""@app.route("/suma/<x>/<y>")
def sumaxy(x, y):
    return gt.guiTest(x, y)"""
    
@app.route("/nombre/<nombre>")
def get_name(nombre):
    return render_template("index.html", name = nombre)


if __name__ == "__main__":
    app.run()