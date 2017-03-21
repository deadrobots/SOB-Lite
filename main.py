#!/usr/bin/python
import actions as act


def main():
    act.init()
    act.getOutAndGrabPoms()
    act.dropPomsInFurrow()
    act.getToMiddle()

if __name__ == "__main__":
    import os
    import sys
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    main()

