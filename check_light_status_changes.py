#!/usr/bin/python3

# A cronjob script to check the current light status (on or off). If the status changes, we
# send a message to the #dimsumlabs IRC channel via Smuxi.
#
# Add this script as crontab entry via "crontab -e" with the same user that smuxi-frontend-gnome is running as:
# *  * * * * /home/pi/check_light_status_changes.py > /home/pi/check_light_status_changes.out 2>&1
#
# For the message sending to to work, it requires Smuxi 1.3 or a git build > May 18th of May 2023 to support --execute-command='/say something'
# https://github.com/meebey/smuxi/commit/0fcced4fe95edc2740a379a3fc6ec0f06153a62b
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                    Version 2, December 2004
#
# Copyright (C) 2024 Mirco Bauer <meebey@meebey.net>
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.

from urllib import request
import os
import time

helios_rest_service = 'http://helios.in.dimsumlabs.com'
previous_light_state_file_path = '$HOME/.helios_light_state'

def is_light_on(helios_host):
    service_url = '{}/rgb'.format(helios_host);
    print(service_url);
    # attempt to fetch the state for 3 times as the REST call fails
    # sometimes because of unreliable comms/API
    for i in range(3):
        req = request.Request(service_url, method='GET')
        try:
            # timeout after 1 second as the light might be turned off
            res = request.urlopen(req, data=None, timeout=2)
            body = res.read()
            return True
        except:
            print('attempt has failed')
            time.sleep(2)
            continue
    
    # all state fetch attempts have failed, we determine with high convidence: lights are off -> False
    return False

def get_previous_light_status():
    path = os.path.expandvars(previous_light_state_file_path);
    try:
        f = open(path, "r")
        state_content = f.read()
        f.close()
        return state_content.lower() == 'true';
    except:
        return False;

def set_previous_light_status(status):
    path = os.path.expandvars(previous_light_state_file_path);
    f = open(path, "w+")
    f.write(str(status))
    f.close()

def execute_smuxi_command(command):
    os.system("mono /opt/smuxi*/smuxi-frontend-gnome.exe --execute-command='{}'".format(command));

if is_light_on(helios_rest_service):
    print('light is on')
    if get_previous_light_status() == False:
        print('light state has changed')
        execute_smuxi_command('/me senses lights are on');
    set_previous_light_status(True)
else:
    print('light is off')
    if get_previous_light_status() == True:
        print('light state has changed')
        execute_smuxi_command('/me senses lights are off');
    set_previous_light_status(False)
