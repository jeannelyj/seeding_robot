#! /usr/bin/env python
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

robot=moveit_commander.RobotCommander()
scene=moveit_commander.PlanningSceneInterface()
display_trajectory_publisher=rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)

arm1_group=moveit_commander.MoveGroupCommander("arm1")
arm1_group.set_named_target("arm1extend")
plan1=arm1_group.go()

hand1_group=moveit_commander.MoveGroupCommander("hand1")
hand1_group.set_named_target("hand1extend")
plan2=hand1_group.go()

arm1_group=moveit_commander.MoveGroupCommander("arm1")
arm1_group.set_named_target("arm1retract")
plan1=arm1_group.go()

arm2_group=moveit_commander.MoveGroupCommander("arm2")
arm2_group.set_named_target("arm2takeseed2")
plan3=arm2_group.go()

hand2_group=moveit_commander.MoveGroupCommander("hand2")
hand2_group.set_named_target("hand2extend")
plan4=hand2_group.go()

hand2_group=moveit_commander.MoveGroupCommander("hand2")
hand2_group.set_named_target("hand2retract")
plan4=hand2_group.go()

arm2_group=moveit_commander.MoveGroupCommander("arm2")
arm2_group.set_named_target("arm2putseedpos1")
plan3=arm2_group.go()

hand2_group=moveit_commander.MoveGroupCommander("hand2")
hand2_group.set_named_target("hand2extend")
plan4=hand2_group.go()

hand2_group=moveit_commander.MoveGroupCommander("hand2")
hand2_group.set_named_target("hand2retract")
plan4=hand2_group.go()

arm2_group=moveit_commander.MoveGroupCommander("arm2")
arm2_group.set_named_target("arm2putseedpos2")
plan3=arm2_group.go()

hand2_group=moveit_commander.MoveGroupCommander("hand2")
hand2_group.set_named_target("hand2extend")
plan4=hand2_group.go()

arm2_group=moveit_commander.MoveGroupCommander("arm2")
arm2_group.set_named_target("arm2takeseed1")
plan3=arm2_group.go()

hand1_group=moveit_commander.MoveGroupCommander("hand1")
hand1_group.set_named_target("hand1retract")
plan2=hand1_group.go()

arm1_group=moveit_commander.MoveGroupCommander("arm1")
arm1_group.set_named_target("arm11original")
plan1=arm1_group.go()

rospy.sleep(5)
moveit_commander.roscpp_shutdown()
