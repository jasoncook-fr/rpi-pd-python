# RPi-pd-python

This project illustrates basic access control of GPIO pins on a Raspberry Pi using PureData. OSC protocol is used to communicate between PureData to Python. Python then accesses the GPIO of the Raspberry Pi

Examples with supporting documentation are included in each folder. 
To execute the examples, simply navigate to a folder containing the codes and follow the instructions

Base dependencies for Python are obtained as follows:
```
sudo apt-get install pip
sudo pip install pyosc
```

Externals required for puredata are as follows:
```
osc
cyclone
iemnet (might be included by default)
```

## PD2Python
Examples illustrate use of GPIO outputs.
Pd controls behaviors of lights, actuators, etc. 

## Python2PD
Examples illustrate use of GPIO inputs.
Pd is controlled by buttons, sensors, etc.

#### mentions
Many thanks to the website [Really Useful Plugins](https://reallyusefulplugins.tumblr.com/richsynthesis) for their excellent PureData synthesis tutorials. <br />
Many thanks to [Raspiaudio](https://www.raspiaudio.com/raspiaudio-aiy) for the wonderful audio shield. Very practical for economising table space and providing quality sound while prototyping
