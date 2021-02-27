#!/usr/bin/python3

# A Smuxi hook script. This hooks flashes the ceiling light when a new message
# on the #dimsumlabs channel was received.

from urllib import request
from time import sleep
import os
import sys
import time

dnd_file = open("/home/pi/dsl-wall/smuxi_scripting_fun/dnd_expire_epoch.txt", "r")
dnd_on = int(dnd_file.read().strip()) > time.time()

def change_ceiling_color(light_host, red, green, blue):
    color_url = 'rgb.lua?r={}&g={}&b={}'.format(red, green, blue)
    request_url = light_host + color_url

    print('request begin to {}'.format(request_url))
    req = request.Request(request_url, method='POST')
    # timeout after 1 second as the light might be turned off
    res = request.urlopen(req, data=None, timeout=1)
    body = res.read()
    print('res body: ' + str(body))

if os.environ['SMUXI_MSG_TYPE'] != "Normal" or os.environ['SMUXI_CHAT_ID'] != "#dimsumlabs" or dnd_on:
    sys.exit(0)

helios_service = 'http://helios.lan/'
helios2_service = 'http://helios2.lan/'

# color value range 0 to 1024
light_pink = (7, 751, 130)
light_green = (783, 7, 652)
change_ceiling_color(helios_service, *light_green)
change_ceiling_color(helios2_service, *light_green)

# sleep for 1 second to give time for the color transition to complete
sleep(1)

# WTF: 0 is brightest value, lulz
white = (0, 0, 0)
change_ceiling_color(helios_service, *white)
change_ceiling_color(helios2_service, *white)

