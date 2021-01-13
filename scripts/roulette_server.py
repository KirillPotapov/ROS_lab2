#!/usr/bin/env python

from __future__ import print_function

from ros_lab2.srv import GetRouletteRoll, GetRouletteRollResponse
import rospy
import random


def get_roll_roulette_result(req):
    print("color: ", req.color)
    print("number:", req.number)

    red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

    if ((req.color == 'green') and (req.number == 0)) or \
       ((req.color == 'red') and (req.number  in red)) or \
       ((req.color == 'black') and (req.number in black)):

        result = ['win', 'lose']
        random.shuffle(result)
        response = 'you ' + result[0]

    else:
        response = 'Wrong color or number out of range'

    return GetRouletteRollResponse(response)


def roll_roulette_server():
    rospy.init_node('roll_roulette_server')
    s = rospy.Service('roll_roulette', GetRouletteRoll, get_roll_roulette_result)
    print("Ready to roll the roulette.")
    rospy.spin()


if __name__ == "__main__":
    roll_roulette_server()
