from gpiozero import PWMLED
from time import sleep

led = PWMLED(13)

while True:
    for x in range(0, 100, 1):
        ledVal = x / 100.0
        print ledVal
        led.value = ledVal
        sleep(0.01)
    for x in range(100, 0, -1):
        led.value = x / 100.0
        sleep(0.01)
