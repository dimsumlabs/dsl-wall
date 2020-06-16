#!/usr/bin/python3

# A Smuxi hook script. This hooks flashes the ceiling light when a new message
# on the #dimsumlabs channel was received.
#
# Usage: put this script in
# ~/.local/share/smuxi/hooks/engine/protocol-manager/on-message-received/
# and chmod +x it

from urllib import request
from time import sleep
import os
import sys

def change_ceiling_color(light_host, red, green, blue):
    color_url = 'rgb.lua?r={}&g={}&b={}'.format(red, green, blue)
    request_url = light_host + color_url

    print('request begin to {}'.format(request_url))
    req = request.Request(request_url, method='POST')
    res = request.urlopen(req)
    body = res.read()
    print('res body: ' + str(body))

if os.environ['SMUXI_MSG_TYPE'] != "Normal" or os.environ['SMUXI_CHAT_ID'] != "#dimsumlabs":
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

