#!/usr/bin/env python

from plps_launcher.srv import *
import sys
import rospy





#------------------------------------------------------------------------------
#This File Is Only For Debug
#------------------------------------------------------------------------------


def move_to_point_client(robot,location, destination, floor):
    print "move_to_point execut start"
    rospy.wait_for_service('move_to_point')
    try:
        pick_proxy = rospy.ServiceProxy('move_to_point', move_to_point)
        resp1 = move_to_point_proxy(robot, location, destination, floor)
        print "move_to_point result: "+resp1.result
        return resp1.result
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":
    move_to_point_client("$robot1", "$location1", "$detination1", "$floor")
