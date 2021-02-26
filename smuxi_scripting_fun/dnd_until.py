#!/usr/bin/python3

from time import sleep
import os
import time

msg = os.environ['SMUXI_MSG'].strip()
chatroom =  os.environ['SMUXI_CHAT_ID']
sender = os.environ['SMUXI_SENDER']

if msg.find("dnd lights ") == 0 and chatroom == "#dimsumlabs" and sender == "dsl-wall":
    duration = msg.split("dnd lights ")[1].strip()
    last_letter = duration[-1:]
    if last_letter == "h": 
        multiplier = 60 * 60
    elif last_letter == "m":
        multiplier = 60
    elif duration == "cancel":
        multiplier = 0
    elif duration == "off":
        multiplier = 0
    else:
        multiplier = 1

    try:
        dnd_seconds = int(duration[:-1]) * multiplier
    except ValueError:
        dnd_seconds = 0

    dnd_expire = int(time.time()) + dnd_seconds

    os.system("cd ~/smuxi_scripting_fun; echo " + str(dnd_expire) + " > dnd_expire_epoch.txt")
    print("Session.Command /echo dnd mode enabled until " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(dnd_expire)))


