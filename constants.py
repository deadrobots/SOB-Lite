'''
Created on Jan 3, 2016
@author: graysonelias
'''

import wallaby as w

# Time
startTime = -1

# Motor ports
LMOTOR = 0
RMOTOR = 3

# Digital ports
CLONE_SWITCH = 9
RIGHT_BUTTON = 13

# Analog ports
TOPHAT = 0
ET = 5

isClone = w.digital(CLONE_SWITCH)

# Servos
servoArm = 0
servoClaw = 1

armUp = 1500
armDownMid = 100
armDown = 25

clawOpen = 0
clawClosed = 1980 #1550

if isClone:
    # Servos
    servoArm = 0
    servoClaw = 1

    armUp = 2000
    armDownMid = 500
    armDown = 300

    clawOpen = 152
    clawClosed = 2047


