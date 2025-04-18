#!/usr/bin/env python3

import rospy
from ee106s25.msg import EE106lab_custom

def talker():
    rospy.init_node('talker')
    pub = rospy.Publisher('custom_topic', EE106lab_custom, queue_size = 10)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
      msg = EE106lab_custom()
      msg.header.stamp = rospy.Time.now()
      msg.int_data = 5
      msg.float_data = 0.5
      msg.string_data = 'Hello'
      pub.publish(msg)
      rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
