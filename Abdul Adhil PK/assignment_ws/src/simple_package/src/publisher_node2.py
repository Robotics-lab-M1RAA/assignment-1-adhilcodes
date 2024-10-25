#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def publisher_node():
    rospy.init_node('Abdul_pubnode', anonymous=True)

    pub1 = rospy.Publisher('Greetings', String, queue_size=10)
    #pub2 = rospy.Publisher('Greetings_2', String, queue_size=10)
    #pub3 = rospy.Publisher('Greetings_3', String, queue_size=10)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():

        message1 = "Hello, I am Abdul from Abdul_node1"
        #message2 = "Hello, I am Abdul from Abdul_node2"
        #message3 = "Hello, I am Abdul from Abdul_node3"

        rospy.loginfo(message1)
       # rospy.loginfo(message2)
        #rospy.loginfo(message3)

        pub1.publish(message1)
       # pub2.publish(message2)
        #pub3.publish(message3)


        rate.sleep()

if __name__ == '__main__':
    try:
        publisher_node()
    except rospy.ROSInterruptException:
        pass

