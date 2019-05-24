#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import struct

mac = 'AA:BB:CC'

ip = '84'
for hex in mac.split(":"):
    ip += '.' + str(int(hex, 16))
print("IP PLC:", ip)
