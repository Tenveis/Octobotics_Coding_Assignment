#!/usr/bin/env python

import rospy
import sys
from inverted_pendulum_sim.msg import ControlForce
import math


def main():
    # Initialize Node
    rospy.init_node("sinusoidal_oscllation_node", anonymous=True)
    rospy.loginfo("Sinusoidal force activated.")

    pub = rospy.Publisher("/inverted_pendulum/control_force",
                          ControlForce, queue_size=10)
    rate = rospy.Rate(100)  # 100Hz

    t = 0
    force_object = ControlForce()
    # 5-50,40
    frequency = 20
    amplitude = 10
    while not rospy.is_shutdown():
        #Equation of Sinusoidal force
        force_object.force = amplitude * \
            math.sin(2 * math.pi * frequency * t)

        pub.publish(force_object)
        t += 0.001

        rate.sleep()


if __name__ == "__main__":
    main()
