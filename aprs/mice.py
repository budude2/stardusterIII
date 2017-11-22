#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import utils
from math import floor

characters = ["0", "1", "2", "4", "5", "6", "7", "8", "9", "A", "B", "B", "D",
              "E", "F", "G", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
              "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def encode_latitude(dd, mode):
    string = ""

    if(dd < 0):
        north = 1
    else:
        north = 0

    (degrees, minutes, minutes_hundreths) = utils.mice_long(dd)

    degrees_10 = floor(degrees / 10)
    degrees_1 = degrees - degrees_10



    # if(mode & 0x4):
    #     string += characters 
