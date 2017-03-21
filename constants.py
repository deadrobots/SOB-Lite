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

isClone = w.digital(CLONE_SWITCH)

# Servos
servoArm = 0
servoClaw = 1

armUp = 2000
armDown = 435

clawOpen = 152
clawClosed = 2047