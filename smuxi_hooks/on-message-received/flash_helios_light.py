#!/usr/bin/python3

# A Smuxi hook script. This hooks flashes the ceiling light when a new message
# on the #dimsumlabs channel was received.
#
# Copyright (C) 2021, 2024 Mirco Bauer <meebey@meebey.net>
# Copyright (C) 2021 Neil Pahl <neildaemond@gmail.com>
# Copyright (C) 2021 Felix E. Klee <felix.klee@inka.de>

from urllib import request
from time import sleep
import os
import sys
import time
import re
from os.path import exists

DND_TIME_FILENAME="$HOME/dsl-wall/smuxi_scripting_fun/dnd_expire_epoch.txt"
if exists(DND_TIME_FILENAME) == True:
    path = os.path.expandvars(DND_TIME_FILENAME);
    dnd_file = open(path, "r")
    dnd_on = int(dnd_file.read().strip()) > time.time()
else:
    dnd_on = False

def get_ceiling_color(light_host):
    request_url = light_host + 'rgb'
    req = request.Request(request_url)
    # timeout after 1 second as the light might be turned off
    res = request.urlopen(req, data=None, timeout=1)
    body = res.read().decode("ascii")
    print("body: '{}'".format(body))
    match = re.search("(?P<red>[0-9]+)\n" +
                      "(?P<green>[0-9]+)\n" +
                      "(?P<blue>[0-9]+).*",
                      body)
    if not match:
        return None
    return ( match.group('red'),
             match.group('green'),
             match.group('blue') )

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

helios_service = 'http://helios2.in.dimsumlabs.com/'
#helios2_service = 'http://helios2.in.dimsumlabs.com/'
# HACK: disable helios2 as it is broken and needs repair. The HTTP/REST call
# just hang forever...
helios2_service = None

# WTF: 0 is brightest value, lulz
white = (0, 0, 0)

current_color = get_ceiling_color(helios_service)
if not current_color:
    print('could not determine current color, assuming white...')
    current_color = white

# color value range 0 to 1024
light_pink = (7, 751, 130)
light_green = (783, 7, 652)
change_ceiling_color(helios_service, *light_green)
if helios2_service:
    change_ceiling_color(helios2_service, *light_green)

# sleep for 1 second to give time for the color transition to complete
sleep(1)

# restore to previous color
change_ceiling_color(helios_service, *current_color)
if helios2_service:
    change_ceiling_color(helios2_service, *current_color)
