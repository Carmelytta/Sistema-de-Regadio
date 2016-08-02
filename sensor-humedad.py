#!/usr/bin/python
# -*- coding: utf-8 -*-

#EJEMPLO DE BLINKING CON RASPBERRY PI
#Escrito por Gl4r3
import RPi.GPIO as GPIO 					#importamos la libreria y cambiamos su nombre por "GPIO"
import time 								#necesario para los delays

#establecemos el sistema de numeracion que queramos, en mi caso BCM
GPIO.setmode(GPIO.BCM)

#configuramos los pines GPIO
#GPIO.setup(17, GPIO.OUT)

muestra = GPIO.setup(4, INPUT)			#Entrada digital del sensor

bajo = GPIO.input(4, GPIO.LOW)
alto = GPIO.input(4, GPIO.HIGH)

#Comprobamos en que modo estamos

if muestra == alto:
	print "No hay humedad"
else: 
	print "Hay humedad"

###############################################

#Salida analogica

##############################################

#if muestra >= 1000:
#	print "Sensor desconectado"
#elif muestra < 1000 && muestra >= 600:
#	print "Suelo seco"
#elif muestra < 600 && muestra >= 370:
#	print "Suelo humedo"
#elif muestra < 370:
#	print "Sensor en agua"
#else:
#	print "Fuera de rango"