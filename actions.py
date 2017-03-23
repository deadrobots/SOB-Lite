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

def dropPomsInFurrow():
    x.pivot_right(9, 50) #angle was 6
    x.drive_speed(12, 65)
    x.drive_speed(6, 35)
    u.move_servo(c.servoArm, c.armDown)
    #x.drive_speed(4, 100)
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
    x.drive_speed(14, 100)
    x.drive_timed(100, 10, 1.4)
    lineFollowRightTimed(10)


    #x.drive_speed(15, 100)
    #x.drive_speed(5, 50)

def lineFollowRightTimed(time):
    u.setWait(time)
    while u.getWait():
        if analog(5) < 300:
            x._drive(-100, 100)
        else: analog(5) > 2900
        x._drive(100, -100)