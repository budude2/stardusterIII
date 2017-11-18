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
gps = serial.Serial()
gps.baudrate = 9600
gps.port = '/dev/tty.usbserial-A5058GNQ'

# Global Variables
exitApp = False
lat = 0
lon = 0
alt = 0

def sigint_handler(signum, frame):
    global exitApp

    print('\nClosing...\n')
    exitApp = True

signal.signal(signal.SIGINT, sigint_handler)

try:
    gps.open()
except serial.SerialException:
    print("Could not open serial port.")
    print("Is it configured correctly?")
    sys.exit(0)

def get_gps():
    global lat
    global lon
    global alt

    while (exitApp == False):
        data = gps.readline().decode('ascii')
        try:
            msg = pynmea2.parse(data)

            if isinstance(msg, pynmea2.types.talker.GGA):
                lat = msg.latitude
                lon = msg.longitude

                print("Latitude:", lat)
                print("Longitude:", lon)
                print("Numb Sats:", msg.num_sats)

                if(msg.altitude_units == 'M'):
                    alt = msg.altitude * (1/0.3048)

                print("Altitude:", str(round(alt, 2)), "ft\n")
        except:
            pass

    gps.close()

def aprs():
    mypkt = utils.position_pkt()

    while (exitApp == False):
        print('loop')
        print(exitApp)
        mypkt.latitude  = lat
        mypkt.longitude = lon
        mypkt.icon      = "O"
        mypkt.heading   = 271
        mypkt.speed     = 12
        mypkt.altitude  = alt

        print(str(mypkt))
        print(mypkt.serialize())

        time.sleep(5)

gps_thread = Thread(target = get_gps)
gps_thread.start()

aprs_thread = Thread(target = aprs)
aprs_thread.start()