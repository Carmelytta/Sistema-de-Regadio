#!/usr/bin/python
# -*- coding: utf-8 -*-



#http://docs.gadgetkeeper.com/pages/viewpage.action?pageId=7700673


#Conexiones
#Vcc 3.3V
#GND tierra
#Pin salida al 4

import RPi.GPIO as GPIO 					#importamos la libreria y cambiamos su nombre por "GPIO"
import time 								#necesario para los delays

#establecemos el sistema de numeracion que queramos, en mi caso BCM
GPIO.setmode(GPIO.BCM)


