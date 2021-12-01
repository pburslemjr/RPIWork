#!/usr/bin/env python  
import roslib
roslib.load_manifest('tf_tree_publisher')
import rospy
import tf
from sensor_msgs.msg import Imu
from sensor_msgs.msg import NavSatFix



def handle_GPS_Data(data):
    br = tf.TransformBroadcaster()    
    br.sendTransform((data.latitude, data.longitude, data.altitude), tf.transformations.quaternion_from_euler(0, 0, 0), rospy.Time.now(), "base_link", "odom")

if __name__ == '__main__':
    rospy.init_node('drone_tf_broadcaster')    
    rospy.Subscriber('/fix', NavSatFix, handle_GPS_Data)
    rospy.spin()