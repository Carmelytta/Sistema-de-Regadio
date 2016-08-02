#!/usr/bin/python

############################################################

# Llamada del programa sudo python sensores.py 11 4
# Programa en el que medimos humedad y temperatura con el sensores DHT/11

############################################################


# Librerias que importamos al programa
import sys
import Adafruit_DHT
import time
import RPi.GPIO as GPIO

import matplotlib.pyplot as plt
import numpy as np
plt.ion()

# Parametros por linea de comandos

sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
count = 0
s = []          #Lista de 20 posiciones para dibujar
s1 = []
GPIO.setmode(GPIO.BCM)   #Ponemos la Raspberry en modo BCM
GPIO.setup(17,GPIO.IN)    #Ponemos el pin 17 como ENTRADA
GPIO.setwarnings(False)


######################BUCLE DE SENSOR DE HUMEDAD############


#for i in range(0,20):          #Hacemos un bucle para rellenar una lista para poder dibujarlo
#       if GPIO.input(17) == GPIO.HIGH:
 #              print "Sensor seco"
#               s.insert(i,0)
                #s[i].append(0)                 #Guardamos un 0 cuando el sensor esta seco
#       else:
 #              print "Sensor humedo"
#               s.insert(i,1)
                #s[i].append(1)                 #Guardamos un 1 cuando el sensor esta humedo
#print s

# Comprobamos que el numero de parametros es el correcto

if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
else:
    print('Usa: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#')
    print('Ejemplo: sudo ./Adafruit_DHT.py 2302 4 - Lee desde AM2302 conectado al pin GPIO #4')
    sys.exit(1)

# Leemos el sensor con el metodo read_retry reintentamos 15 veces la lectura del sensor con dos segundos entre reintento

while count <= 5:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
#    count = count + 1
    if GPIO.input(17) == GPIO.HIGH:
        print "Sensor sequillo"
        s1.insert(count,0)
    else:
        print "Sensor humedillo"
        s1.insert(count,1)

    print s1
    count = count + 1

    print('Temperatura={0:0.1f}*  Humedad del aire={1:0.1f}%'.format(temperature, humidity))

#Dibujamos la grafica de la humedad

plt.plot(s1)
plt.title("Humedad del suelo")
plt.xlabel("Tiempo")
plt.ylabel("Humedad")

# Para expresar la temperatura en Fahrenheit.
# temperature = temperature * 9/5.0 + 32

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)



