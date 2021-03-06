'''
Created on Jan 3, 2016
@author: graysonelias
'''

'''
This module provides some of our standard methods.
'''

import constants as c

from wallaby import ao
from wallaby import msleep
from wallaby import digital
from wallaby import seconds
from wallaby import freeze
from wallaby import set_servo_position
from wallaby import get_servo_position
from wallaby import analog
import drive as d
import wallaby as w

def waitForButton():
    print "Press Button..."
    while not digital(c.RIGHT_BUTTON):
        pass
    msleep(1)
    print "Pressed"
    msleep(1000)


def DEBUG():
    freeze(c.LMOTOR)
    freeze(c.RMOTOR)
    ao()
    print 'Program stop for DEBUG\nSeconds: ', seconds() - c.startTime
    exit(0)


def DEBUGwithWait():
    freeze(c.LMOTOR)
    freeze(c.RMOTOR)
    ao()
    print 'Program stop for DEBUG\nSeconds: ', seconds() - c.startTime
    msleep(5000)
    exit(0)

# Servo Constants
DELAY = 10

# Servo Control #

def move_servo(servo, endPos, speed=10):  # Moves a servo with increment "speed".
    # speed of 1 is slow
    # speed of 2000 is fast
    # speed of 10 is the default
    now = get_servo_position(servo)
    if speed == 0:
        speed = 2047
    if endPos >= 2048:
        print "Programmer Error"
        exit(0)
    if endPos < 0:
        print "Programmer Error"
        exit(0)
    if now > endPos:
        speed = -speed
    for i in range(int(now), int(endPos), int(speed)):
        set_servo_position(servo, i)
        msleep(DELAY)
    set_servo_position(servo, endPos)
    msleep(DELAY)


def move_servo_timed(servo, endPos, time):  # Moves a servo over a specific time.
    if time == 0:
        speed = 2047
    else:
        speed = abs((DELAY * (get_servo_position(servo) - endPos)) / time)
    move_servo(servo, endPos, speed)

# Loop break timers #

time = 0  # This represents how long to wait before breaking a loop.


def setWait(DELAY):  # Sets wait time in seconds before breaking a loop.
    global time
    time = seconds() + DELAY


def getWait():  # Used to break a loop after using "setWait". An example would be: setWiat(10) | while true and getWait(): do something().
    return seconds() < time

def seeLine():
    return analog(0) > 2400



def wait4light():
    while not calibrate(c.STARTLIGHT):
        pass
    wait4(c.STARTLIGHT)

from wallaby import left_button, right_button

def calibrate(port):
    print "Press LEFT button with light on"
    while not left_button():
        pass
    lightOn = analog(port)
    print "On value =", lightOn
    if lightOn > 200:
        print "Bad calibration"
        return False
    msleep(1000)
    print "Press RIGHT button with light off"
    while not right_button():
        pass
    lightOff = analog(port)
    print "Off value =", lightOff
    if lightOff < 3000:
        print "Bad calibration"
        return False

    if (lightOff - lightOn) < 2000:
        print "Bad calibration"
        return False
    c.startLightThresh = (lightOff - lightOn) / 2
    print "Good calibration! ", c.startLightThresh
    return True


def wait4(port):
    print "waiting for light!! "
    while analog(port) > c.startLightThresh:
        pass
