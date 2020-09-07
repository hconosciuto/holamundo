from datetime import datetime
from flask import Flask

ahora = datetime.now()
vfecha = ahora.strftime("%Y-%m-%d %H:%M")
app = Flask(__name__)

@app.route("/")
def hello_www():

    return "Hola Mundo, la fecha y hora son: " + vfecha