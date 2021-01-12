#!/usr/bin/env python

from plps_launcher.srv import *
import rospy





#------------------------------------------------------------------------------
#This File Is Only For Debug
#------------------------------------------------------------------------------


def pick_client(robot,object, location):
    print "pick execut start"
    rospy.wait_for_service('pick')
    try:
        pick_proxy = rospy.ServiceProxy('pick', pick)
        resp1 = pick_proxy(robot,object, location)
        print "pick result: ",resp1.result
        return resp1.result
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":
    pick_client("$robot1", "$object1","$location1")