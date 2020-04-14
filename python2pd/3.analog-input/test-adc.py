import time

# Import the ADS1x15 module.
from ADS1x15 import ADS1015

# create an ADS1015 ADC (12-bit) instance.
adc = ADS1015()

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
GAIN = 1

# Print nice channel column headers.
print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
print('-' * 37)

# Main loop.
while True:
    # Read all the ADC channel values in a list.
    values = [0]*4
    for i in range(4):
        values[i] = adc.read_adc(i, gain=GAIN)
    # Print the ADC values.
    print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
    # slight pause for screen buffer
    time.sleep(0.1)
