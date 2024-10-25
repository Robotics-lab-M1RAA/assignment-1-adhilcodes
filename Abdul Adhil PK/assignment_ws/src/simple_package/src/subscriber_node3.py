#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("Node 3 heard: %s", data.data)

def subscriber_node():
    rospy.init_node('CET', anonymous=True)
    rospy.Subscriber('hello_college', String, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        subscriber_node()
    except rospy.ROSInterruptException:
        pass

