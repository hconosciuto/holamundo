from datetime import datetime
from flask import Flask

ahora = datetime.now()
vfecha = ahora.strftime("%Y-%m-%d %H:%M")
app = Flask(__name__)

@app.route("/")
def hello_www():

    return "Hola Mundo, la fecha y hora son: " + vfecha
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  # pragma: no cover

