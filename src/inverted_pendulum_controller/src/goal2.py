#!/usr/bin/env python

import rospy
import sys
from inverted_pendulum_sim.msg import CurrentState, ControlForce
import math


class Swing():

    def __init__(self) -> None:
        # Initialize Node
        rospy.init_node("sinusoidal_oscllation_node", anonymous=True)
        rospy.loginfo("Sinusoidal force activated.")

        self.pub = rospy.Publisher("/inverted_pendulum/control_force",
                                   ControlForce, queue_size=10)
        sub = rospy.Subscriber(
            "/inverted_pendulum/current_state", CurrentState, self.callback)

        self.rate = rospy.Rate(100)  # 100Hz

        self.t = 0
        self.force_object = ControlForce()
        # 5-50,40
        self.frequency = 20
        self.amplitude = 10

        self.main()

    def callback(self, msg):
        print("curr_x:", msg.curr_x)
        print("curr_x_dot:", msg.curr_x_dot)
        print("curr_x_dot_dot:", msg.curr_x_dot_dot)
        print("curr_theta:", msg.curr_theta)
        print("curr_theta_dot:", msg.curr_theta_dot)
        print("curr_theta_dot_dot:", msg.curr_theta_dot_dot)
        print("-----------------------------------------------")

        if (0 <= msg.curr_theta) and (msg.curr_theta < 0.8):
            self.force_object.force = 50
            # self.pub.publish(self.force_object)
        elif (-0.8 < msg.curr_theta) and (msg.curr_theta < -0.1):
            self.force_object.force = -50

        self.pub.publish(self.force_object)

    def main(self):
        # while not rospy.is_shutdown():
        #     # Equation of Sinusoidal force
        #     self.force_object.force = self.amplitude * \
        #         math.sin(2 * math.pi * self.frequency * self.t)

        #     self.pub.publish(self.force_object)
        #     self.t += 0.001

        #     self.rate.sleep()
        rospy.spin()


if __name__ == "__main__":
    Swing()
