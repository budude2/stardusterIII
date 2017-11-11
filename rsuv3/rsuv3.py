#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import serial
import time

ser = serial.Serial('/dev/tty.usbserial-A904MJU4', 19200)

ser.write(b"FT146540")
time.sleep(0.1)
ser.write(b'\r')

time.sleep(0.1)
ser.write(b"F?")
time.sleep(0.1)
ser.write(b'\r')
time.sleep(0.1)

string = ser.read(26)
print(string.decode('UTF-8'))
time.sleep(0.1)

ser.write(b'CTN5WON')
time.sleep(0.1)
ser.write(b'\r')

ser.close()