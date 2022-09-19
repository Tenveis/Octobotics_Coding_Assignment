#!/usr/bin/env python

import rospy
from inverted_pendulum_sim.msg import ControlForce, CurrentState
from simple_pid import PID
import math
from inverted_pendulum_sim.srv import *


class Balance():

    def __init__(self) -> None:

        rospy.wait_for_service("/inverted_pendulum/set_params")
        self.SetValueService = rospy.ServiceProxy(
            "/inverted_pendulum/set_params", SetParams)

        # Set initial Parameters
        self.resp1 = self.SetValueService(
            2, 300, 0.5, 3.3, 0, 0, 0, 0, 0)  # 3.3, 3.0

        # Initiate Node
        rospy.init_node("Balancing_node", anonymous=True)

        self.pub = rospy.Publisher("/inverted_pendulum/control_force",
                                   ControlForce, queue_size=10)

        self.rate = rospy.Rate(100)

        self.force_object = ControlForce()
        self.theta = math.pi
        self.angle = 0
        self.pid = PID(130, 50, 50, setpoint=self.theta,
                       output_limits=(-20, 20))

        self.main()

    def callback(self, msg):
        self.angle = msg.curr_theta
        self.force_object.force = self.pid(self.angle)
  
        self.pub.publish(self.force_object)

    def main(self):
        self.sub = rospy.Subscriber(
            "/inverted_pendulum/current_state", CurrentState, self.callback)
        rospy.spin()


if __name__ == "__main__":
    Balance()
