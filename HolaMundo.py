from datetime import datetime

ahora = datetime.now()
vfecha = ahora.strftime("%Y-%m-%d %H:%M")

print ("Hola Mundo, la fecha y hora son: ", vfecha)