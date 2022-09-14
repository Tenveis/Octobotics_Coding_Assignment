#!/usr/bin/env python

import rospy
from inverted_pendulum_sim.msg import ControlForce, CurrentState
from simple_pid import PID
import math
from inverted_pendulum_sim.srv import *


rospy.wait_for_service("/inverted_pendulum/set_params")
SetValueService = rospy.ServiceProxy(
    "/inverted_pendulum/set_params", SetParams)

# Set initial Parameters
resp1 = SetValueService(2, 300, 0.5, 3.3, 0, 0, 0, 0, 0)  # 3.3, 3.0

# Initiate Node
rospy.init_node("Balancing_node", anonymous=True)

pub = rospy.Publisher("/inverted_pendulum/control_force",
                      ControlForce, queue_size=10)

rate = rospy.Rate(100)

force_object = ControlForce()
pid = PID(130, 50, 50, setpoint=math.pi, output_limits=(-20, 20))
theta = math.pi
angle = 0


def callback(msg):
    angle = msg.curr_theta
    force_object.force = pid(angle)

    pub.publish(force_object)


sub = rospy.Subscriber(
    "/inverted_pendulum/current_state", CurrentState, callback)
rospy.spin()
