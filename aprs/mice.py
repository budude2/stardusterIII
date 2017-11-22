#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import utils
from math import floor

characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D",
              "E", "F", "G", "H", "I", "J", "K", "L",
              "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def encode_latitude(dd, mode):
    string = ""

    if(dd < 0):
        north = 1
    else:
        north = 0

    (degrees, minutes, minutes_hundreths) = utils.mice_long(dd)

    degrees_10 = floor(degrees / 10)
    degrees_1 = degrees - (degrees_10 * 10)

    minutes_10 = floor(minutes / 10)
    minutes_1 = minutes - (minutes_10 * 10)

    minutes_hundreths_10 = floor(minutes_hundreths / 10)
    minutes_hundreths_1 = minutes_hundreths - (minutes_hundreths_10 * 10)



    if(mode & 0x4):
        string += characters[degrees_10 + 22]
    else:
        string += characters[degrees_10]

    if(mode & 0x2):
        string += characters[degrees_1 + 22]
    else:
        string += characters[degrees_1]

    print(string)