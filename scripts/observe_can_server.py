#!/usr/bin/env python

from plps_launcher.srv import observe_can,observe_canResponse
import random
import rospy

def handle_observe_can(req):
    print "observe_can service execute start"
    print "parameters sent to server are:"
    print(req)
    rospy.sleep(8.1)
    print "robot: "+req.robot
    print "location: " + req.location
    print "object: " + req.can

    actionFailed = random.random() < 0.01
    observedSuccesfuly = random.random() < 0.95

    #Responses: '0': action failed, '1': action succeeded object not at room, '2': action succeeded object at room

    if actionFailed:
        print "action failed response is: '0'"
        return observe_canResponse("0")

    print "location param:" + req.location
    print "object param:" + req.can

#.rstrip(' \t\r\n\0') is removing trailing nulls
    if req.location.rstrip(' \t\r\n\0') == '$robot_lab' and req.can.rstrip(' \t\r\n\0') == '$can':
        if observedSuccesfuly :
            print "action succeeded, observed can at room, response is: '2'"
            return observe_canResponse("2")
        else:
            print "action succeeded, could not observe can at room, response is: '1'"
            return observe_canResponse("1")
    print "action succeeded, can not at room, response is: '1'"
    return observe_canResponse("1")
    #print "observe_can execute finish"

def observe_can_server():
    rospy.init_node('observe_can_server')
    s = rospy.Service('observe_can', observe_can, handle_observe_can)
    print "Ready to observe can."
    rospy.spin()

if __name__ == "__main__":
    observe_can_server()

