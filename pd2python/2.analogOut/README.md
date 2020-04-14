## Analog out example (PWM) 
The python code uses gpiozero module instead of the traditional GPIO. I decided to make the code using this alternative because it can be produced on all gpio pins, as it is a software PWM. The raspberry pi 3 offers 4 hardware PWM pins. The Raspiaudio shield uses 2 of these. The resulting pwm on an LED shows some flicker. It's not terribly smooth in my opinion. This being said, it may be entirely satisfactory for certain applications (changing motor speeds for example).

The puredata patch included requires the following external
```
mapping (for autoscale)
```
Keeping all .pd and .py scripts in the same folder, launch the code with the following command:
```
python recv-pwm.py
```
The Python code will launch the PureData code without graphic interface. If you wish to launch the interface at the same time simply edit the os.system command in the python code, removing the option '-nogui'

