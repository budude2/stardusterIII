#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import serial
from aprslib.packets import PositionReport
import utils

#ser = serial.Serial('/dev/ttyUSB0', 119200)

mypkt = utils.position_pkt()

mypkt.latitude  = 33.103172
mypkt.longitude = -96.670547
mypkt.icon      = "O"
mypkt.heading   = 271
mypkt.speed     = 12
mypkt.altitude  = 600

print(str(mypkt))
print(mypkt.serialize())
