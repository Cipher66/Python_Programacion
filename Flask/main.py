from flask import Flask
from flask import render_template

app = Flask(__name__)
app.debug = True

@app.route("/test")
def hello():
    
    nombre = "Sergio"
    apellido = "Chávez"
    return render_template("index.html", name = nombre)
    
    #return "Tu nombre es "+nombre+" y tu apellio es "+apellido
    
@app.route("/nombre/<nombre>")
def get_name(nombre):
    return render_template("index.html", name = nombre)


if __name__ == "__main__":
    app.run()