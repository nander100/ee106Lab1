#!/usr/bin/env python3
from ee106s25.msg import EE106lab_custom_new
import rospy
from std_msgs.msg import String

def callback(data):
    sum = data.int_rand1 + data.int_rand2
    # Combine all information into a single string
    log_msg = (f"random int 1 = {data.int_rand1}, "
              f"random int 2 = {data.int_rand2}, "
              f"sum = {sum}"
              f"time_delay = {(rospy.Time.now()-data.header.stamp).to_sec():.3f}s")
    rospy.loginfo(log_msg)

def listener_custom():
    rospy.init_node('listener_custom')
    rospy.Subscriber('custom_topic', EE106lab_custom_new, callback)
    rospy.spin()

if __name__ == '__main__':
    listener_custom()
