#!/usr/bin/python

############################################
#
#	   TFG : SISTEMA DE RIEGO 
#
############################################


# LIBRERIAS
import sys
import Adafruit_DHT
import time
import sqlite3
import RPi.GPIO as GPIO

# PARAMETROS EN LINEA DE COMANDOS
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
#definicion de la funcion
def humedadT(hum):
   conn = sqlite3.connect('/home/pi/bbdd/riego.db')
   cursor = conn.cursor()
   cursor.execute("INSERT INTO humedadT values(date('now'), time('now'), (?))", (hum,))
   conn.commit()
   conn.close()
# VARIABLES

s = []          #Lista de 20 posiciones para dibujar


#for row in cursor.execute("SELECT * FROM tempertatura"):
 #   print row
# MODO BCM DE LA RASPBERRY PI
GPIO.setmode(GPIO.BCM)   
# DEFINIMOS EL PIN 17 COMO ENTRADA
GPIO.setup(17,GPIO.IN)    
# Warnings
GPIO.setwarnings(False)


# PROGRAMA

# Comprobamos que el numero de parametros es el correcto

if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2] #Escogemos el pin 4 como entrada del sensor DHT
    #count = int(sys.argv[3]) #Bucle de captura del sensor
else:
    print('usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#')
    print('example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected ')
    sys.exit(1)



humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

#print('Temperatura={0:0.1f}*  Humedad del aire= {1:0.1f}%'.format(temperature, humidity))

humedadT(humidity)
if humidity is not None and temperature is not None:
    #while count > 0:
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
     #  count = count - 1
    
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)
