#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Copyright 2014,2018 Mario Gomez <mario.gomez@teubi.co>
#
#    This file is part of MFRC522-Python
#    MFRC522-Python is a simple Python implementation for
#    the MFRC522 NFC Card Reader for the Raspberry Pi.
#
#    MFRC522-Python is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    MFRC522-Python is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with MFRC522-Python.  If not, see <http://www.gnu.org/licenses/>.
#

import RPi.GPIO as GPIO
import MFRC522TUI
import signal
import requests
import os
#import json

continue_reading = True
url_verificacion_estudiante = "http://10.6.49.201:5000/verificar"

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    #print("Campus:", estudime):
    global continue_reading
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

def verificar(uid):
    uid = "".join(list(map(str,uid)))
    print("join:", uid)
    return requests.get(url_verificacion_estudiante, {"uid":uid}).content


# Create an object of the class MFRC522
MIFAREReader = MFRC522TUI.MFRC522()

# This loop keeps checking for chips. If one is njson
while continue_reading:
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status != MIFAREReader.MI_OK:
        print("Tarjeta no detectada") 
        continue
    
    print("Tarjeta detectada!")

    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # UID valido
    if status != MIFAREReader.MI_OK:
        print("Identificador no válido") 
        continue

    print("UID:", uid)
    estudiante_info = verificar(uid)
    print(estudiante_info, "\n")
    print("Bienvenid@!\n")
    print("Nombre:", estudiante_info.nombre, estudiante_info.apellido1)
    #print("Campus:", estudiante_info.campus)
    print("Rol:", estudiante_info.rol)
    os.system.cls()