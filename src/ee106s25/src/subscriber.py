#!/usr/bin/env python3
from ee106s25.msg import EE106lab_custom
import rospy
from std_msgs.msg import String

def callback(data):
    # Combine all information into a single string
    log_msg = (f"Got int = {data.int_data}, "
              f"float = {data.float_data:.2f}, "
              f"str = {data.string_data}, "
              f"time_delay = {(rospy.Time.now()-data.header.stamp).to_sec():.3f}s")
    rospy.loginfo(log_msg)

def listener_custom():
    rospy.init_node('listener_custom')
    rospy.Subscriber('custom_topic', EE106lab_custom, callback)
    rospy.spin()

if __name__ == '__main__':
    listener_custom()
