#!/usr/bin/env python

import rospy
import sys
from inverted_pendulum_sim.msg import *
import math


class Swing():

    def __init__(self) -> None:
        # Initialize Node
        rospy.init_node("sinusoidal_oscllation_node", anonymous=True)
        rospy.loginfo("Sinusoidal force activated.")

        self.pub = rospy.Publisher("/inverted_pendulum/control_force",
                                   ControlForce, queue_size=10)
        self.rate = rospy.Rate(100)  # 100Hz

        self.t = 0
        self.force_object = ControlForce()
        # 5-50,40
        self.frequency = 20
        self.amplitude = 10

        self.main()

    def main(self):
        while not rospy.is_shutdown():
            # Equation of Sinusoidal force
            self.force_object.force = self.amplitude * \
                math.sin(2 * math.pi * self.frequency * self.t)

            self.pub.publish(self.force_object)
            self.t += 0.001

            self.rate.sleep()

        # force_object = ControlForce()

        # def callback(msg):
        #     pass

        # sub = rospy.Subscriber(
        #     "/inverted_pendulum/current_state", CurrentState, callback)
        # rospy.spin()


if __name__ == "__main__":
    Swing()
