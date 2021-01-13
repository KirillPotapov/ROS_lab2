#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
import string
import random
from ros_lab2.srv import *


def roulette_client(clr, numb):
    rospy.wait_for_service('roll_roulette')
    try:
        roll_roulette = rospy.ServiceProxy('roll_roulette', GetRouletteRoll)
        resp1 = roll_roulette(clr, numb)
        return resp1.roll_result
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)


if __name__ == "__main__":
    rospy.init_node('client', anonymous=True)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():

        color_list = ['green', 'red', 'black']
        random.shuffle(color_list)
        color = color_list[0]

        number = random.randrange(0, 37)
        print("Requesting roll result for: {color} {number}")
        print(roulette_client(color, number))
        rate.sleep()
