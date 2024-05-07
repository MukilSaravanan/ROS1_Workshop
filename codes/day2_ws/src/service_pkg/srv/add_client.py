#!/usr/bin/env python3


import sys
import rospy
from service_pkg.srv import addition, additionResponse


def add_two_ints_client(x, y):
    rospy.wait_for_service('add_ints')
    add_ints = rospy.ServiceProxy('add_ints', addition)
    #we need to write service name and srv file name
    resp1 = add_ints(x, y)
    print(resp1.result)
    #we need to add responce


if __name__ == "__main__":
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    add_two_ints_client(x, y)