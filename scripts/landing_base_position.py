#!/usr/bin/env python3
''' This nodes prints the location and orientation of the platform. It was used for testing '''
import rospy
import tf2_ros

if __name__ == '__main__':
    rospy.init_node("landing_base_location_node_initiated")
    rospy.loginfo("Position of landing base will be broadcasted soon. Please wait.")\
    
    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        try:
            trans = tfBuffer.lookup_transform("world","platform_link",rospy.Time())
            print("X: ", trans.transform.translation.x)
            print("Y: ", trans.transform.translation.y)
            print("Z: ", trans.transform.translation.z)
            print("x: ", trans.transform.rotation.x)
            print("y: ", trans.transform.rotation.y)
            print("z: ", trans.transform.rotation.z)
            print("w: ", trans.transform.rotation.w)
            print("-------------------------------")
        
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rospy.logwarn("An error occured while getting the transform")
            rate.sleep()
            continue

        rate.sleep()