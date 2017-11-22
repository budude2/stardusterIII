#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Utility functions pulled from aprs-python
## https://github.com/rossengeorgiev/aprs-python

from math import floor, ceil

def degrees_to_ddm(dd):
    degrees = int(floor(dd))
    minutes = (dd - degrees) * 60
    return (degrees, minutes)

def mice_long(dd):
    loc = degrees_to_ddm(abs(dd))
    degrees = loc[0]
    minutes = floor(loc[1])

    minutes_hundreths = floor(100*(loc[1] - minutes))

    return (degrees, minutes, minutes_hundreths)

def comment_altitude(altitude):
    altitude = min(999999, altitude)
    altitude = max(-99999, altitude)
    return "/A={0:06.0f}".format(altitude)