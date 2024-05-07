#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from service_pkg.srv import velocity, velocityResponse

class vel_server:
    def __init__(self):
        pub_topic_name = '/turtle1/cmd_vel'
        sub_topic_name = '/turtle1/pose'
        self.pub = rospy.Publisher(pub_topic_name, Twist, queue_size=10)
        self.sub = rospy.Subscriber(sub_topic_name, Pose, self.pose_callback)
        self.service = rospy.Service('velocity_change_service', velocity, self.velo_cb)
        self.velocity_msg = Twist()
        # self.pose = Pose()
        # self.rate = rospy.Rate(1)

    def velo_cb(self, req):
        self.velocity_msg.linear.x = req.vel
        self.velocity_msg.angular.z = req.ang
        return "velocity of robot changed"


    def pose_callback(self, msg):
        self.pub.publish(self.velocity_msg)

if __name__ == '__main__':
    rospy.init_node('turtle_vel_test')
    vel_server()
    rospy.spin()