# RT1 - Assignment 2 - ROS Simulator 
RT1 - Assignment 2 - ROS Simulator 
Professor: Carmine Tommaso Recchiuto, Student: Aurora Bottino

# Assignment Description

Starting from the package assignment_2_2022 (https://github.com/CarmineD8/assignment_2_2022), which provides an implementation of an action server that moves a robot in the environment by implementing the bug0 algorithm, the following project creates a new package in which three nodes are developed:
(a) A node that implements an action client, allowing the user to set a target (x, y) or to cancel it. The node also publishes the robot position and velocity as a custom message (x,y, vel_x, vel_z), by relying on the values published on the topic /odom.
(b) A service node that, when called, prints the number of goals reached and cancelled.
(c) A node that subscribes to the robot’s position and velocity (using the custom message) and prints the distance of the robot from the target and the robot’s average speed. Use a parameter to set how fast the node publishes the information. 

# Nodes
There are six nodes in the package:

bug_as.py: the action server node that calls the services to move the robot to the goal position
go_to_point_service.py: the service node to move the robot to the goal position
wall_follow_service.py: the service node to avoid obstacles

and then I implemented the three nodes requested:

print_info.py: is the node that subscribes to the robot’s position and velocity from the /Position_velocity as a custom message and prints the distance of the robot from the target and the robot’s average speed with a frequency setted as a parameter in the lauch file.

service.py: is the service node that, when called, prints the number of goals reached and cancelled

user_input.py: is the action client node, allowing the user to set a target, x and y, or to cancel it. The node also publishes the robot position and velocity as a custom message on the /Position_velocity topic, by relying on the values published on the topic /odom. The structure of the node is described in the following flowchart:



