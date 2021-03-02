# Gregory Polmatier
# For project 3 with Signorelli
import random
import math

import rospy
from turtleAPI import robot

RATE = rospy.Rate(10)

def diff(a1, a2):
    return abs(a1-a2)

def turn(angle):
    currYaw = r.getAngle()[2]
    finalAngle = currYaw + angle
    
    sign = 1
    if angle < 0:
        sign = -1

    if angle == 0:
        return

    print("deep in turn")

    speed = .3
    r.drive(angSpeed=speed*sign, linSpeed=0)
    while diff(finalAngle, r.getAngle()[2]) > .1:
        RATE.sleep()
        print(r.getAngle[2], finalAngle)

    return 

try:
    print("creating robot")
    r = robot()
    
    # drive straight
    r.drive(angSpeed=0, linSpeed=.25)
    while not rospy.is_shutdown():
        RATE.sleep()
        bump = r.getBumpStatus()
        print(bump)
        # print(bump['status'])
        if bump['state'] == '-1':
            if bump['bumper'] == '-1':
                if random.choice([True, False]):
                    print("got to turn")
                    turn(math.pi/2)
                else:
                    turn(-math.pi/2)    
            elif bump['bumper'] == '0':
                turn(-math.pi/4)
            else:
                turn(math.pi/4)
        r.drive(angSpeed=0, linSpeed=.25)
        
except Exception as e:
    print(e)
    # rospy.loginto("node now terminated")




