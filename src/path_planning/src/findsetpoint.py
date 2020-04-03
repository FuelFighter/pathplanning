#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Range
from geometry_msgs.msg import Point
from std_msgs.msg import Float64
from nav_msgs.msg import OccupancyGrid
import math
import numpy as np


def callback(data):
    grid=[]
    for i in range(len(data.data)):
	if (0<data.data[i]<50):
		grid.append(0)
	elif (data.data[i]>=50):
		grid.append(1)
	else: grid.append(-1)
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", grid)
    
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("map", OccupancyGrid , callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()

