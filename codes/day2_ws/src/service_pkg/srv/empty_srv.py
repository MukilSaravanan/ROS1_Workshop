#!/usr/bin/env python3

from std_srvs.srv import Empty, EmptyResponse
import rospy

def empty_response(req):
    print("Returning empty response_answer.")
    return EmptyResponse()

if __name__ == "__main__":
    rospy.logwarn("This is a warning")
    rospy.init_node('empty_srv')
    
    s = rospy.Service('print_srv', Empty, empty_response)
    #service name , service type(srv-file) , callback function(response)
    
    print("service started ")
    print("Ready to print empty response.")
    rospy.spin()

#service name , service type(srv-file) , callback function(response)