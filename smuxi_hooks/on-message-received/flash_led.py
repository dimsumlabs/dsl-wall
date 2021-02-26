#!/usr/bin/python3

from gpiozero import LED
from time import sleep
import os

led = LED(14)

if os.environ['SMUXI_MSG_TYPE'] == "Normal" and os.environ['SMUXI_CHAT_ID'] == "#dimsumlabs":
    led.on()
    sleep(1)
    led.off()

