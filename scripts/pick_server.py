#!/usr/bin/env python

from plps_launcher.srv import pick,pickResponse
import rospy

def handle_pick(req):
    print "pick execute start"
    print "parameters sent to server are:"
    print(req)
    rospy.sleep(5.1)
    print "pick execute finish"
    return pickResponse("1")

def pick_server():
    rospy.init_node('pick_server')
    s = rospy.Service('pick', pick, handle_pick)
    print "Ready to pick."
    rospy.spin()

if __name__ == "__main__":
    pick_server()
