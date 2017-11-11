#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import floor

def degrees_to_ddm(dd):
    degrees = int(floor(dd))
    minutes = (dd - degrees) * 60
    return (degrees, minutes)

def latitude_to_ddm(dd):
    direction = "S" if dd < 0 else "N"
    degrees, minutes = degrees_to_ddm(abs(dd))

    return "{0:02d}{1:05.2f}{2}".format(
        degrees,
        minutes,
        direction,
        )

def longitude_to_ddm(dd):
    direction = "W" if dd < 0 else "E"
    degrees, minutes = degrees_to_ddm(abs(dd))

    return "{0:03d}{1:05.2f}{2}".format(
       degrees,
       minutes,
       direction,
       )

def comment_altitude(altitude):
    altitude = min(999999, altitude)
    altitude = max(-99999, altitude)
    return "/A={0:06.0f}".format(altitude)

class position_pkt(object):
    latitude  = 0
    longitude = 0
    icon      = ''
    heading   = 0
    speed     = 0
    altitude  = 0


    def __init__(self):
        self.data = []

    def __str__(self):
        return str(latitude_to_ddm(self.latitude)) + "/" + str(longitude_to_ddm(self.longitude)) + self.icon + str(self.heading) + "/" + str(self.speed) + comment_altitude(self.altitude)

    def serialize(self):
        return str.encode(str(latitude_to_ddm(self.latitude)) + "/" + str(longitude_to_ddm(self.longitude)) + self.icon + str(self.heading) + "/" + str(self.speed) + comment_altitude(self.altitude)) + b'\x0D'
