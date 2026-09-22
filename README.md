# ROS2 Publisher-Subscriber Example

A minimal ROS2 (Lyrical) Python package demonstrating node-to-node communication using the publisher-subscriber pattern — the foundational communication model used in robotics and autonomous systems.

## Overview

This project contains two independent ROS2 nodes:

- **Publisher (`talker`)**: publishes a string message to the `topic` channel every second.
- **Subscriber (`listener`)**: subscribes to `topic` and logs every message it receives in real time.

The two nodes run as separate processes and communicate entirely through ROS2's messaging system, showing how distributed robotic components (e.g. a sensor node and a control node) exchange data.

## Tech Stack

- Python 3
- ROS2 (rclpy)
- std_msgs

## Setup

```bash
# from your ROS2 workspace src folder
git clone https://github.com/aysesilankarabulut/ros2-publisher-subscriber-python.git my_first_node
cd ~/ros2_ws
colcon build
source install/setup.bash
```

## Usage

Run the publisher in one terminal:

```bash
ros2 run my_first_node talker
```

Run the subscriber in another terminal:

```bash
ros2 run my_first_node listener
```

The subscriber terminal will print each message published by the talker in real time.

## What I Learned

- ROS2 workspace structure and the `colcon` build system
- Creating and structuring a ROS2 Python package
- Implementing a `Node`, `Publisher`, and `Subscriber` using `rclpy`
- Debugging Python packaging issues (`setup.py`, `entry_points`)
- Git/GitHub workflow for version control

## Author

Ayşe Şilan Karabulut — Computer Engineering student, KTO Karatay University

