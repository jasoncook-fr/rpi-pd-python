import time
import OSC
from ADS1x15 import ADS1015
import os

# create an ADS1015 ADC (12-bit) instance.
adc = ADS1015()

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
GAIN = 1

def sendMsg(val):
    oscmsg.append(val)
    c.send(oscmsg)
    oscmsg.remove(val)

os.system('puredata -nogui -audiodev 3 recv-adc.pd &')

print "=============="
print "starting PD!!!"
print "=============="
time.sleep(1)

send_address = '127.0.0.1', 8001
c = OSC.OSCClient()
c.connect(send_address)   # localhost, port 57120
oscmsg = OSC.OSCMessage()
oscmsg.setAddress("/pdRecv") #address name is declared in pd patch

# Main loop.
while True:
    # Read ADC channel 0
    adcVal = adc.read_adc(0, gain=GAIN)
    # Print the ADC values.
    print adcVal
    sendMsg(adcVal)
    # slight pause for screen buffer
    time.sleep(0.1)
