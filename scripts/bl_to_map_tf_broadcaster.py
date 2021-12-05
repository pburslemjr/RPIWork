#!/usr/bin/env python  
import roslib
roslib.load_manifest('tf_tree_publisher')
import rospy
import tf
from sensor_msgs.msg import Imu
from sensor_msgs.msg import NavSatFix
from nav_msgs.msg import Odometry



def handle_GPS_Data(data):
    br = tf.TransformBroadcaster()    
    br.sendTransform((data.pose.pose.position.x, data.pose.pose.position.y, data.pose.pose.position.z), tf.transformations.quaternion_from_euler(data.pose.pose.orientation.x, data.pose.pose.orientation.y, data.pose.pose.orientation.z), rospy.Time.now(), "base_link", "odom")

if __name__ == '__main__':
    rospy.init_node('base_link_to_map')
    rospy.set_param('use_sim_time', True)    
    rospy.Subscriber('/odometry/filtered_map', Odometry, handle_GPS_Data)
    rospy.spin()
