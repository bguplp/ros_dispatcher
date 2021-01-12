#!/usr/bin/env python
import rospkg
import os
import signal
import socket
import threading
from subprocess import Popen
import time
import rospy
from sensor_msgs.msg import Image
import cv2 as cv
import numpy as np
from cv_bridge import CvBridge, CvBridgeError



def handle_client_connection(client_socket):
    try:
        request = client_socket.recv(1024)
        print 'Received {}'.format(request)
        client_socket.send('ACK!')
        client_socket.close()
        print 'connection ended'
    except Exception as e:
        print 'exception thrown: ', e
        client_socket.close()
        print 'connection ended'


def start_tcp_server(host, port):
    #import pdb;
    #pdb.set_trace()
    #with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    print('bind executed')
    server.listen(100)

    while not rospy.is_shutdown():
        try:
            client_sock, address = server.accept()
            print 'Accepted connection from {}:{}'.format(address[0], address[1])
            client_handler = threading.Thread(
                target=handle_client_connection,
                args=(client_sock,)
                # without comma you'd get a... TypeError: handle_client_connection() argument after * must be a sequence, not _socketobject
            )
            client_handler.start()
        except Exception as e:
            print e
            server.close()
            print('socket closed')
    server.close()
    print('TCP server closed')





if __name__ == '__main__':
 try:
     HOST = socket.gethostbyname("localhost")
     PORT = 1770
     print('HOST:',HOST)
     start_tcp_server(HOST, PORT)
 except rospy.ROSInterruptException:
  pass