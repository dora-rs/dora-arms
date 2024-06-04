import argparse
import os
import time
from pathlib import Path

import h5py
from reachy2_sdk import ReachySDK
import pyarrow as pa
from dora import Node
import numpy as np

freq = 30

# ret, image = cap.read()
# reachy = ReachySDK("172.16.0.74")

reachy = ReachySDK("192.168.1.51")

reachy.turn_on()

time.sleep(1)
action = [
    -0.11903145498601328,
    0.11292280260403312,
    0.48048914307403895,
    -1.4491468779308918,
    0.1895427567665842,
    0.009599310885968814,
    -0.20141099568014562,
    2.2656896114349365,
    -0.13212142437597074,
    -0.07731808586334879,
    -0.5141739976375295,
    -1.512502329778286,
    0.00034906585039886593,
    0.3193952531149623,
    0.40474185353748504,
    2.2610876560211,
]

# action = [
# -0.1253,
# 0.1162,
# 0.4838,
# -1.4453,
# 0.1571,
# 0.0061,
# -0.2053,
# 2.2672,
# -0.1442,
# -0.0822,
# -0.5131,
# -1.5139,
# -0.0000,
# 0.3192,
# 0.4039,
# 2.2626,
# ]


reachy.l_arm.shoulder.pitch.goal_position = np.rad2deg(action[0])
reachy.l_arm.shoulder.roll.goal_position = np.rad2deg(action[1])
reachy.l_arm.elbow.yaw.goal_position = np.rad2deg(action[2])
reachy.l_arm.elbow.pitch.goal_position = np.rad2deg(action[3])
reachy.l_arm.wrist.roll.goal_position = np.rad2deg(action[4])
reachy.l_arm.wrist.pitch.goal_position = np.rad2deg(action[5])
reachy.l_arm.wrist.yaw.goal_position = np.rad2deg(action[6])
reachy.l_arm.gripper.set_opening(min(100, max(0, action[7] * 40)))

reachy.r_arm.shoulder.pitch.goal_position = np.rad2deg(action[8])
reachy.r_arm.shoulder.roll.goal_position = np.rad2deg(action[9])
reachy.r_arm.elbow.yaw.goal_position = np.rad2deg(action[10])
reachy.r_arm.elbow.pitch.goal_position = np.rad2deg(action[11])
reachy.r_arm.wrist.roll.goal_position = np.rad2deg(action[12])
reachy.r_arm.wrist.pitch.goal_position = np.rad2deg(action[13])
reachy.r_arm.wrist.yaw.goal_position = np.rad2deg(action[14])
reachy.r_arm.gripper.set_opening(min(100, max(0, action[15] / 2.26 * 100)))
time.sleep(1)
# start = time.time()
node = Node()
for event in node:
    id = event["id"]
    match id:
        case "action":
            action = event["value"].to_numpy()
            reachy.l_arm.shoulder.pitch.goal_position = np.rad2deg(action[0])
            reachy.l_arm.shoulder.roll.goal_position = np.rad2deg(action[1])
            reachy.l_arm.elbow.yaw.goal_position = np.rad2deg(action[2])
            reachy.l_arm.elbow.pitch.goal_position = np.rad2deg(action[3])
            reachy.l_arm.wrist.roll.goal_position = np.rad2deg(action[4])
            reachy.l_arm.wrist.pitch.goal_position = np.rad2deg(action[5])
            reachy.l_arm.wrist.yaw.goal_position = np.rad2deg(action[6])
            reachy.l_arm.gripper.set_opening(min(100, max(0, action[7] / 2.26 * 100)))

            reachy.r_arm.shoulder.pitch.goal_position = np.rad2deg(action[8])
            reachy.r_arm.shoulder.roll.goal_position = np.rad2deg(action[9])
            reachy.r_arm.elbow.yaw.goal_position = np.rad2deg(action[10])
            reachy.r_arm.elbow.pitch.goal_position = np.rad2deg(action[11])
            reachy.r_arm.wrist.roll.goal_position = np.rad2deg(action[12])
            reachy.r_arm.wrist.pitch.goal_position = np.rad2deg(action[13])
            reachy.r_arm.wrist.yaw.goal_position = np.rad2deg(action[14])
            reachy.r_arm.gripper.set_opening(min(100, max(0, action[15] / 2.26 * 100)))
        case "tick":

            qpos = {
                "l_arm_shoulder_pitch": np.deg2rad(
                    reachy.l_arm.shoulder.pitch.present_position
                ),
                "l_arm_shoulder_roll": np.deg2rad(
                    reachy.l_arm.shoulder.roll.present_position
                ),
                "l_arm_elbow_yaw": np.deg2rad(reachy.l_arm.elbow.yaw.present_position),
                "l_arm_elbow_pitch": np.deg2rad(
                    reachy.l_arm.elbow.pitch.present_position
                ),
                "l_arm_wrist_roll": np.deg2rad(
                    reachy.l_arm.wrist.roll.present_position
                ),
                "l_arm_wrist_pitch": np.deg2rad(
                    reachy.l_arm.wrist.pitch.present_position
                ),
                "l_arm_wrist_yaw": np.deg2rad(reachy.l_arm.wrist.yaw.present_position),
                "l_gripper": reachy.l_arm.gripper._present_position,
                "r_arm_shoulder_pitch": np.deg2rad(
                    reachy.r_arm.shoulder.pitch.present_position
                ),
                "r_arm_shoulder_roll": np.deg2rad(
                    reachy.r_arm.shoulder.roll.present_position
                ),
                "r_arm_elbow_yaw": np.deg2rad(reachy.r_arm.elbow.yaw.present_position),
                "r_arm_elbow_pitch": np.deg2rad(
                    reachy.r_arm.elbow.pitch.present_position
                ),
                "r_arm_wrist_roll": np.deg2rad(
                    reachy.r_arm.wrist.roll.present_position
                ),
                "r_arm_wrist_pitch": np.deg2rad(
                    reachy.r_arm.wrist.pitch.present_position
                ),
                "r_arm_wrist_yaw": np.deg2rad(reachy.r_arm.wrist.yaw.present_position),
                "r_gripper": reachy.r_arm.gripper._present_position,
            }

            # node.send_output("agent_pos", pa.array(states[index].numpy()))
            # index += 1
            node.send_output("agent_pos", pa.array(qpos.values()))
