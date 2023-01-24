#!/usr/bin/env python

import rospy
import actionlib
import actionlib.msg
import assignment_2_2022.msg
from std_srvs.srv import *
import sys
import select
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Twist
from assignment_2_2022.msg import Position_velocity

 
def pub_values(msg):
	
	global pub
	
	# Position from the msg
	pos = msg.pose.pose.position
	
	# Twist from the msg
	velocity = msg.twist.twist.linear
	
	# Create custom message
	position_velocity = Position_velocity()
	
	# Costume message
	position_velocity.x=pos.x
	position_velocity.y=pos.y
	position_velocity.v_x=velocity.x
	position_velocity.v_y=velocity.y
	
	# Publish the custom message
	pub.publish(position_velocity)
	
def client():
	
    # Action client
    client = actionlib.SimpleActionClient('/reaching_goal', assignment_2_2022.msg.PlanningAction)
    
    # Wait for the server to be started
    client.wait_for_server()

    while not rospy.is_shutdown():
	  
      # User enters x and y from keyboard
      x_position = float(input("x: "))
      y_position = float(input("y: "))
   

      # Goal position
      goal = assignment_2_2022.msg.PlanningGoal()
      goal.target_pose.pose.position.x = x_position
      goal.target_pose.pose.position.y = y_position

      # Send the goal to the server
      client.send_goal(goal)
      
      
      # Cancel the goal in 10 seconds by typing c
      print("Enter 'c' to cancel the goal:")
      val = select.select([sys.stdin], [], [], 10)[0]
      
      if val:
        value = sys.stdin.readline().rstrip()
				   
        if (value == "c"):
	  # Goal cancelled
          print("Goal has been cancelled!")
          client.cancel_goal()


    

 


def main():

    # Inizialize the node
    rospy.init_node('user_input')

    # Global pub
    global pub
    
    # publisher: send a message which contains two parameters (velocity and position)
    pub = rospy.Publisher("/pos_vel", Position_velocity, queue_size = 1)
    
    # subscriber: get from "Odom" two parameters (velocity and position)
    sub_from_Odom=rospy.Subscriber("/odom",Odometry,pub_values)
    
    # Calling the function client
    client()

if __name__ == '__main__':
    main()
