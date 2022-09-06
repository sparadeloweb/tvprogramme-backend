import flask
from get_programmes import parseXML

app = flask.Flask(__name__)
app.config["DEBUG"] = True # Activo debug para mensajes en consola

@app.route('/home', methods=['GET']) # Ruta que brinda los programas para la pagina HOME
def home():
    channels = parseXML('home.xml')
    return channels

app.run()