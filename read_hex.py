#!/usr/bin/env python
# -*- coding: utf8 -*-

import MFRC522TUI
import RPi.GPIO as GPIO
from itertools import cycle

MIFAREReader = MFRC522TUI.MFRC522()

flag = True

while flag:
	(status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
        # Comprueba si es valida la tarjeta
        if status == MIFAREReader.MI_OK:
		print MIFAREReader.MFRC522_Read(143)
		"""
		i = 0x50
		while i < 0x100:
			print i
			print MIFAREReader.MFRC522_Read(i)
			i += 0x01
		"""
