#!/usr/bin/env python

from niryo_one_python_api.niryo_one_api import *
import rospy
import time
rospy.init_node('niryo_one_example_python_api')

n = NiryoOne()

n.move_pose(0.255, 0.264, 0.15, 0.073, 1.577, 1.558)
n.move_pose(0.255, 0.264, 0.115, 0.073, 1.577, 1.558)
n.close_gripper(TOOL_GRIPPER_1_ID, 1000)
n.move_pose(0.255, 0.264, 0.15, 0.073, 1.577, 1.558)
n.move_pose(0.262, 0.193, 0.15, 0, 1.55, -1.601)
n.wait(2)
n.move_pose(0.262, 0.193, 0.115, 0, 1.55, -1.601)
n.open_gripper(TOOL_GRIPPER_1_ID, 250)
n.move_pose(0.262, 0.193, 0.15, 0, 1.55, -1.601)
n.move_pose(0.262, 0.193, 0.115, 0, 1.55, -1.601)
n.close_gripper(TOOL_GRIPPER_1_ID, 1000)
n.move_pose(0.262, 0.193, 0.15, 0, 1.55, -1.601)
n.move_pose(0.255, 0.264, 0.15, 0.073, 1.577, 1.558)
n.move_pose(0.255, 0.264, 0.115, 0.073, 1.577, 1.558)
n.open_gripper(TOOL_GRIPPER_1_ID, 250)
n.move_pose(0.255, 0.264, 0.15, 0.073, 1.577, 1.558)
