#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
from time import sleep

# This node moves the landing platform back and forth
def mover():
    # initiating the node
    rospy.init_node("platform_mover")
    rospy.loginfo("Mover node initiated")
    model_name = rospy.get_param('~model_name','default_value')
    sleep(1)
    # making sure we publish on the topic that our controller is expected to recieve its set points
    platform_position_publisher = rospy.Publisher("/moving_{}/slider_joint_position_controller/command".format(model_name), Float64, queue_size=10)
    rate = rospy.Rate(50) # 50 hz
    # This will be the value published as the desired position
    i = 0
    # Flag in order to toggle the incrementation of i
    flag = 1
    # These are the joint limits as in the urdf file
    upper_movement_limit = 4
    lower_movement_limit = 0
    while not rospy.is_shutdown():
        # check if i reached our joint limits and determine whether to toggle or not
        if i >= upper_movement_limit or i <=lower_movement_limit:
            if i <= lower_movement_limit:
                flag = 1
            else:
                flag = 0
        # based on the flag, determine to increase or decrease the value of i
        if flag == 1:
            i+=0.02
        else:
            i-=0.02
        # publish i to the controller
        platform_position_publisher.publish(i)
        rate.sleep()

if __name__ == '__main__':
    try:
        mover()
    except rospy.ROSInterruptException:
        pass
