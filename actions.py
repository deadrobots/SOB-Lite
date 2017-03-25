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
    x.drive_speed(40,100)

def getOutAndGrabPoms():
    x.drive_speed(6, 75)
    u.move_servo(c.servoClaw, c.clawClosed, 20)
    msleep(1000)
    u.move_servo(c.servoArm, c.armUp)

def dropPomsInFurrow():
    x.drive_speed(12, 65)
    x.pivot_right(11, 50)  # angle was 6
    x.drive_speed(6, 35)
    u.move_servo(c.servoArm, c.armDown, 25)
    #x.drive_speed(4, 100)
    msleep(1000)
    u.move_servo(c.servoClaw, c.clawOpen)
    msleep(1000)
    u.move_servo(c.servoArm, c.armUp, 25)

def getToMiddle():
    x.drive_speed(-4, 100)
    x.pivot_right(-90, 100)
    x.drive_speed(-5.5, 50)
    x.drive_speed(30, 100)
    x.rotate(90, 50)
    x.drive_condition(100,100,u.seeLine,False)
    x.drive_speed(-1,100)
    x.rotate(-40,100)
    x.drive_condition(100, 100, u.seeLine, False)
    x._drive(60, 0)
    while u.seeLine():
        pass
    lineFollowRightTimed(6.5)

    #x.drive_speed(15, 100)
    #x.drive_speed(5, 50)

def exitMiddle():
    x.pivot_right(90, 100)
    x.drive_speed(-5.5, 50)
    x.drive_timed(100, 100, 4)
    x.rotate(-75, 75)
    x.drive_condition(100, 100, u.seeLine, False)

def lineFollowRightTimed(time):
    u.setWait(time)
    while u.getWait():
        if analog(c.TOPHAT) < 300:
            x._drive(40, 60)
        elif analog(c.TOPHAT) > 2400:
            x._drive(60, 40)