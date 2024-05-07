#!/usr/bin/env python3

from std_srvs.srv import Empty, EmptyResponse
from geometry_msgs.msg import Twist
import rospy

def empty_response(req):
    vel_msg = Twist()
    for i in range(15):
        vel_msg.linear.x = 1
        vel_msg.angular.z = 0.5
        pub.publish(vel_msg)
        rate.sleep()
    print("Returning empty response_answer.")
    return EmptyResponse()

if __name__ == "__main__":
    rospy.logwarn("This is a warning")
    rospy.init_node('empty_srv')
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10) 
   
    s = rospy.Service('rotate_turtle_srv', Empty, empty_response)
    print("Ready to return empty response.")
    rate = rospy.Rate(1)

    rospy.spin()