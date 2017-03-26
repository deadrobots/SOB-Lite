#!/usr/bin/python
import actions as act
import utils as u


def main():
    # act.test()
    act.init()
    act.getOutAndGrabPoms()
    act.dropPomsInFurrow()
    act.getToMiddle()
    act.exitMiddle()
    act.dropSecondPoms()
    act.goToBarn()
    u.DEBUGwithWait()

if __name__ == "__main__":
    import os
    import sys
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    main()

