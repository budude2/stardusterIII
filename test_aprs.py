#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
from aprslib.packets import PositionReport

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#address = ('localhost', int(8001))
address = ('192.168.2.3', int(8001))
sock.connect(address)

########## Setup the TNC ##########

## Set TXDELAY to 480 ms
#message = b'\xC0' + b'\x01' + b'\x50' + b'\xc0'
#sock.sendall(message)
#
## Set TXTAIL to 60 ms
#message = b'\xC0' + b'\x04' + b'\x06' + b'\xc0'
#sock.sendall(message)

########## APRS Data ##########

pkt = PositionReport()
pkt.latitude = 33.103172
pkt.longitude = -96.670547
pkt.fromcall = "N5WON"
pkt.tocall = "APRS"
pkt.altitude = 600
pkt.comment = "this is comment text"
pkt.path = "WIDE2-1"
print(str(pkt))

message = b'\xC0' + b'\x00' + str.encode(str(pkt)) + b'\xc0'

sock.sendall(message)

sock.close()
