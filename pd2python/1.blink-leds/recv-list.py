#! /usr/bin/python
import RPi.GPIO as GPIO
import socket
import OSC
import time, threading
from time import sleep 
import os

GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BCM)   # Use physical pin numbering
GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)

# tupple with ip the OSC server will listen to. 
receive_address = '127.0.0.1', 9000
 
# OSC Server. there are three different types of server.
s = OSC.OSCServer(receive_address) # basic
##s = OSC.ThreadingOSCServer(receive_address) # threading
##s = OSC.ForkingOSCServer(receive_address) # forking

# this registers a 'default' handler (for unmatched messages),
# an /'error' handler, an '/info' handler.
# And, if the client supports it, a '/subscribe' & '/unsubscribe' handler
s.addDefaultHandlers()

# define a message-handler function for the server to call.
def printing_handler(addr, tags, stuff, source):
    print "---"
    print "received from :  %s" % OSC.getUrlStr(source)
    print "with addr : %s" % addr
    print "typetags : %s" % tags
    print "data : %s" % stuff
    print "---"
    print "gpio is %s" % stuff[1]
    GPIO.output(4, stuff[0])
    GPIO.output(17, stuff[1])
    GPIO.output(27, stuff[2])


s.addMsgHandler("/test", printing_handler) # adding our function, first parameter corresponds to the OSC address you want to listen to
     
     
# just checking which handlers we have added
print "Registered Callback-functions are :"
for addr in s.getOSCAddressSpace():
    print "#############################"
    print " handler address is ",addr
    print "#############################"
     
     
# Start OSCServer
print "\nStarting OSCServer. Use ctrl-C to quit."
st = threading.Thread( target = s.serve_forever )
st.start()
     
os.system('puredata -audiodev 3 send-list.pd')
print "=============="
print "starting PD!!!"
print "=============="
    
try :
    while 1 :
        time.sleep(5)
 
except KeyboardInterrupt :
    print "\nClosing OSCServer."
    s.close()
    print "Waiting for Server-thread to finish"
    st.join() ##!!!
    print "Done"

