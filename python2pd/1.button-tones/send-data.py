#! /usr/bin/python
import RPi.GPIO as GPIO
import OSC
from time import sleep
import os

buttonPin = [11,9,10]
buttonState = [False, False, False]
buttonFlag = [False, False, False]

GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BCM)   # Use physical pin numbering

'''
All three inputs are buttons.
Instead of adding resistors on the breadboard
we activate here the internal pull-up resistors
available to us on the Raspberry Pi
'''
for x in range(0,3):
    GPIO.setup(buttonPin[x], GPIO.IN, pull_up_down=GPIO.PUD_UP)

send_address = '127.0.0.1', 9001
c = OSC.OSCClient()
c.connect(send_address)   # localhost, port 57120
oscmsg = OSC.OSCMessage()
oscmsg.setAddress("/pdRecv") #address name is declared in pd patch

def sendMsg(button):
    oscmsg.append(button)
    c.send(oscmsg) #turn on the chosen toggle of our puredata patch
    oscmsg.remove(button)

os.system('puredata -nogui -audiodev 3 recv-data.pd &')
print "=============="
print "starting PD!!!"
print "=============="

while True: # Run forever
    for x in range(0,3):
        buttonState[x] = GPIO.input(buttonPin[x])
        if buttonState[x] == False and buttonFlag[x] == False:
            print "Button ",x," was pushed!"
            sendMsg(x)
            buttonFlag[x] = True
        elif buttonState[x] == True and buttonFlag[x] == True:
            buttonFlag[x] = False
    sleep(.01)

