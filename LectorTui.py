#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
--------------------------------
| Lectura TUI USM		       	|
| Camilo Nuñez Fernandez		|
| camilo.nunez@cnf.cl 			|
| camilo.nunezf@sansano.usm.cl 	|
| 29 de Enero del 2016			|
---------------------------------
-.Todos los derechos no son reservados, libre de modificación.
"""

import MFRC522TUI
import RPi.GPIO as GPIO
from itertools import cycle

banderaLectura = True


#Cortesía de www.github.com/rbonvall
def vericador(rut):
		reversed_digits = map(int, reversed(str(rut)))
		factors=cycle(range(2,8))
		s = sum(d * f for d, f in zip(reversed_digits,factors))
		return str((-s)%11)

def decodificado(lista):
	return "".join([hex(a)[2:].decode('hex') for a in lista]).strip()

MIFAREReader = MFRC522TUI.MFRC522()

while banderaLectura:
	(status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
	# Comprueba si es valida la tarjeta
	if status == MIFAREReader.MI_OK:
		(status,uid) = MIFAREReader.MFRC522_Anticoll()
		print "uid", uid
		size=MIFAREReader.MFRC522_SelectTag(uid)
		print "size:", size
		# Escoge solo las tarjetas Mifare 4k
		if size==56:
			if status == MIFAREReader.MI_OK:

				# Llave genérica para todos los bloques usados
				key = [0xA0,0xA1,0xA2,0xA3,0xA4,0xA5]

				#------------------------------- I - Lectura de Bloques -------------------------------#

				bloqueRut=79 # Bloque del rut
				status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, bloqueRut, key, uid)
				print "status", status
				if status == MIFAREReader.MI_OK:
					sector,datos= MIFAREReader.MFRC522_Read(bloqueRut)
					rutL= [hex(datos[x]) for x in range(5)]
					rut = ''.join([rutL[x][2:] for x in range(5)])
					rut = int(rut[:-1] + vericador(int(rut[:-1])))
				else:
					rut=0

				bloqueNom=72 # Bloque de los nombres
				status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, bloqueNom, key, uid)
				if status == MIFAREReader.MI_OK:
					sector,datos= MIFAREReader.MFRC522_Read(bloqueNom)
					nombres= decodificado(datos)
				else:
					nombres= "Error"

				bloqueApe1=73 # Bloque del primer apellido
				status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, bloqueApe1, key, uid)
				if status == MIFAREReader.MI_OK:
					sector,datos= MIFAREReader.MFRC522_Read(bloqueApe1)
					apellido1= decodificado(datos)
				else:
					apellido1= "Error"

				bloqueApe2=74 #Bloque de segundo apellido
				status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, bloqueApe2, key, uid)
				if status == MIFAREReader.MI_OK:
					sector,datos= MIFAREReader.MFRC522_Read(bloqueApe2)
					apellido2= decodificado(datos)
				else:
					apellido2= "Error"

				bloqueCargo=80 # Bloque del cargo del usuario
				status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, bloqueCargo, key, uid)
				if status == MIFAREReader.MI_OK:
					sector,datos= MIFAREReader.MFRC522_Read(bloqueCargo)
					cargo= decodificado(datos)
				else:
					cargo= "Error"

				bloqueCar1=81 # Bloque de carrera usuario
				status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, bloqueCar1, key, uid)
				if status == MIFAREReader.MI_OK:
					sector,datos= MIFAREReader.MFRC522_Read(bloqueCar1)
					car1= decodificado(datos)
				else:
					car1= "Error"

				bloqueCar2=82 # Bloque continuacion carrera
				status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, bloqueCar2, key, uid)
				if status == MIFAREReader.MI_OK:
					sector,datos= MIFAREReader.MFRC522_Read(bloqueCar2)
					car2= decodificado(datos)
				else:
					car2= "Error"

				#------------------------------- F - Lectura de Bloques -------------------------------#

				# Corte de lectura y limpiado de pines
				banderaLectura=False
				MIFAREReader.MFRC522_StopCrypto1()
				GPIO.cleanup()

print "NOMBRE: "+nombres+" "+apellido1+" "+apellido2
print "CARGO:"+" "+cargo
print "CARRERA: "+car1+car2
print "RUT:"+str(rut)
print "UID:",uid
