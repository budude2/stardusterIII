#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import max31865
import HSC
import HTU21D

pres = HSC.HSC(1)
hum = HTU21D.HTU21D(1)
temp = max31865.max31865(8,9,10,11)

print("Pressure (mb): " + str(pres.read_pressure()))
print("Humidity (rh): " + str(round(hum.read_humidity(), 2)))
print("Temp (c): " + str(round(hum.read_temperature(), 2)))
print("Thermo temp (c): " + str(round(temp.readTemp(), 2)))
