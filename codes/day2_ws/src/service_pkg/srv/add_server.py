#!/usr/bin//env python3

import rospy
from service_pkg.srv import addition, additionResponse

def server_cb(req):
        # print("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))
    # rospy.init_node('server_cd')
    # rospy.spin()
    return additionResponse(req.x + req.y)

if __name__ == "__main__":
    rospy.init_node('addition_server')
    s = rospy.Service('add_ints', addition, server_cb)
    print("Ready to add_ints.")
    rospy.spin()
