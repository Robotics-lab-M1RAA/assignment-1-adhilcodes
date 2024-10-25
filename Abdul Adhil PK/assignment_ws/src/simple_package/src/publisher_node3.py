#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def publisher_node():
    rospy.init_node('Abdul', anonymous=True)
    pub = rospy.Publisher('hello_class', String, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        message = "Hello RAA 24_26!"
        rospy.loginfo(message)
        pub.publish(message)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher_node()
    except rospy.ROSInterruptException:
        pass
