#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import serial
import pynmea2
import utils
from threading import Thread
import time
import sys
import signal

# aprstnc = serial.Serial('/dev/ttyUSB0', 119200)

# Setup GPS Serial port
gps = serial.Serial('/dev/ttyAMA0')

rfd = serial.Serial('/dev/ttyUSB0', 57600, rtscts = 1)
rfd.write(b"hello!\r\n")

# Global Variables
exitApp = False
lat = 0
lon = 0
alt = 0
heading = 0
speed = 0

def sigint_handler(signum, frame):
    global exitApp

    print('\nClosing...\n')
    exitApp = True

signal.signal(signal.SIGINT, sigint_handler)

######################### GPS Data Thread #########################
def get_gps():
    global lat
    global lon
    global alt
    global heading
    global speed

    while (exitApp == False):
        try:
            data = gps.readline().decode('ascii')
            msg = pynmea2.parse(data)

            if isinstance(msg, pynmea2.types.talker.GGA):
                lat = round(msg.latitude, 5)
                lon = round(msg.longitude, 5)

                print("Latitude:", lat)
                print("Longitude:", lon)
                print("Numb Sats:", msg.num_sats)

                rfd.write(b"Latitude: " + bytes(str(lat), 'UTF-8') + b"\r\n")
                rfd.write(b"Longitue: " + bytes(str(lon), 'UTF-8') + b"\r\n")
                rfd.write(b"Numb sats: " + bytes(str(msg.num_sats), 'UTF-8') + b"\r\n")

                if(msg.altitude_units == 'M'):
                    alt = msg.altitude * (1/0.3048)

                print("Altitude:", str(round(alt, 2)), "ft")
                rfd.write(b"Altitude: " + bytes(str(round(alt,2)), 'UTF-8') + b"\r\n\n")

            if isinstance(msg, pynmea2.types.talker.VTG):
                # Magnetic north
                if msg.mag_track is None:
                    heading = 0
                else:
                    heading = msg.mag_track

                # Convert kmph to mph
                speed = round(msg.spd_over_grnd_kmph * 1.609344, 2)

                print("heading:", heading)
                print("speed:", speed, "\n")
        except:
            pass

    gps.close()

######################### APRS Thread #########################
def aprs():
    mypkt = utils.position_pkt()

    while (exitApp == False):
        mypkt.latitude  = lat
        mypkt.longitude = lon
        mypkt.icon      = "O"
        mypkt.heading   = heading
        mypkt.speed     = speed
        mypkt.altitude  = alt

        print("\n")
        print(str(mypkt))
        print(mypkt.serialize())
        print("\n")

        rfd.write(mypkt.serialize())
        rfd.write(b"\n")

        time.sleep(5)

######################### Start Threads #########################
gps_thread = Thread(target = get_gps)
gps_thread.start()

aprs_thread = Thread(target = aprs)
aprs_thread.start()
