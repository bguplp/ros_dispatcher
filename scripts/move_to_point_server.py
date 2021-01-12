#!/usr/bin/env python

from plps_launcher.srv import move_to_point,move_to_pointResponse
import rospy

def handle_move_to_point(req):
    print "move_to_point execute start"
    print "parameters sent to server are:"
    print(req)
    rospy.sleep(8.1)
    print "move_to_point execute finish"
    return move_to_pointResponse("1")

def move_to_point_server():
    rospy.init_node('move_to_point_server')
    s = rospy.Service('move_to_point', move_to_point, handle_move_to_point)
    print "Ready to move to a point."
    rospy.spin()

if __name__ == "__main__":
    move_to_point_server()

