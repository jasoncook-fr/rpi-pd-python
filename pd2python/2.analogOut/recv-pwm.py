#! /usr/bin/python
from gpiozero import PWMLED
import OSC
import time, threading
from time import sleep
import os

led = PWMLED(13)
ledVal = 0

receive_address = '127.0.0.1', 9000

s = OSC.OSCServer(receive_address) # basic OSC server
s.addDefaultHandlers()

# define a message-handler function for the server to call.
def recv_handler(addr, tags, data, source):
    global ledVal
    #PWM of gpiozero uses float variable 0.0 to 1.0 (lowest to highest)
    ledVal = data[0] / 100.0

#add our function, first parameter corresponds to the OSC address you want to listen to
s.addMsgHandler("/pyRecv", recv_handler)

# Start OSCServer
st = threading.Thread( target = s.serve_forever )
st.start()

os.system('puredata -nogui -audiodev 3 send-pwm.pd &')

try :
    while 1 :
        time.sleep(.05) #a slight delay seems to smooth out the pwm a little bit
        led.value = ledVal

except KeyboardInterrupt :
    print "\nClosing OSCServer."
    s.close()
    print "Waiting for Server-thread to finish"
    st.join() ##!!!
    print "Done"

