#! /usr/bin/env python

import rospy
from inverted_pendulum_sim.srv import *


class Parameters():
    def __init__(self) -> None:
        rospy.init_node("Initial_parameters")

        rospy.wait_for_service("/inverted_pendulum/set_params")

        self.params()

    def params(self):
        try:
            self.data = rospy.ServiceProxy(
                "/inverted_pendulum/set_params", SetParams)

            self.setParameter = SetParamsRequest()
            # Set the parameters as given in task-1.
            self.setParameter.pendulum_mass = 2
            self.setParameter.pendulum_length = 300
            self.setParameter.cart_mass = 0.5
            self.setParameter.theta_0 = 0
            self.setParameter.theta_dot_0 = 0
            self.setParameter.theta_dot_dot_0 = 0
            self.setParameter.cart_x_0 = 0
            self.setParameter.cart_x_dot_0 = 0
            self.setParameter.cart_x_dot_dot_0 = 0

            resp1 = self.data(self.setParameter)
            # resp1 = self.data(2, 300, 0.5, 0, 0, 0, 0, 0, 0)
            print(resp1)
        except rospy.exceptions as e:
            print("Service failed: %s" % e)


if __name__ == "__main__":
    Parameters()
