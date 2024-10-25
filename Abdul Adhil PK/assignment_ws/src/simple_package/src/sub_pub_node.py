#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("Node 2 heard: %s", data.data)
    pub = rospy.Publisher('hello_college', String, queue_size=10)
    message = "Hello Abdul Welcome!"
    rospy.loginfo(message)
    pub.publish(message)

def subscriber_node():
    rospy.init_node('M1RAA 2024', anonymous=True)
    rospy.Subscriber('hello_class', String, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        subscriber_node()
    except rospy.ROSInterruptException:
        pass

