#!/usr/bin/env python

from plps_launcher.srv import *
import sys
import rospy





#------------------------------------------------------------------------------
#This File Is Only For Debug
#------------------------------------------------------------------------------


def observe_can_client(robot,location, can):
    print "observe_can execut start"
    rospy.wait_for_service('observe_can')
    try:
        pick_proxy = rospy.ServiceProxy('observe_can', observe_can)
        resp1 = observe_can_proxy(robot, location, location, can)
        print "observe_can result: "+resp1.result
        return resp1.result
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":
    observe_can_client("$robot1", "$location1", "$can")

    #observationActionSuccess = random.random() < 0.99;
    #print("observattion action success: %s" % observationActionSuccess)
    #CanAtRoom = True
    #print("Can at room: %s" % CanAtRoom)
    #observationFoundCan = (random.random() < 0.95) and CanAtRoom
    #if not observationActionSuccess:

