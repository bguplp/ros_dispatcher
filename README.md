# ros_dispatcher
A ROS-POMDP module for dispatcher the 'Solver' module actions on ROS

To integrate ROS-POMDP with your ROS project you need to add `/scripts/tcp_server.py` and `/scripts/dispatcher.py` to your project.

## integrate ROS-POMDP with your ROS project
1. add `/scripts/tcp_server.py` and `/scripts/dispatcher.py` to your `scripts` folder.
2. edit `dispatcher.py`:
* create a methode for every action as shown in `dispatcher.py` example, the method parameters are the PLP/action parameters. 
The method response is the observation received from the action.

