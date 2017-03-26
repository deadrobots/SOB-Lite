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
    u.move_servo(c.servoArm, c.armUp, 50)
    u.move_servo(c.servoClaw,c.clawClosed, 20)
    msleep(100)
    u.move_servo(c.servoClaw, c.clawOpen, 20)
    while seeHay():
        pass
    x.drive_condition(100, 100, u.seeLine, False)
    u.move_servo(c.servoArm, c.armDown, 50)
    u.wait4light()
    c.startTime = seconds()

def test():
    print"test"
    if c.isClone:
        print "I am Clone"
    else:
        print "I am Prime"
    x.drive_speed(50,100)
    u.DEBUG()

def seeHay():
    return analog(5) < 2200

def getOutAndGrabPoms():
    # x.drive_speed(6, 75)
    x._drive(75,75)
    msleep(1000)
    x._drive(0,0)
    u.move_servo(c.servoClaw, c.clawClosed, 20)
    u.move_servo(c.servoArm, c.armUp, 50)

def dropPomsInFurrow():
    x.drive_speed(9.5, 65)
    if c.isClone:
        x.pivot_right(11, 50)
    else:
        x.pivot_right(13, 50)
    x.drive_speed(7, 35)
    if c.isClone:
        u.move_servo(c.servoArm, c.armDownMid, 25)
    else:
        u.move_servo(c.servoArm, c.armDown, 25)
    #x.drive_speed(4, 100)
    msleep(1000)
    u.move_servo(c.servoClaw, c.clawOpen,15)
    msleep(1000)
    u.move_servo(c.servoArm, c.armMid, 7.5)
    msleep(100)
    u.move_servo(c.servoClaw, c.clawClosed, 200)
    msleep(200)
    u.move_servo(c.servoArm, c.armDown, 20)
    msleep(100)
    u.move_servo(c.servoArm, c.armMid, 20)
    msleep(100)
    u.move_servo(c.servoArm, c.armDown, 20)
    msleep(100)
    u.move_servo(c.servoArm, c.armUp, 20)
    msleep (100)
    u.move_servo(c.servoClaw, c.clawOpen, 200)
x
def getToMiddle():
    x.drive_speed(-4, 100)
    x.pivot_right(-90, 100)
    x.drive_speed(-5.5, 50)
    if c.isClone:
        x.drive_speed(31,100)
    else:
        x.drive_speed(28, 100)
    x.rotate(90, 50)
    x.drive_condition(100,100,u.seeLine,False)
    x.drive_speed(-1,100)
    x.rotate(-40,100)
    x.drive_condition(100, 100, u.seeLine, False)

    # x.pivot_left_condition(60, u.seeLine)

    x._drive(60, 0)
    while u.seeLine():
        pass

    if c.isClone:
        lineFollowRightTimed(8)
    else:
        lineFollowRightTimed(7)



def exitMiddle():
    x.drive_speed(-2,100)
    x.pivot_right(90, 100)
    x.drive_speed(-6.5, 50)
    if c.isClone:
        x.drive_timed(100,100,4.5)
    else:
        x.drive_timed(100, 100, 4)
    x.rotate(-75, 75)
    x.drive_condition(100, 100, u.seeLine, False)


def dropSecondPoms():
    x.rotate(30,75)
    x.drive_speed(15,100)
    # x.rotate(160,75)
    x.pivot_right(140, 75)
    x.drive_speed(-10,75)
    x.drive_speed(3.9,75)
    x.rotate(90,75)
    x.drive_speed(-8,75)
    u.move_servo(c.servoArm, c.armDown, 10)
    #x.drive_condition(95,100, u.seeLine,False)
    if c.isClone:
        x._drive(90,100)
        msleep(2100)
    else:
        x._drive(100,100)
        msleep(2500)
    x._drive(0,0)
    u.move_servo(c.servoClaw, c.clawClosed,20)
    msleep(100)
    u.move_servo(c.servoArm, c.armUp, 50)
    x.rotate(-90,60)
    x.drive_speed(5,100)
    x.drive_speed(65,100)
    x.rotate(-180,75)
    if c.isClone:
        x.drive_speed(-20,100)
        x.drive_speed(14.75, 100)
        x.rotate(-85, 75)
        x.drive_speed(16.5,100)
        x.drive_speed(-1, 100)
    else:
        x.drive_speed(-14,100)
        x.drive_speed(14.75, 100)
        x.rotate(-90, 75)
        x.drive_condition(100, 100, u.seeLine, False)
        x.drive_condition(25, 25, u.seeLine)
    u.move_servo(c.servoArm, c.armDownMid,10)
    u.move_servo(c.servoClaw, c.clawOpen,10)
    u.move_servo(c.servoArm,c.armMid,10)
    msleep(100)
    u.move_servo(c.servoClaw, c.clawClosed, 200)
    msleep(100)
    u.move_servo(c.servoArm, c.armDown, 30)
    msleep(100)
    u.move_servo(c.servoArm, c.armMid, 30)
    msleep(100)
    u.move_servo(c.servoArm, c.armDown, 30)
    msleep(100)
    u.move_servo(c.servoArm, c.armMid, 30)
    msleep(100)
    u.move_servo(c.servoClaw, c.clawOpen, 200)
    msleep(500)
    x.drive_condition(-50, -50, u.seeLine, False)
    x.drive_condition(-50, -50, u.seeLine)
    u.move_servo(c.servoArm, c.armFurrow)
    msleep(100)

def goToBarn():
    x.drive_speed(3, -100)
    u.move_servo(c.servoArm, c.armDown)
    x.drive_speed(5, -100)
    u.move_servo(c.servoArm, c.armUp)
    x.pivot_right(-85, 50)
    x.drive_speed(6.5, 100)
    x.pivot_right(90, 50)
    x.drive_condition(100, 100, u.seeLine, False)
    x.drive_condition(-50, -50, u.seeLine)
    u.move_servo(c.servoArm, c.armFurrow)
    msleep(100)
    x.drive_speed(3, -100)
    u.move_servo(c.servoArm, c.armDown)
    x.drive_speed(5, -100)
    u.move_servo(c.servoArm, c.armUp)
    x.pivot_right(-85, 50)
    x.drive_speed(6.5, 100)
    x.pivot_right(90, 50)
    x.drive_condition(100, 100, u.seeLine, False)
    x.drive_condition(-50, -50, u.seeLine)
    u.move_servo(c.servoArm, c.armFurrow)
    msleep(100)
    x.drive_speed(3, -100)
    x.drive_speed(1, 100)
    u.move_servo(c.servoArm, c.armDown)
    x.drive_speed(33, -100)
    u.move_servo(c.servoArm, c.armUp, 20)
    u.DEBUGwithWait()

def lineFollowRightTimed(time):
    u.setWait(time)
    while u.getWait():
        if analog(c.TOPHAT) < 300:
            x._drive(40, 60)
        elif analog(c.TOPHAT) > 2400:
            x._drive(60, 40)