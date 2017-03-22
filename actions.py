from ssl import _ASN1Object

import motorsPlusPlus as x
import utils as u
import constants as c
from wallaby import *

def init():
    print "init"
    if c.isClone:
        print "I am Clone"
    else:
        print "I am Prime"
    enable_servos()
    u.move_servo(c.servoArm, c.armDown)
    u.move_servo(c.servoClaw, c.clawOpen)
    u.waitForButton()

def test():
    x.drive_speed(50, 50)

def getOutAndGrabPoms():
    x.drive_speed(6, 75)
    u.move_servo(c.servoClaw, c.clawClosed)
    msleep(1000)
    u.move_servo(c.servoArm, c.armUp)
    u.waitForButton()

def dropPomsInFurrow():
    x.pivot_right(5, 50)
    x.drive_speed(18, 65)
    u.move_servo(c.servoArm, c.armDown)
    msleep(1000)
    u.move_servo(c.servoClaw, c.clawOpen)
    msleep(1000)
    u.move_servo(c.servoArm, c.armUp)

def getToMiddle():
    x.drive_speed(-4, 50)
    x.pivot_right(-90, 50)
    x.drive_speed(-4, 50)
    x.drive_speed(30, 100)
    x.rotate(90, 50)
    x.drive_speed(15, 100)
    x.drive_speed(5, 50)

