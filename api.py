import flask
from get_programmes import parseXML

app = flask.Flask(__name__)
app.config["DEBUG"] = True # Activo debug para mensajes en consola

@app.route('/home', methods=['GET']) # Ruta que brinda los programas para la pagina HOME
def home():
    channels = parseXML('outputs/home.xml')
    return channels

@app.route('/all', methods=['GET']) # Ruta que brinda los programas para la pagina HOME
def home():
    channels = parseXML('outputs/all.xml')
    return channels


app.run(host='0.0.0.0')
